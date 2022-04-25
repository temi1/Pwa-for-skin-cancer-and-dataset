from django.apps import AppConfig
import os
from django.apps import AppConfig
from django.conf import settings
from tensorflow import keras
from keras.models import load_model


class ProdModelConfig(AppConfig):
    name = 'prodAPI'
    # MODEL_FILE = os.path.join(settings.MODELS, "FinalProductionmodel.h5")
    MODEL_FILE = os.path.join(settings.MODELS, "FinalProductionmodel.h5")

    model = keras.models.load_model(MODEL_FILE)



class SkinappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'skinapp'
