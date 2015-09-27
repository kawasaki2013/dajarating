# -*- coding: utf-8 -*-
import re

TOKENIZER=None

def dajarep(text):
    u"""
    与えられた文字列にダジャレが含まれていた場合、該当部分の読みを返す。
    """

    def fixWord(text):
        text=text.replace(u"ッ", u"[ツッ]?")
        text=text.replace(u"ー", u"[ー]?")
        text=text.replace(u"ァ", u"[アァ]?")
        text=text.replace(u"ィ", u"[イィ]?")
        text=text.replace(u"ゥ", u"[ウゥ]?")
        text=text.replace(u"ェ", u"[エェ]?")
        text=text.replace(u"ォ", u"[オォ]?")
        text=text.replace(u"ャ", u"[ヤャ]")
        text=text.replace(u"ュ", u"[ユュ]")
        text=text.replace(u"ョ", u"[ヨョ]")
        return text

    def fixText(text):
        text=text.replace(u"ッ", u"")
        text=text.replace(u"ー", u"")
        text=text.replace(u"、", u"")
        text=text.replace(u",", u"")
        text=text.replace(u" ", u"")
        text=text.replace(u"　", u"")

        return text

    tokens=TOKENIZER.tokenize(text)
    kana="".join([token.reading for token in tokens])
    for token in tokens:
        if token.part_of_speech.split(",")[0]==u"名詞" and len(token.reading)>1:
            if text.count(token.surface)<len(re.findall(fixWord(token.reading),fixText(kana))):
                return token.reading
    return ""