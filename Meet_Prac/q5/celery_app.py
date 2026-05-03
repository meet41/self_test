from celery import Celery

celery_app = Celery(
    'process_order',
    backend='redis://localhost:6379/0',
    broker='redis://localhost:6379/1'
)

celery_app.conf.update(
    task_serializer='json',
    result_serializer='json'
    accept_content=['json'],
    task_routes={
        'tasks.process_order':
         {'queue':'order_queue'}
    }
)
