import flask 
import secret
import requests

app = flask.Flask(__name__)

@app.route('/')
def index():     
    return '<h1>Welcome!</h1>'

@app.route('/name/<name>/')
def hello(name):
    return flask.render_template('name.html', name=name)

@app.route('/headlines/<name>/')
def headlines(name):
    title = []
    url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?'
    response = requests.get(url, {"api-key": secret.api_key}).json()
    for i in response["results"]:
        title.append(i["title"])
    return flask.render_template('headlines.html',name=name, title=title)   

@app.route('/links/<name>/')
def links(name):
    url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?'
    title = []
    link = []
    response = requests.get(url, {"api-key": secret.api_key}).json()
    for i in response["results"]:
        title.append(i["title"])
        link.append(i["url"])
    return flask.render_template('links.html',name=name, title=title, link=link)   
if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)
