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
        questions = {
            'adın ne?': "ben süper havalı bir botum ve amacım size yardım etmek!",
            'kaç yaşındasın?': "bu çok felsefi bir soru ama belli bir yaşım yok"
        }

        if self.text.lower() in questions.keys():
            return questions[self.text.lower()]
        else:
            return 'Cevap Bulamadım'


    def __translate(self, text, from_lang, to_lang):
        try:
            translator= Translator(from_lang=from_lang,to_lang=to_lang)
            ceviri= translator.translate(text)
            return ceviri
        except:
            return "Çeviri girişimi başarısız oldu"