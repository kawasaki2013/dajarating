# -*- coding: utf-8 -*-
import dajarep
import stt
import os
import commands
from janome.tokenizer import Tokenizer

dajarep.TOKENIZER = Tokenizer()

print("ではどうぞ、")

out=commands.getstatusoutput('rec --encoding signed-integer --bits 16 --channels 1 --rate 16000 ./test.wav trim 0 3')

filename =os.path.join(os.path.dirname(__file__), "test.wav")
#text=u"布団が吹っ飛んだ"
text=stt.stt_google_wav(filename)
dajare=dajarep.dajarep(text)

say=""
if(dajare!=""):
    say="ダジャレですね."
    point=int(abs(round(hash(dajare) % 100,0)))
    say=say+str(point)+"点です"
else:
    say="ダジャレではないですね"
print(say)
print(u"->"+text)
commands.getstatusoutput('say '+say)
