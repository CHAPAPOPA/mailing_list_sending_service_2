# :page_with_curl: Сервис рассылки писем №2 (apscheduler)

## Описание

Данный сервис предназначен для упрощения процесса создания и управления email рассылками. Он предоставляет пользователям возможность создавать рассылки, управлять и отслеживать их эффективность.

## Основные функции

- Создание и управление клиентской базой
- Создание и редактирование email сообщений
- Планирование и отправка рассылок по заданному расписанию
- Отслеживание статистики отправки и открытия писем
- Управление доступом и правами пользователей

## Установка и запуск

### Склонируйте репозиторий:

```bash
git clone https://github.com/CHAPAPOPA/mailing_list_sending_service_2.git
```

### Перейдите в папку с проектом

```bash
cd mailing_list_sending_service_2
```

### Установите зависимости:

Сначала активируем poetry
```bash
poetry shell
```

Затем установим все зависимости из pyproject.toml
```bash
poetry install
```

Для определения необходимых переменных окружения воспользуйтесь шаблоном
```bash
.env.sample
```

Сделайте миграции
```bash
python manage.py makemigrations
python manage.py migrate
```

Создайте суперпользователя
```bash
python manage.py create_su
```

Загрузите фикстуры 
```bash
python manage.py loaddata fixture/groups.json
```

## Запуск программы

### Сервер сайта
Для запуска сервера сайта выполните команду:
```bash
python manage.py runserver
```

### Сервис автоматической рассылки
Для запуска сервиса автоматической рассылки выполните команду:
```bash
python manage.py runapscheduler
```


## Как пользоваться сервисом

- **Регистрация**: Зарегистрируйтесь на сайте, чтобы получить доступ к сервису.
- **Верификация**: Что бы начать пользоваться сервисом, необходимо верифицировать свой email.
- **Вход в личный кабинет**: Войдите в систему, используя свои учетные данные.
- **Создание клиентской базы**: Добавьте клиентов, которым вы собираетесь отправлять рассылки.
- **Создание сообщений**: Создайте сообщения для рассылок с помощью встроенного редактора.
- **Создание рассылок**: Настройте параметры рассылок, включая периодичность, дату начала и окончания.
- **Отслеживание статистики**: Мониторьте эффективность ваших рассылок с помощью статистических отчетов.
- **Контроль рассылок**: Вы можете останавливать и запускать рассылки в ручном режиме.

## Технологии и инструменты

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **База данных**: PostgreSQL
- **Управление зависимостями**: Poetry

---

Этот README файл предоставляет основную информацию о проекте, его установке и использовании.

## Контакты

- [GitHub](https://github.com/CHAPAPOPA)
- [Telegram](https://t.me/CHAPAPOPA)
- [Email](mailto:yackow.muliawin2015@yandex.ru)
