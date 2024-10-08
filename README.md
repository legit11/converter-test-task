** Сервис конвертации валют **


* Свою функциональность сервис осуществляет с помощью интеграции API ```https://fixer.io/```


*Запускаем проект с Docker, но можно и вручную локально:*


1. Создать файл [".env"]
2. Поинтересоваться о содержимом для данного файла(Пункт PS)
3. По необходимости запустить локально:
4. Создать виртуальное окружение poetry(```poetry shell```)
5. Установить зависимости(```poetry install```)
6. Запустить проект через main или с помощью команды(```uvicorn src.main:app --reload```)
8. Выполнить ```docker-compose up -d --build```

**В проекте присутствует БД PostgreSQL, хотя в теории она тут не нужна**


но я добавил на будущее, вдруг проект будет расширяться и понадобится хранить какие либо данные, возможно кешировать самые частые запросы **


* В проекте настроено логирование с помощью библиотеки loguru(https://github.com/Delgan/loguru) *



*Пункт PS:*


Содержимое файла .env:


DB_HOST=db


DB_PORT=5432


POSTGRES_DB=postgres


POSTGRES_USER=postgres


POSTGRES_PASSWORD=postgres


SQL_REQUESTS_SHOW_IN_CONCOLE=False


Это самые важные параметры:


API_KEY=de523d9f14-1174d2fbde-sl1x78


EXTERNAL_API_URL=https://api.fastforex.io/convert

  

