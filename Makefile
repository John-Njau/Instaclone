serve:
	python manage.py runserver 9000

migrations:
	python manage.py makemigrations
	python manage.py migrate

super:
	python manage.py createsuperuser

shell:
	Python manage.py shell