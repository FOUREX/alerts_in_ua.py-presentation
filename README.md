# Приклади використання бібліотеки `Alerts-in-ua.py`

## Перед початком роботи
**Потрібен Python 3.10 і вище.**

Створіть та активуйте віртуальне середовище наступними командами:

```shell
# Створення віртуального середовища
python -m venv venv

# Активація віртуального середовища
venv\Scripts\activate
```

Для роботи програм необхідно встановити залежності наступною командою:

```sh
pip install -r requirements.txt
```


## CLI client
**Перейдіть в директорію `"CLI client"`**

Виведення тривог на даний момент. Використання параметрів не обов'язкове. Приклад використання:
```shell
py alerts.py
```

Перегляд доступних параметрів:
```shell
py alerts.py -h
```

Дані для відображення задаються параметром `-f`, `--format`.Доступні параметри дивитися
на сайті https://devs.alerts.in.ua/#modelalert (Назва поля). Приклад використання:
```shell
py alerts.py monitor -f "started_at" "location_title" "location_oblast" "location_uid"
```

Режим монітору. Дані будуть оновлюватися автоматично. Оновлення відбувається 3 рази за хвилину.
Частота оновлень змінюється параметрами `-freq`, `--frequency`. Приклад використання:
```shell
py alerts.py monitor -freq 5
```

Загальний вигляд та використання:
```shell
py alerts.py monitor -freq 4 -f "started_at" "location_title" "location_oblast" "location_uid"
```

![](assets/CLI%20client%20example.png)

# Yep

Тут ще щось буде

![](https://tenor.com/ru/view/pikachu-pokemon-tongue-out-wiggle-tongue-weird-face-gif-16364996.gif)