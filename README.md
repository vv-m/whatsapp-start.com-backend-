# whatsapp-start.com (backend)

## Описание проекта

Проект позволяет отправлять сообщения на WhatsApp не добавляя 
телефон получателя в контакты. 

Для зарегистрированных пользователей предусмотрены шаблоны сообщений.

## Запуск проекта 🚀

_Создаем виртуальное окружение_
```bash
python3 -m venv venv
```

_Активируем виртуальное окружение_
```bash
source venv/bin/activate
```

_Устанавливаем зависимости_
```bash
pip install -r requirements.txt
```


_Создаем миграции_
```bash
python manage.py makemigrations
```

_Применяем миграции_
```bash
python manage.py migrate
```


_Запускаем **Django**_ сервер

```bash
python manage.py runserver
```

Далее клонируем [проект с frontend`ом](https://github.com/vv-m/whatsapp_start_FRONT) и следуем инструкции приложенной нему.



## Используемые технологии

- [Django REST framework](https://www.django-rest-framework.org/#)
- Аутентификация с помощью JWT токенов, используя
  библиотеки [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html#available-endpoints)
  и [Simple
  JWT](https://djoser.readthedocs.io/en/latest/getting_started.html#installation))

## Автор

- [@Vlad Mironov](https://t.me/LR_STUDIO)