from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

# Postgres config
pg_host = os.getenv("POSTGRES_HOST", "db")
pg_user = os.getenv("POSTGRES_USER", "user")
pg_pass = os.getenv("POSTGRES_PASSWORD", "password")
pg_db   = os.getenv("POSTGRES_DB", "appdb")

# Redis config
redis_host = os.getenv("REDIS_HOST", "redis")
cache = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    return "Hello from Flask in Docker!"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            host=pg_host, user=pg_user, password=pg_pass, dbname=pg_db
        )
        cur = conn.cursor()
        cur.execute("SELECT content FROM messages;")
        rows = cur.fetchall()
        return {"messages": [r[0] for r in rows]}
    except Exception as e:
        return {"error": str(e)}

@app.route("/cache")
def cache_check():
    try:
        count = cache.incr("hits")
        return {"redis_hits": int(count)}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
