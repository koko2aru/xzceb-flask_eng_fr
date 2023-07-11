#Translator
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    #Translator English to French
    french_text = MyMemoryTranslator(source='GB-en', target='FR-fr').translate(english_text)
    print(french_text)
    return french_text
    
def french_to_english(french_text):
    #Translator French to English
    english_text = MyMemoryTranslator(source='FT-fr', target='GB-en').translate(french_text)
    print(english_text)
    return english_text