# Приклади використання бібліотеки `Alerts-in-ua.py`

## Перед початком роботи
**Потрібен Python 3.10 і вище.**

Створіть та активуйте віртуальне середовище за допомогою наступних команд:

```shell
# Створення віртуального середовища
python -m venv venv

# Активація віртуального середовища
venv\Scripts\activate
```

Створіть `.env` файл в корені проекту в якому будуть зберігатися токени:
```dotenv
ALERTS_CLIENT_TOKEN=token
TELEGRAM_BOT_TOKEN=token
```

Для роботи програм необхідно встановити залежності наступною командою:

```sh
pip install -r requirements.txt
```


## CLI client
**Перейдіть в директорію `"CLI client"`**

Виведення тривог на даний момент (звичайний режим). Використання параметрів не обов'язкове. Приклад використання:
```shell
py alerts.py
```

### Параметри
- `-h`, `--help` - Виведення списку доступних параметрів.
- `monitor` - Режим монітора. Дані будуть оновлюватися автоматично декілька раз на хвилину.
- `-freq`, `--frequency` - Задає частоту оновлень даних в режимі монітора за хвилину.
- `-f`, `--format` - Список атрибутів локацій які будуть відображені в списку.
- `--show-image` - Відображення мапи тривог (не працює в режимі монітора).
- `--save-image` - Зберігає мапу тривог як зображення в директорію .\saves

### Приклади

Зміна частоти оновлення даних в режимі монітора параметрами `-freq`, `--frequency`:
```shell
py alerts.py monitor -freq 4
```

Зміна даних для відображення параметрами `-f`, `--format`. Доступні параметри дивитися
на [сайті](https://devs.alerts.in.ua/#modelalert) (назва поля). Приклад використання:
```shell
py alerts.py monitor -f "started_at" "location_title" "location_oblast" "location_uid"
```

Збереження мапи тривог параметром `--save-image`, наступне зображення зберігається тільки при змінах:
```shell
py alerts.py --save-image
```

### Загальний вигляд

Режим монітору з частотою оновлення 4 рази на хвилину та індивідуальним форматом:
```shell
py alerts.py monitor -freq 4 -f "started_at" "location_title" "location_oblast" "location_uid"
```

![](assets/CLI%20client%20example.png)

Відображення мапи тривог - одна з особливостей даної бібліотеки:
```shell
py alerts.py --show-image
```

![](assets/Show%20image%20example.png)

# Telegram бот
**Перейдіть в директорію `"telegram bot"`**

Для запуску бота скористайтеся командою:
```shell
py main.py
```

Приклад мапи тривог в Telegram боті. Використовуйте команду `/alerts`:
![](assets/Telegram%20bot%20example.png)

# Сайт
**Перейдіть в директорію `"site"`**

Для запуску сайту використовуйте команду:
```shell
flask run --host=127.0.0.1 --port=25585
```

Вигляд сайту з мапою та списком тривог
![](/assets/Site%20example.png)

# Додатково

Приклад Telegram бота: https://t.me/alerts_in_ua_dot_py_bot

Приклад сайту: http://91.199.45.219:25585

Документація API: https://devs.alerts.in.ua/

Репозиторій бібліотеки: https://github.com/FOUREX/alerts_in_ua.py

PyPi бібліотеки: https://pypi.org/project/alerts-in-ua.py/

Telegram канал для обговорень: https://t.me/Alerts_in_ua_dot_py

![Кря](https://tenor.com/ru/view/pikachu-pokemon-tongue-out-wiggle-tongue-weird-face-gif-16364996.gif)