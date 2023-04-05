import os
import webbrowser
import sys
import subprocess
import pyautogui
import voice
import requests	


def browser():
	'''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

	webbrowser.open('https://www.youtube.com', new=2)
	

def game():
	'''Нужно разместить путь к exe файлу любого вашего приложения'''
	try:
		subprocess.Popen('Ваш путь к файлу.exe')
	except:
		voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')


def open_presentation():
    '''Открыть презентацию'''
    try:
        os.startfile('Ваш путь к презентации')
    except:
        voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')
	
def close_presentation():
    '''Закрыть презентацию'''
    try:
        os.system('taskkill /f /im POWERPNT.EXE')
    except:
        voice.speaker('Не удалось закрыть презентацию')

def next_slide():
    '''Перейти на следующий слайд'''
    try:
        pyautogui.press('right')
    except:
	    voice.speaker('Похоже тебе самому придется перелестнуть слайд')

def previous_slide():
    '''Перейти на предыдущий слайд'''
    try:
        pyautogui.press('left')
    except:
	    voice.speaker('Похоже тебе самому придется вернуть слайд')

def start_slideshow():
    '''Запустить режим демонстрации'''
    try:
        pyautogui.press('f5')
	    
    except:
        voice.speaker('У меня не получилось включить режим демонстрации')

def stop_slideshow():
    '''Остановить режим демонстрации'''
    try:
        pyautogui.press('esc')
	    
    except:
	    voice.speaker('У меня не получилось выключить режим демонстрации')


def speak():
	pass


def offpc():
	#Эта команда отключает ПК под управлением Windows

	# os.system(r'shutdown /s')
	print('пк был бы выключен, но команде # в коде мешает;)))')


def weather():
	try:
		params = {'q': 'Novokuznetsk', 'units': 'metric', 'lang': 'ru', 'appid': 'Ваш API'}
		response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
		if not response:
			raise
		w = response.json()
		voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
		
	except:
		voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
	'''Отключает бота'''
	sys.exit()


def passive():
	'''Функция заглушка при простом диалоге с ботом'''
	pass


