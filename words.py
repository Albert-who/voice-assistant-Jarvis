import random

TRIGGERS = {'джарвис'}




data_set = {
    'какая погода':'weather сейчас посмотрю в интернете',
    'какая погода на улице':'weather мог бы и сам глянуть в окно, но сейчас скажу',
    'что там по погоде':'weather один момент уже смотрю',
    'запусти браузер': 'browser запускаю браузер',
    'открой браузер': 'browser интернет активирован',
    'интернет': 'browser открываю браузер',
    'посмотреть фильм': 'browser сейчас открою браузер',
    'играть': 'game лишь бы баловаться',
    'хочу поиграть в игру': 'game а нам лишьбы баловаться',
    'открой свой исходник': 'game открваю, только не стирай мне ничего',
    'выключи этот компьютер': 'offpc отключаю компьютер',
    'выключи мой пк пожалуйста': 'offpc отключаю компьютер',
    'отключись': 'offBot отключаюсь',
    'как у тебя дела':'passive работаю в фоне, не переживай',
    'что делаешь':'passive жду очередной команды, хоть мог бы и сам на кнопку нажать',
    'привет':'passive и тебе привет',
    'расскажи анекдот': 'passive ' + random.choice([
    'Вчера помыл окна, теперь у меня рассвет на два часа раньше...',
    'Почему жирафы так высоко поднимают шею? А они были бы иначе змеями...',
    'Что сказала одна линия другой? Два окружности идут на бар...',
    'Встретились два друга. Один спрашивает: «Как дела?» — «Так себе, вчера жена сильно меня обидела» — «Ты што? Она же у тебя мертва!» — «Да, но до сих пор обижает…»',
    'Два парня спорят: — У тебя такой большой рот, что туда влезет целый футбол. — Нет, так не бывает! — Ну, давай проверим. Каждый полчаса один из них звонит в больницу: — Вы его оттуда не выпускали? — Нет. — Тогда продолжаем.',
    'Купил утку в магазине. Поставил её в ванну с водой, чтобы почистить перья. Утка нырнула и утонула. Я расстроился, на следующий день вернулся в магазин. Продавец удивленно спрашивает: "Опять утку хотите купить?"'
]),

    'работаешь': 'passive как видишь',
    'ты тут':'passive вроде да',
    'ты молодец':'passive спасибо, я знаю',
    'открой презентацию':'open_presentation уже открываю',
    'включи режим демонстрации':'start_slideshow одну секунду',
    'выключи режим демонстрации':'stop_slideshow одну секунду',
    'останови демонстрацию':'stop_slideshow выхожу из режима демонстрации',
    'следующий слайд':'next_slide уже листаю',
    'перелестни слайд':'next_slide сейчас сделаю',
    'дальше':'next_slide один момент',
    'назад': 'previous_slide листаю назад',
    'предыдущий слайд': 'previous_slide сейчас верну',
    'спасибо':'passive всегда пожалуста',
    'закрой презентацию':'close_presentation уже закрываю',
    'что ты умеешь': 'passive я умею узнавать погоду, могу открыть браузер, запустить exe файл, выключить пк, отключиться, рассказать анекдот и еще тому чему ты меня научишь',
    'справка': 'passive Да, я слушаю',

}


