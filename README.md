# Inteligence Type
Inteligence Type — Hamidbek Makhmatkulov tomonidan ishlab chiqilgan.

## Ishga tushirish
    python -m venv venv && source venv/bin/activate
    pip install -r requirements.txt
    python manage.py makemigrations core && python manage.py migrate
    python manage.py runserver
Sayt: http://127.0.0.1:8000

## Hostingga joylash
    export DEBUG=0 SECRET_KEY=<uzun-kalit> ALLOWED_HOSTS=domen.uz CSRF_ORIGINS=https://domen.uz
    python manage.py collectstatic --noinput && python manage.py migrate
    gunicorn config.wsgi
Ishlab chiqarishda PostgreSQL uchun config/settings.py dagi DATABASES ni almashtiring.
