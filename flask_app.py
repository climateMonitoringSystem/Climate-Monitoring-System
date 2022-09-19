
# 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
from flask import (
    Flask, redirect,
    url_for, request, jsonify,
    render_template
)


app = Flask(__name__)

temperature, humidity, light = float(), float(), int()


@app.errorhandler(404)
def not_found(e):
    return '404 : Not Found'


@app.route('/', methods=['POST', 'GET'])
def home():
    global temperature, humidity, light
    return render_template("home.html",
                          temperature=round(temperature, 2),
                          humidity=round(humidity, 2),
                          light=light,
                          activeH="active",
                          activeT="")

@app.route('/team', methods=['POST', 'GET'])
def team():
    return render_template("team.html", activeH="",
                          activeT="active")

@app.route('/update', methods=['POST'])
def update():

    global temperature, humidity, light
    return jsonify({
        "temperature" : temperature,
        "humidity" : humidity,
        "light" :  light
    })

@app.route('/record', methods=['POST', 'GET'])
def record():
    response = {"status": 0}
    try:
        global temperature, humidity, light
        content = request.get_json()
        temperature = content.get("temperature")
        humidity = content.get("humidity")
        light = content.get("light")
        response["status"] = 1

    except Exception as e:
        response = {"status": -1}

    return response


if __name__ == '__name__':
    app.run(port=8000)
