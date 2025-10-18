# Mosk PDK - Django project scaffold

Это минимальная заготовка проекта для системы учёта и контроля замечаний по вагонам.
Язык интерфейса: русский. Тема: светлая (Bootstrap).

## Что внутри
- Django проект `mosk_pdk`
- Приложение `pdk_system` с моделями: Depo, Train, Wagon, Remark
- Админка зарегистрирована.
- Начальные данные (fixture) с депо 1..6 и тестовыми пользователями описаны — вы можете создать админа командой `createsuperuser`.
- Файлы для деплоя на Render (Procfile, requirements.txt).

## Как запустить локально (быстро)
1. Создайте виртуальное окружение и установите зависимости:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Примените миграции и создайте суперпользователя:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
3. Запустите сервер:
   ```bash
   python manage.py runserver
   ```

## Развёртывание на Render.com (краткая инструкция)
1. Зарегистрируйтесь на https://render.com и создайте новый **Web Service**.
2. Подключите репозиторий (GitHub) или загрузите код через форк/репозиторий.
3. В настройках сервиса укажите команду сборки: (Render автоматически установит pip install -r requirements.txt)
4. Добавьте переменную окружения `DATABASE_URL` с вашим Postgres URL (Render предлагает создать базу в разделе Databases).
5. В разделе Environment укажите `PYTHONUNBUFFERED=1` если нужно.
6. Деплой завершится и сайт станет доступен по адресу `https://<your-service>.onrender.com`.

ПРИМЕЧАНИЕ: в этом скелете по умолчанию используется настройка, читающая `DATABASE_URL`. Для локального запуска без Postgres можно использовать SQLite (по умолчанию).

