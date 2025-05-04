# ToDo List Application

Простое веб-приложение для управления задачами с аутентификацией пользователей.

## Особенности

- 📝 Создание, редактирование и удаление задач
- ✅ Отметка задач как выполненных/невыполненных
- 🔐 Аутентификация пользователей (регистрация, вход, выход)
- 🎨 Приятный интерфейс на Semantic UI
- 🔒 Защита от CSRF-атак
- 📱 Адаптивный дизайн

## 🛠 Технологический стек

- **Backend**: Python 3, Flask
- **Database**: PostgreSQL (через SQLAlchemy)
- **Authentication**: Flask-Login
- **Frontend**: Semantic UI, CSS3
- **Security**: Flask-WTF (CSRF защита)

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
    # Настройки БД
    POSTGRES_DB=your_db_name
    POSTGRES_USER=your_db_user
    POSTGRES_PASSWORD=your_db_password
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    SECRET_KEY=your_secret_key
    ```

5. **Запустите приложение:**

    ```bash
    python run.py
    ```

    Приложение будет доступно по адресу `http://127.0.0.1:5001`.

## Использование

1. **Регистрация:**
    - Перейдите на страницу регистрации и заполните форму.
    - После успешной регистрации вы будете перенаправлены на страницу входа.

2. **Вход:**
    - Введите свои учетные данные для входа в систему.

3. **Управление задачами:**
    - На главной странице вы можете добавлять новые задачи, отмечать их как выполненные или удалять.

## Структура проекта

- `todo/static/css/style.css`: Файл стилей для приложения.
- `todo/templates/todo/`: Шаблоны HTML для различных страниц приложения.
- `todo/__init__.py`: Инициализация приложения Flask и настройка базы данных.
- `todo/forms.py`: Формы для регистрации и входа.
- `todo/models.py`: Модели базы данных для пользователей и задач.
- `todo/routes.py`: Маршруты и логика приложения.
- `run.py`: Точка входа для запуска приложения.


