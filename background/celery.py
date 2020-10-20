from celery import Celery

app = Celery('background', broker='redis://localhost', include=['background.tasks'])
app.conf.timezone = 'Asia/Shanghai'


if __name__ == '__main__':
    app.start()