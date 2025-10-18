from translate import Translator
import requests
from collections import defaultdict


class TextAnalysis():   
    
    memory=defaultdict(list)

    def __init__(self, text, owner):

        TextAnalysis.memory[owner].append(self)

        self.text = text
        self.translation = self.__translate(self.text, "tr", "en")

        
        self.response = self.get_answer()

    
    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "tr")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            translator= Translator(from_lang=from_lang,to_lang=to_lang)
            ceviri= translator.translate(text)
            return ceviri
        except:
            return "Çeviri girişimi başarısız oldu"