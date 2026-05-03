import time
from celery_app import celery_app


@celery_app.task(bind=True,max_retries=2,delay=3)
async def process_order(self, order_id: str,items: list):
    try:
        list1 = []
        seen=set()
        skip_items = []
        order_id = 1
        for item in items:
            item_id = item['item_id']
            if item['item_id'] not in list1:
                list1.append((order_id,item['item_id']))
                seen.add(item_id)
                order_id += 1
            else:
                skip_items.append(item['item_id'])
        return {
            'order_id': order_id,
            'process_items': len(list1),
            'skipped_items': len(skip_items)
        }
    except Exception as e:
        raise self.retry(exe=e,countdown=3)