cooking:
	docker-compose exec django python3 manage.py migrate
	docker-compose exec django python3 manage.py collectstatic --noinput

createsuperuser:
	docker-compose exec django python3 manage.py createsuperuser

djangoshell:
	docker-compose exec django python3 manage.py shell_plus

cleardefender:
	docker-compose exec django python3 manage.py cleanup_django_defender

run:
	docker-compose up

build:
	docker-compose build

stop:
	docker-compose stop

backup:
	docker-compose exec db pg_dump -U user -a -Fc -f /fixtures/organiser.backup database

restore: recreate_db migrate_db restore_db

recreate_db:
	docker-compose stop django
	docker-compose exec db dropdb -U user database
	docker-compose exec db createdb -U user database
	docker-compose start django

migrate_db:
	docker-compose exec django python3 manage.py makemigrations
	docker-compose exec django python3 manage.py migrate

restore_db:
	docker-compose exec db pg_restore -U user -a -d database /fixtures/organiser.backup

restart:
	docker-compose stop && docker-compose up 
