FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . /code/
#Only Used for Celery Integration
#RUN adduser --disabled-password --gecos '' myuser
CMD ["sh", "/code/run.sh"]
