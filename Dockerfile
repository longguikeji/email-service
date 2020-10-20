FROM python:3.8
ENV PORT 80
EXPOSE 80
WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y --no-install-recommends

COPY requirements.txt ./

RUN pip install --trusted-host mirrors.aliyun.com -r requirements.txt

COPY . .

COPY uwsgi.ini /etc/uwsgi/uwsgi.ini
CMD supervisord
