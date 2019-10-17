from flask import jsonify, Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome_web_api():
	return ('API OK')
		
if __name__ == "__main__":
    app.run()