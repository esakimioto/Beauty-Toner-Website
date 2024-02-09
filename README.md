# DJango Framework to Docker Composer Template

# Outline
* 本プロジェクトはDocker Compose上にDJango Frameworkを設定するデフォルトテンプレートになります。

# Startup
~~~sh
$ docker compose down

$ docker compose up
or
$ docker compose up -d
~~~


~~~sh
$ docker compose exec web /bin/bash
# サーバを起動するコマンド
$ python manage.py runserver 0.0.0.0:8000

# DBを更新するコマンド
$ python manage.py migrate
# DBを更新ファイルを生成するコマンド
$ python manage.py makemigrations

~~~