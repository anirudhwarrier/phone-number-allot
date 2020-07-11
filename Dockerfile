FROM python:3.6

# Create app directory
WORKDIR /app

# Install app dependencies

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

RUN pip install gunicorn gevent

# Bundle app source
COPY ./app /app/app
COPY ./manage.py ./

EXPOSE 5000

CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 manage:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info