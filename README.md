# Трекер полезных привычек

## Предварительные требования
Убедитесь, что у вас установлено следующее:
- Redis (или другой брокер, поддерживаемый Celery)
- Postgres

## Установка
Этот проект использует Celery для обработки асинхронных задач и Celery Beat для периодических задач. Следуйте приведенным ниже инструкциям для настройки и запуска Celery и Celery Beat в вашем проекте Django.
1. **Клонируйте репозиторий**
```bash
git clone git@github.com:FairuzovR/Course_work_7_final.git
cd ваш_проект
```
2. **Создайте и активируйте виртуальное окружение**
```bash
python -m venv venv
source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
```
3. **Установите необходимые пакеты**
```bash
pip install -r requirements.txt
```
4. **Создайте файл .env и заполните в соответствии с .env.sample**
```bash
touch .env
```
5. **Запустите Celery worker**
```bash
celery -A config worker --loglevel=info
```
6. **Запустите Celery Beat (для периодических задач)**
```bash
celery -A beat worker --loglevel=info
```
7. **Не забудьте также запустить сервер разработки Django**
```bash
python manage.py runserver
```

## Создание пользователей
```bash
python manage.py create_user user@example.com password123 --phone "+1234567890" --city "Moscow" --avatar "some_avatar.jpg" --tg_chat_id "123456789"
```
### Аргументы команды
* `email`: Электронная почта пользователя (обязательный аргумент).
* `password`: Пароль пользователя (обязательный аргумент).
* `--phone`: Телефон пользователя (необязательный аргумент).
* `--city`: Город пользователя (необязательный аргумент).
* `--avatar`: Путь к изображению аватара пользователя (необязательный аргумент).
* `--tg_chat_id`: ID чата в Телеграм пользователя (необязательный аргумент).

## Запуск тестов

### Перейти в корневую директорию и запустить тесты
```bash
pytest
```

### Проверка покрытия
Запуск тестов
```bash
coverage run --source='.' manage.py test
```
Вывод отчета
```bash
coverage report
```
## Запуск Docker Compose
``````bash
docker-compose up -d --build
