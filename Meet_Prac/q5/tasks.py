from celery_app import celery_app

@celery_app.task(bind=True, max_retries=2)
def process_order(self, order_id: str, items: list):
    try:
        processed = []
        seen = set()
        skipped_items = []

        counter = 1

        for item in items:
            item_id = item['item_id']

            if item_id not in seen:
                processed.append((counter, item_id))
                seen.add(item_id)
                counter += 1
            else:
                skipped_items.append(item_id)

        return {
            'order_id': order_id,
            'processed_items': len(processed),
            'skipped_items': len(skipped_items)
        }

    except Exception as e:
        raise self.retry(exc=e, countdown=3)