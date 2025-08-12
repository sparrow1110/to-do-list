# ToDo List Application

Веб-приложение для управления задачами с аутентификацией пользователей.

## Особенности

- 📝 Создание, редактирование и удаление задач через REST API
- ✅ Три статуса задач: "Не начато", "В процессе", "Завершено"
- 🔐 Аутентификация пользователей (регистрация, вход, выход)
- 🎨 Приятный интерфейс на Semantic UI
- 🔒 Защита от CSRF-атак
- 📱 Адаптивный дизайн
- 🛡️ Защищенные API-эндпоинты (только для аутентифицированных пользователей)

## 🛠 Технологический стек

- **Backend**: Python 3, Django 5, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: Django Session Auth
- **Frontend**: Semantic UI, CSS3, HTML, Javascript

## Установка

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/sparrow1110/to-do-list.git
    cd to-do-list
    ```

2. **Создайте виртуальное окружение и активируйте его:**

    ```bash
    python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
    ```

3. **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Создайте файл .env в корне проекта с настройками (пример в .env.example):**

    ```env
    SECRET_KEY=your-secret-key-here
    DB_NAME=to_do_db
    DB_USER=postgres
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=5432
    DEBUG=True
    ```

5. **Примените миграции:**

    ```bash
    cd todoproject
    python manage.py migrate
    ```

6. **Создайте суперпользователя (опционально):**

    ```bash
    python manage.py createsuperuser
    ```

7. **Запустите сервер разработки:**

    ```bash
    python manage.py runserver
    ```

    Приложение будет доступно по адресу `http://127.0.0.1:8000`.

## Использование

1. **Регистрация:**
    - Перейдите на страницу регистрации и заполните форму.
    - После успешной регистрации вы будете перенаправлены на страницу входа.

2. **Вход:**
    - Введите свои учетные данные для входа в систему.

3. **Управление задачами:**
    - На главной странице вы можете:
        - Добавлять новые задачи
        - Изменять их статус (Не начато → В процессе → Завершено)
        - Удалять задачи

## API Endpoints

Приложение предоставляет REST API для управления задачами:

- `GET /api/v1/tasks/` - получить список всех задач
- `POST /api/v1/tasks/` - создать новую задачу
- `PATCH /api/v1/tasks/<id>/` - изменить статус задачи
- `DELETE /api/v1/tasks/<id>/` - удалить задачу

Все API-эндпоинты требуют аутентификации.

## Структура проекта

- `todoproject/` - основная конфигурация проекта
  - `settings.py` - настройки Django
  - `urls.py` - главные URL-маршруты
- `todo/` - приложение задач
  - `models.py` - модель Task
  - `views.py` - представления
  - `urls.py` - URL-маршруты
  - `templates/` - HTML шаблоны
  - `static/` - статические файлы (CSS, изображения)
- `users/` - приложение для аутентификации
  - `forms.py` - формы входа и регистрации
  - `views.py` - представления аутентификации
  - `urls.py` - URL-маршруты (регистрация, вход, выход)
  - `templates/` - HTML шаблоны
- `api/` - REST API для задач
  - `views.py` - API представления
  - `serializers.py` - сериализаторы
  - `urls.py` - API эндпоинты
- `templates/` - глобальные шаблоны


