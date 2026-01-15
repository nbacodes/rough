from flask import Flask
import redis
import os

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

@app.route("/")
def hello():
    count = r.incr("hits")
    return f"Hello from Flask + Redis! Hits = {count}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


