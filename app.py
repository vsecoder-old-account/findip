from flask import Flask, render_template, request
import os, requests, json
from flask import request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'codebinpy'


#index
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#ip
@app.route("/ip.js", methods=['GET', 'POST'])
def ipjs():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print("IP: " + str(ip))
    return render_template('index.js', ip=ip)

@app.route("/ip", methods=['GET', 'POST'])
def ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print("IP: " + str(ip))
    return render_template('ip.html', ip=ip)

@app.route("/ip.json", methods=['GET', 'POST'])
def ipjson():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print("IP: " + str(ip))
    return render_template('ip.json', ip=ip)

@app.route("/ip.jsonp", methods=['GET', 'POST'])
def ipjsonp():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print("IP: " + str(ip))
    return render_template('ip.jsonp', ip=ip)
    
@app.route("/getip.jsonp", methods=['GET', 'POST'])
def getip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print("IP: " + str(ip))
    return render_template('getip.jsonp', ip=ip)
    
    
@app.route("/geo.js", methods=['GET', 'POST'])
def geo():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    response = requests.post('https://geoipt.herokuapp.com/' + ip)
    geojson = json.loads(response.text)
    city = geojson['city']
    country = geojson['country']
    return render_template('geo.js', ip=ip, city=city, country=country)
    
@app.route("/geo", methods=['GET', 'POST'])
def geo1():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    response = requests.post('https://geoipt.herokuapp.com/' + ip)
    geojson = json.loads(response.text)
    city = geojson['city']
    country = geojson['country']
    return render_template('geo.json', geo=geojson)
        
    
#404
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

#RUN
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
