import pyttsx3	

#  Иницилизация 
engine = pyttsx3.init()


# voices = engine.getProperty('voices')
# for voice in voices:
#     print(voice.id)
voice_id = 'Ваш выбранный voice.id'
# настройка параметров
engine.setProperty('voice', voice_id)
engine.setProperty('rate', 160)				#скорость речи


def speaker(text):
	'''Озвучка текста'''
	engine.say(text)
	engine.runAndWait()