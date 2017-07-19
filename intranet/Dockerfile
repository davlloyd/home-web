FROM python:3.6.1
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip3 install -r requirements.txt
 RUN pip3 install -e git+git://github.com/theatlantic/django-mysqlndb-backend.git@v1.1.0#egg=django-mysqlndb-backend
 ADD . /code/