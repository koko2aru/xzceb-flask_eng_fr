import os
import json
from deep_translator import MyMemoryTranslator


def englishToFrench(englishText):
    frenchText = MyMemoryTranslator(source='en', target='fr').translate(englishText)
    print(frenchText)
    return frenchText