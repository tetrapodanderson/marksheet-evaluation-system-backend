from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

@app.route("/test")
def test():
    return "flask server test!"

if __name__ == '__main__':
    app.run()