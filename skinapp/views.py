from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from skinapp.serializers import RegistrationSerializer
# from quickstart.serializers import PledgeSerializer, PledgeListSerializer,PledgeDetailSerializer,MessageAccountSerializer
# from quickstart.models import pledgefeed
from skinapp.models import Account
from django.http.response import JsonResponse
import requests
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser
from .apps import *
import numpy as np
from keras.preprocessing import image
from skimage import transform
import time
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import *
import tensorflow
import json
from PIL import *
import base64
from datetime import date
# Create your views here.
class UploadView(APIView):
    # permission_classes = [IsAuthenticated]

    parser_classes = (
        MultiPartParser,
        JSONParser,
    )
    # parser_classes = [FileUploadParser]

    @staticmethod
    def post(request):
        files = request.data.get('picture')
        file=files.replace("data:image/jpeg;base64", "")
        imgdata = base64.b64decode(file)
        filename = 'androidparty1.jpg'
        img = Image.new('RGB', (300, 300), color = 'red')
        img.save('androidparty1.jpg')
        with open (filename, 'wb') as f:
            f.write(imgdata)




        #load models
        resnet_chest = ProdModelConfig.model


#working code
        img = Image.open(filename)
        img = img.resize((128, 128), Image.ANTIALIAS)
        x = image.img_to_array(img)
        # x=x/255
        np_image =x.reshape(1,128, 128,3)

        resnet_pred = resnet_chest.predict(np_image)
        print(resnet_pred)
        probability = resnet_pred[0]
        print(probability)

        prob=list(probability)
        # prob[3]=0.02+prob[3]
        # prob[7]=0.07+prob[7]


        tmp = max(prob)
        print(prob)
        index = prob.index(tmp)
        if tmp<0.97:
            index=8
        print(index)
        disease=""
        if index==0:
            disease="Acne"
            detail="Acne is a common skin condition that affects most people at some point, mainly developed in the face, back and chest. It causes spots, oily skin and sometimes skin that's hot or painful to touch. Acne is most commonly linked to the changes in hormone levels during puberty, but can start at any age."

        elif index==1:
            disease="Basal Cell Carcinoma"
            detail="Basal cell carcinoma is a type of skin cancer. Basal cell carcinoma begins in the basal cells — a type of cell within the skin that produces new skin cells as old ones die off. Basal cell carcinoma often appears as a slightly transparent bump on the skin, though it can take other forms. Basal cell carcinoma occurs most often on areas of the skin that are exposed to the sun, such as your head and neck. Most basal cell carcinomas are thought to be caused by long-term exposure to ultraviolet (UV) radiation from sunlight. Avoiding the sun and using sunscreen may help protect against basal cell carcinoma."

        elif index==2:
            disease="Eczema"
            detail="Eczema is a condition that causes the skin to become itchy, dry and cracked. Atopic eczema is more common in children, often developing before their first birthday. But it may also develop for the first time in adults.It's usually a long-term (chronic) condition, although it can improve significantly, or even clear completely, in some children as they get older."

        elif index==3:
            disease="Melanoma Cancer"
            detail="Melanoma (also called malignant melanoma) is a cancer that usually starts in the skin. It can start in a mole or in normal-looking skin. Melanoma develops from cells called melanocytes that start to grow and divide more quickly than usual. It's important to find and treat melanoma as early as possible. Melanomas that are only in the upper layer of skin are unlikely to spread into the blood or lymphatic vessels. They are usually cured with surgery"

        elif index==4:
            disease="Psoriasis"
            detail="Psoriasis is a skin condition that causes red, flaky, crusty patches of skin covered with silvery scales. These patches normally appear on your elbows, knees, scalp and lower back, but can appear anywhere on your body. The severity of psoriasis varies greatly from person to person. For some it's just a minor irritation, but for others it can majorly affect their quality of life."

        elif index==5:
            disease="Ringworm"
            detail="Ringworm is a common skin infection that is caused by a fungus. It’s called “ringworm” because it can cause a circular rash (shaped like a ring) that is usually red and itchy. Anyone can get ringworm. The fungi that cause this infection can live on skin, surfaces, and on household items such as clothing, towels, and bedding.Ringworm goes by many names. The medical terms are “tinea” or “dermatophytosis."

        elif index==6:
            disease="Squamous Cell Carcinoma"
            detail="Squamous cell carcinoma of the skin is a common form of skin cancer that develops in the squamous cells that make up the middle and outer layers of the skin. Squamous cell carcinoma of the skin is usually not life-threatening, though it can be aggressive. Untreated, squamous cell carcinoma of the skin can grow large or spread to other parts of your body, causing serious complications."
        elif index==7:
            disease="Vitiligo"
            detail="Vitiligo is a long-term condition where pale white patches develop on the skin. It's caused by the lack of melanin, which is the pigment in skin. Vitiligo can affect any area of skin, but it commonly happens on the face, neck and hands, and in skin creases."
        elif index==8:
            disease="No Skin Disease Image Found"
            detail="Kindly rescan or upload valid skin disorder image"
        # #print("Resnet Predictions:")
        # if probability[0] > 0.5:
        #     resnet_chest_pred = str('%.2f' % (probability[0]*100) + '% COVID')
        # else:
        #     resnet_chest_pred = str('%.2f' % ((1-probability[0])*100) + '% NonCOVID')
        # #print(resnet_chest_pred)
        # #print(xception_chest_pred)
        return Response({
            'status': 'success',
            'Prediction':disease,
            'Detail':detail,
        }, status=201)






#Regview
@api_view(['POST',])
def registration_view(request):
    if request.method=='POST':
        serializer = RegistrationSerializer(data = request.data)
        data={}
        if serializer.is_valid():
            account= serializer.save()
            data['status']=200
            data['response']= "Your profile was successfully created"
            data['email'] = account.email
            tr=account.email
            data['username'] = account.username
            # acc = Account.objects.get(email=tr)
            # print(acc)
            # rt=acc.id
            # print(rt)
            # refresh = RefreshToken.for_user(tr)
            # print(refresh)
            # data['token']=refresh.access_token
            #url = 'http://127.0.0.1:800/api/v1/login/'
            #Update
            # url = 'http://djangotutorial51-env-2.eba-s6ipw463.us-west-2.elasticbeanstalk.com/api/v1/login/'
            # myobj = {'email': tr,
            #          'password':'password'}
            #
            # x = requests.post(url, data=myobj)
            # time.sleep(3)
            # print(x.json())
            # data['token'] = x.json()['access']

        else:
            data = serializer.errors

        return Response(data)

# Create your views here.
