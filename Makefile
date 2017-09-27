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
