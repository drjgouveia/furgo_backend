FROM python:3.9

COPY . .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# running migrations
RUN python manage.py migrate
RUN pip3 install django gunicorn
RUN python manage.py makemigrations
RUN python manage.py makemigrations home
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input
RUN python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'diogo2002')"

ENV VIRTUAL_HOST="furgo.drjgouveia.dev"
EXPOSE 1234
CMD ["gunicorn", "--bind", "0.0.0.0:1234", "core.wsgi"]

