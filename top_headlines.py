import requests
from flask import Flask, render_template
import secrets

# Constant variables-------------------------------------------------------------------------
client_key = secrets.NYT_API_KEY
BASE_URL = "https://api.nytimes.com/svc/topstories/v2/technology.json"

app = Flask(__name__)

## Main page
@app.route('/')
def index():
    return '<h1>Welcome!</h1>'

## Name page
@app.route('/name/<name>')
def about(name):
    return render_template('name.html', name=name.capitalize())

## Headlines page
@app.route('/headlines/<name>')
def visit_headlines(name):
    hdlist = get_headlines_list()
    return render_template('headlines.html', name=name.capitalize(), headlines_list=hdlist)

## EC 1: Headlines with link url page
@app.route('/links/<name>')
def visit_links(name):
    hdlist = get_headlines_list()
    return render_template('links.html', name=name.capitalize(), headlines_list=hdlist)

## EC 2: Headlines with link url page and thumbnail image
@app.route('/images/<name>')
def visit_images(name):
    hdlist = get_headlines_list()
    return render_template('images.html', name=name.capitalize(), headlines_list=hdlist)

# Build functions -------------------------------------------------------------------------
def get_headlines_list():
    '''
    Make request with API key and return headlines of
    top 5 technology news
    Parameters
    ---------------
    None

    Return
    ---------------
    List
    List of 5 dictionaries containing headlines and associated information

    '''
    baseurl = BASE_URL
    params = {"api-key": client_key}
    response = requests.get(baseurl, params=params).json()
    result = response['results'][0:5]

    hdlist = []
    for row in result:
        hdl = {}
        hdl['title'] = row['title']
        hdl['url'] = row['url']
        hdl['img'] = row['multimedia'][0]['url']
        hdlist.append(hdl)
    return hdlist


if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)