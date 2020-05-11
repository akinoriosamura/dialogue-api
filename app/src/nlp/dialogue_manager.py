from google.cloud import translate_v2 as translate
from src.nlp.parlai_api import ParlAI

import time


class DialogueManager(object):
    def __init__(self):        
        self.translate_client = translate.Client()
        self.parlai = ParlAI()

    def translate(self, text, tar_lang='ja'):
        result = self.translate_client.translate(text, target_language=tar_lang)
        # print(result['translatedText'])

        return result['translatedText']

    def get_reply(self, text):
        print("入力: ", text)
        en_translated = self.translate(text, tar_lang='en')
        print("en translate: ", en_translated)
        st = time.time()
        res_dialogue = self.parlai.dialogue(en_translated)
        print("dialogue time[s]: ", time.time() - st)
        print("reply by dialogue: ", res_dialogue)
        res_ja_translated = self.translate(res_dialogue, tar_lang='ja')
        print("translate reply: ",  res_ja_translated)

        return res_ja_translated

