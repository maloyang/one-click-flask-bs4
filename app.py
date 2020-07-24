from flask import Flask, request, abort, render_template
from flask import json, jsonify

#app = Flask(__name__)
app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def airbox():
    return app.send_static_file('index.html')


@app.route('/aqi-history-get', methods=['GET', 'POST'])
def aqi_rt_get():
    aqi = {}
    aqi['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())  
    aqi['location'] = '高雄'
    aqi['data'] = []
    value = 10
    for i in range(10):
        value = random.randint(0, 20)
        aqi['data'].append(value)
    return jsonify(aqi)


if __name__ == "__main__":
    app.run(debug=True, port=80)
