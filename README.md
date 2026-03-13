# FastAPI Startup Template

Чистый шаблон для быстрого старта FastAPI проектов с async PostgreSQL.

---

## Стек

- **Python 3.13**
- **FastAPI** — веб-фреймворк
- **SQLAlchemy 2.0** — async ORM
- **Alembic** — миграции базы данных
- **asyncpg** — async драйвер PostgreSQL
- **Pydantic v2 + pydantic-settings** — конфигурация и валидация

---

## Структура проекта
```
├── app/
│   ├── config/
│   │   ├── envs/           # .env файлы (.env.example — пример, .env — в .gitignore)
│   │   ├── yaml/           # yaml конфиги
│   │   ├── app.py          # настройки приложения
│   │   ├── database.py     # настройки базы данных
│   │   ├── logging.py      # настройки логирования
│   │   ├── http.py         # настройки http
│   │   └── settings.py     # корневые настройки
│   ├── database/
│   │   ├── base.py         # декларативная база
│   │   ├── engine.py       # async engine и сессия
│   │   └── annotations.py  # переиспользуемые типы колонок
│   └── main.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── alembic/
├── run.py
└── pyproject.toml
```

---

## Конфигурация

Поддерживается три слоя конфигурации с приоритетом:
```
переменные окружения > .env файл > yaml файл
```

Все переменные окружения используют префикс `FST_APP__` и разделитель `__` для вложенности.

---

## Запуск

Если нет локальной БД — можно запустить PostgreSQL через Docker:
```bash
docker compose -f docker/docker-compose.yml up -d db
```

**Создать виртуальное окружение:**
```bash
python -m venv .venv
```
```bash
# Windows
.venv\Scripts\activate
```
```bash
# Linux / Mac
source .venv/bin/activate
```

**Установить зависимости:**
```bash
pip install poetry
```

```bash
poetry install
```

**Применить миграции: (проверка подключения)**
```bash
alembic upgrade head
```

**Запустить сервер:**
```bash
python run.py
```

---

## Создание миграции
```bash
alembic revision --autogenerate -m "create users table"
alembic upgrade head
```

Файлы миграций автоматически форматируются через **black** и организуются по папкам с датой.

---

## Docker

В папке `docker/` находится `Dockerfile` и `docker-compose.yml` для деплоя на сервер.