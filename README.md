# Телеграм-бот для получения информации о погоде

Этот бот создан с использованием библиотеки aiogram для работы с Telegram API и aiohttp для асинхронных HTTP-запросов.

## Установка

1. Сначала склонируйте репозиторий:

    ```bash
    git clone git@github.com:AhmedZulkarnaev/Weather_bot.git
    cd ваш-репозиторий
    ```

2. Создайте виртуальное окружение и установите зависимости:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Linux/Mac
    pip install -r requirements.txt
    ```

3. Создайте файл `.env` и добавьте свои токены для Telegram и OpenWeatherMap:

    ```
    BOT_TOKEN=ваш-токен-бота-в-телеграм
    WEATHER_TOKEN=ваш-токен-погоды-в-openweathermap
    ```

## Использование

1. Запустите ваш бот:

    ```bash
    python bot.py
    ```

2. Откройте чат с вашим ботом в Telegram и введите команду `/start`.

3. Выберите город с клавиатуры и получите информацию о погоде в выбранном городе.

## Замечание

Убедитесь, что у вас есть актуальные токены для вашего бота в Telegram и API OpenWeatherMap.

