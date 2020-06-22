from gtts import gTTS 

import os
fh = open("test.txt","r")
myText = fh.read().replace("\n"," ")

language= 'en'

output = gTTS(text=myText,lang=language ,slow=False)
fh.close()
output.save("output.mp3")
os.system("start output.mp3")
