from flask import Flask
import redis
import os
import time

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = 6379

# Retry mekanizması (Redis hazır olana kadar bekle)
for i in range(10):  # 10 deneme yap
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        r.ping()
        print("Redis bağlantısı başarılı.")
        break
    except redis.exceptions.ConnectionError as e:
        print(f"Redis bağlantısı kurulamadı, tekrar deneniyor... ({i+1}/10)")
        time.sleep(3)  # Her denemede 3 saniye bekle
else:
    raise Exception("Redis'e bağlanılamadı.")


@app.route("/")
def index():
    r.incr("ziyaret")
    return f"Ziyaret sayısı: {r.get('ziyaret').decode()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
