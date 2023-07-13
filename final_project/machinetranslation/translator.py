"""Translator"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Translator English to French"""
    french_text = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """Translator French to English"""
    english_text = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(french_text)
    print(english_text)
    return english_text
