#Translator
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    #Translator English to French
    french_text = MyMemoryTranslator(source='GB-en', target='FR-fr').translate(english_text)
    print(french_text)
    return french_text
    
def french_to_english(french_text):
    #Translator French to English
    english_text = MyMemoryTranslator(source='FR-fr', target='GB-en').translate(french_text)
    print(english_text)
    return english_text

#unit test.py
import unittest
from mymodule import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Bad"), "Bonjour")  

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "good") 
        
unittest.main()