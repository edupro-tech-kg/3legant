# E-Commerce Web API

**Учебный проект (не коммерческий)** - Django REST Framework API для электронной коммерции с JWT аутентификацией.

Разработан для обучения фронтенд-разработчиков работе с REST API.

## 🚀 Деплой на Render (бесплатный хостинг)

Проект настроен для деплоя на [Render.com](https://render.com) - бесплатный хостинг для учебных проектов.

**API доступен по адресу:** `https://your-app-name.onrender.com`

## Особенности

- ✅ JWT аутентификация (SimpleJWT)
- ✅ Регистрация и авторизация пользователей
- ✅ Восстановление пароля
- ✅ Управление товарами, категориями и брендами
- ✅ Корзина покупок
- ✅ Избранное
- ✅ Отзывы на товары
- ✅ Заказы
- ✅ Поиск товаров
- ✅ Подписка на рассылку
- ✅ Статьи/блог

## Технологии

- Django 5.2
- Django REST Framework 3.16.1
- djangorestframework-simplejwt 5.3.1
- PostgreSQL (на Render) / SQLite (локально)
- WhiteNoise (для статических файлов)

## Быстрый старт

### Локальная разработка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd ecomm_web
```

2. Создайте виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# или
.venv\Scripts\activate  # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

6. Запустите сервер:
```bash
python manage.py runserver
```

## 📦 Деплой на Render

### Шаг 1: Подготовка репозитория

1. Закоммитьте и запушьте код в Git (GitHub, GitLab, Bitbucket)

2. Убедитесь, что в проекте есть:
   - ✅ `requirements.txt`
   - ✅ `runtime.txt`
   - ✅ `build.sh`
   - ✅ Все файлы в `.gitignore` (кроме необходимых)

### Шаг 2: Создание Web Service на Render

1. Зайдите на [render.com](https://render.com) и зарегистрируйтесь
2. Нажмите "New +" → "Web Service"
3. Подключите ваш Git репозиторий
4. Заполните настройки:

**Настройки:**
- **Name:** `ecomm-api` (или любое имя)
- **Environment:** `Python 3`
- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn config.wsgi:application`

### Шаг 3: Создание PostgreSQL Database

1. Нажмите "New +" → "PostgreSQL"
2. Выберите **Free** план
3. Скопируйте **Internal Database URL**

### Шаг 4: Настройка Environment Variables

В настройках Web Service добавьте переменные окружения:

```env
SECRET_KEY=<сгенерируйте случайный ключ>
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
DATABASE_URL=<Internal Database URL из PostgreSQL>
CSRF_TRUSTED_ORIGINS=https://your-app-name.onrender.com
```

**Генерация SECRET_KEY:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Шаг 5: Деплой

1. Нажмите "Create Web Service"
2. Render автоматически:
   - Установит зависимости
   - Запустит `build.sh`
   - Применит миграции
   - Запустит приложение

3. После успешного деплоя ваш API будет доступен по адресу:
   `https://your-app-name.onrender.com`

### Шаг 6: Создание суперпользователя

После деплоя создайте админа через Render Shell:

1. Откройте Web Service
2. Перейдите в "Shell"
3. Выполните:
```bash
python manage.py createsuperuser
```

## API Endpoints

### Базовый URL: `https://your-app-name.onrender.com`

### Аутентификация
- `POST /api/auth/register/` - Регистрация
- `POST /api/auth/login/` - Авторизация (получить JWT токены)
- `POST /api/auth/token/refresh/` - Обновить access токен
- `POST /api/auth/password-reset/` - Запрос на восстановление пароля
- `POST /api/auth/password-reset/confirm/` - Подтверждение сброса пароля

### Товары
- `GET /api/products/` - Список товаров
- `GET /api/products/<id>/` - Детали товара
- `GET /api/categories/` - Список категорий
- `GET /api/brands/` - Список брендов
- `GET /api/popular/products/` - Популярные товары
- `GET /api/new/products/` - Новые товары

### Поиск
- `GET /api/search/?q=query` - Поиск товаров
- `GET /api/suggest/?q=query` - Автодополнение

### Корзина (требует авторизации)
- `GET /api/cart/` - Получить корзину
- `POST /api/cart/add/` - Добавить в корзину
- `DELETE /api/cart/remove/<item_id>/` - Удалить из корзины

### Избранное (требует авторизации)
- `GET /api/favorites/` - Список избранного
- `POST /api/favorites/add/` - Добавить в избранное
- `DELETE /api/favorites/remove/<product_id>/` - Удалить из избранного

### Отзывы
- `GET /api/reviews/product/<product_id>/` - Отзывы на товар
- `POST /api/reviews/create/` - Создать отзыв (требует авторизации)
- `DELETE /api/reviews/delete/<review_id>/` - Удалить отзыв

### Заказы (требует авторизации)
- `GET /api/orders/` - Список заказов
- `POST /api/orders/` - Создать заказ
- `GET /api/orders/<id>/` - Детали заказа

### Рассылка
- `POST /api/newsletter/subscribe/` - Подписаться
- `POST /api/newsletter/unsubscribe/` - Отписаться

### Админ-панель
- `GET /admin/` - Админ-панель Django

## Пример использования API

### Регистрация
```bash
curl -X POST https://your-app-name.onrender.com/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "StrongPass123",
    "password2": "StrongPass123"
  }'
```

### Авторизация
```bash
curl -X POST https://your-app-name.onrender.com/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "StrongPass123"
  }'
```

### Получение токенов
Ответ:
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Использование токена
```bash
curl -X GET https://your-app-name.onrender.com/api/cart/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Структура проекта

```
ecomm_web/
├── accounts/          # Аутентификация и регистрация
├── products/          # Товары, категории, бренды
├── cart/              # Корзина покупок
├── orders/            # Заказы
├── favourites/        # Избранное
├── reviews/           # Отзывы
├── search/            # Поиск товаров
├── newsletter/        # Подписка на рассылку
├── articles/          # Статьи/блог
├── user_profile/      # Профиль пользователя
├── config/            # Настройки проекта
├── build.sh           # Скрипт для деплоя на Render
├── runtime.txt        # Версия Python
└── requirements.txt   # Зависимости
```

## Важные замечания для Render

- ⚠️ **Free план имеет ограничения:** сервис "засыпает" после 15 минут неактивности, первый запрос после пробуждения может занять 30-50 секунд
- ✅ Это нормально для учебных проектов
- 💡 Для production используйте платные планы

## Лицензия

Учебный проект. Свободное использование для обучения.

## Поддержка

Это учебный проект для фронтенд-разработчиков. Используйте API для обучения работе с REST API и JWT аутентификацией.
