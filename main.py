import logging
from config import create_api
from datetime import datetime, timedelta
import time
from twitter import check_mentions

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

last_id = 0
# start_time = (datetime.utcnow() - timedelta(minutes=30)).strftime('%Y-%m-%dT%H:%M:%SZ')
start_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
tw_client = create_api()

while True:
    try:
        last_id = check_mentions(tw_client, last_id, start_time)
        time.sleep(2)
    except Exception as e:
        print(e)
