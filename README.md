# BraniacLMS

Современная платформа для обучения. Прогрессивный взгляд на простые вещи.

Учебный проект системы управления обучением, который разработан при 
прохождении обучения на факультете "Python-разработка", портал GeekBrains, курс `Основы Django`.

## Стек

- Python > 3.7
  - isort, black, autoflake
  - Django < 3.3
  - Celery[Redis]
- PyCharm
- VSCode
- SQLite 3


---
```commandline
docker run --name my-redis-container -p 7001:6379 -d redis
```

Запускать Celery параллельно с отладочным сервером Django!
```commandline
celery -A config worker -l INFO
```

## Лицензия

MIT

