from flask import Flask, request, render_template, jsonify
from scraping import scrap_app
import re
import requests
app = Flask(__name__)

regex_aptoide_url = re.compile(r'^(http(s)?:\/\/)[\w\-\.]+\.en\.aptoide\.com\/?')

@app.route('/', methods=['GET'])
def index():
    return render_template('welcome.html')


@app.route('/', methods=['POST'])
def data():
    link = request.form['aptoide_search']
    request.user_agent.string = "Mohamed LEGHERABA bot, only scrapping app data"
    if regex_aptoide_url.match(link):
        page_response = requests.get(link, timeout=5)
        if page_response.status_code == 200:

            n,v,nb,r,d = scrap_app(page_response)
            return render_template('results.html',name=n,version=v,nbdownloads=nb,date=r,description=d)
        else:
            return "Error " + str(page_response.status_code)
    else:
        return "Error : not a valid aptoide (english) url"

@app.route('/api/<path:link>', methods=['GET'])
def api(link):
    request.user_agent.string = "Mohamed LEGHERABA bot, only scrapping app data"
    if regex_aptoide_url.match(link):
        page_response = requests.get(link, timeout=5)
        if page_response.status_code == 200:

          n,v,nb,r,d = scrap_app(page_response)
          return jsonify(name=n,
              version=v,
              nbdownloads=nb,
              date=r,
              description=d
          )
        else:
            return "Error " + str(page_response.status_code)
    else:
        return "Error : not a valid aptoide url"

