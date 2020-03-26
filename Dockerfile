FROM python:3

RUN mkdir /app
WORKDIR /app
RUN mkdir /app/src
RUN pip install django
COPY /src/requirements.txt /app/src
WORKDIR /app/src
RUN pip install -r requirements.txt
EXPOSE 8000
ENV PYTHONUNBUFFERED=1