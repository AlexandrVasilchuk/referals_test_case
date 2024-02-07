# referals_test_case
Тестовое задание для компании Stakewolle. Выполнено в соответсвии с тз https://clck.ru/38aZqg

---

## Коротко о функционале:

- Созданы пользователи с аутентификацией по JWT токену.
- Создана реферальная система со следующими особенносстями:
- - Пользователь может создать только 1 активный реферальный код
- - Пользователь может удалить реферальный код
- - Можно получить реферальный код пользователя по email
- - Можно просмотреть список приглашенных пользователей в проект, 
которые указали реферальный код при регистрации

---

### Технологии

- FastApi
- FastApiUsers
- SQLAlchemy

## Начало Работы

Чтобы запустить локальную копию проекта, следуйте инструкциям ниже.

### Зависимости

- Python 3.9+

### Установка

1. **Клонируйте репозиторий**

   ```shell
   git clone git@github.com:AlexandrVasilchuk/referals_test_case.git
   ```

### Локальный Запуск (Development)

1. **Установите зависимости проекта**

    ```shell
    pip install -r requirements.txt
    ``` 
2. **В корне проекта создай `.env` файл по аналогии с файлом .env.example**

    ```dotenv
    SECRET="<секретный ключ>"
    ```

   *Секретный ключ можно сгенерировать [тут](https://djecrety.ir/)*

3. **Запустите базу данных**

    ```shell
    alembic upgrade head
    ```
4. **Запустите локальный сервер**

    ```shell
    uvicorn app.main:app
    ```

   После запуска, проект будет доступен по [адресу](http://localhost:8000/)

## Использование

Swagger UI доступен по [адресу](http://localhost:8000/docs).

Там вы найдете полную документацию к API, а также сможете сделать запрос на
сервер. 

А так же ReDoc документация лежит [тут](http://localhost:8000/redoc).

---

## Контакты

___

Автор:
[Васильчук Александр](https://github.com/AlexandrVasilchuk/)

#### Контакты:

![Gmail-badge](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)\
alexandrvsko@gmail.com\
![Telegram-badge](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)\
@vsko_dev