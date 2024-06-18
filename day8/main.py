from gtts import gTTS
from playsound import playsound

mytext = input("Enter the text: ")

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)


myobj.save("text.mp3")


print('playing sound using  playsound')
playsound('D:/other/Python/workshop/text.mp3')

