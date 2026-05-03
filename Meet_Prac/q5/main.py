from celery_app import celery_app
from tasks import process_order

items = [
    {'item_id':1,'price':100},
    {'item_id':2,'price':200},
    {'item_id':3,'price':300},
    {'item_id':3,'price':200}
]

res = process_order.delay(1,items)
print(res.id)
print(res.get(timeout=10))