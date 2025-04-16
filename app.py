from flask import Flask
import redis

import os
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=REDIS_HOST, port=6379)

app = Flask(__name__)
# r = redis.Redis(host="redis", port=6379)

@app.route("/")
def index():
    r.incr("ziyaret")
    return f"Ziyaret sayısı: {r.get('ziyaret').decode()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
