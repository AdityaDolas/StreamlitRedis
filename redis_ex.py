import redis
import json, streamlit

redis_client = redis.Redis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

username = redis_client.get('username')

print(username)
streamlit.write(username.upper())

redis_client.set('name', json.dumps({"age": 23}))