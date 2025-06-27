from flask import Flask, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(host = 'localhost', port = 6379)

@app.route('/')
def hello():
    count = r.incr('counter')
    return jsonify(message=f'This page hase been hit {count} times', count=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
    r.set('counter', 0)  # Initialize the counter
    print("Counter initialized to 0")