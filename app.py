from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
        return jsonify({"message": "Hello from AWS Lambda with Zappa!"})

    # Necesario para Zappa
    if __name__ == "__main__":
            app.run()
            
