#(1)Celery のインポート
from celery import Celery

#(2)Celery オブジェクトの初期化
celery = Celery('mytasks',
	broker='amqp://localhost//'
)

#(3)celery の追加の設定
celery.conf.update(
    CELERY_RESULT_BACKEND = "amqp://localhost//",
)


#(4)タスクの実装
@celery.task
def add(x, y):
    return x + y

