FROM python:3.8

MAINTAINER Ilya Balashov "balashovia@bk.ru"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "-u", "currency_bot.py"]