# -*- coding: utf-8 -*-

from googletrans import Translator

class Translator():
    def __init__(self):
        pass
    
    def translate_text(self,text: str, dest_lang: str) -> str:
        """
        translates text from one language to another.

        :param text: text to be translated
        :param dest_lang: output language code (such as 'zh-cn')
        :return: text translated
        """
        translator = Translator()
        try:
            # Auto detect the language of the text
            detected_lang = translator.detect(text).lang
            translation = translator.translate(text, src=detected_lang, dest=dest_lang)
            return translation.text
        except Exception as e:
            return f"translate_text error: {e}"

