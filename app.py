from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask App on Azure!"

@app.route('/search')
def search():
    q = request.args.get("q")
    return f"Search results for: {q}"

if __name__ == "__main__":
    app.run()
