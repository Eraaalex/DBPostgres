
### Flask
В корневой папке проекта через терминал(командную строку) нужно прописать команды:
```
pip install flask
pip install psycopg2-binary
pip install flask-sqlalchemy
pip install Flask-Migrate
```

### PostgreSQL
* [install PostgreSQl](https://www.postgresql.org/download/)
* [install pgAdmin](https://www.pgadmin.org/download/pgadmin-4-windows/) - эта штука нужна, чтобы смотреть, что бд есть и запускать ее (с последним не факт). Есть альтернативы не такие навороченные, но я разобралась только в этой штуке.

### Чтобы все работало:

Нужно создать локально бд, возможно, этого можно избежать, но на момент написания я потяния не имею как, и у меня просто выдает ошибку


1. Заходим в pgAdmin, придумываем ваш личный пароль.

2. Заметим, что в app.py есть строка
```app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:eralex@localhost:5432/postgres_db"```.
Она описывает название,пароль и порт, которые установлены на моей бд, можете сделать точно также либо менять тогда эту строку. (Данные на этапе создания: user name: postgres, pswrd: eralex, data base name: postgres_db)
3. Создаем бд через pgAdmin

Потом, когда у вас уже все файлы в локальной папке есть, так же в корне прописываете:
```
flask db init
flask db migrate
flask db upgrade
```

Дальше запускаете ```app.py```. Должно работать. Переходите по ссылке которая будет прописана в терминале
[http://127.0.0.1:5000](http://127.0.0.1:5000), не обращайте внимание на WARNING, вот если ссылка не прописана, то это проблема, остальное ок.

### Возвращаемся к pgAdmin.

В верхнем углу ищем кнопочку с подписью Query Tool. Вводим правее:
```commandline
SELECT * from user
```
Пример команды показывающий табличку для User. Вероятно она будет изначально пуста
