# -*- coding: utf-8 -*-
    
from translate import Translator
from langdetect import detect
from typing import Optional

def translator(text: str, target_lang: str = 'en') -> Optional[str]:
    """
    Automatically detect the language of the input text and translate it to the target language.
    
    :param text: The text to be translated.
    :type text: str
    :param target_lang: The language code to translate the text into, default is 'en' (English).
    :type target_lang: str
    :return: Translated text or None if translation fails.
    :rtype: Optional[str]
    """
    try:
        # Detect the language of the input text
        source_lang = detect(text)
        
        # Initialize the translator
        translator = Translator(from_lang=source_lang, to_lang=target_lang)
        
        # Translate the text
        translated_text = translator.translate(text)
        
        return translated_text
    except Exception as e:
        print(f"Error: {e}")
        return None

