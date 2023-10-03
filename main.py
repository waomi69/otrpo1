from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    count = str(requests.get('https://pokeapi.co/api/v2/pokemon/').json()['count'])
    url = 'https://pokeapi.co/api/v2/pokemon?limit='+str(count)
    response = requests.get(url)
    data = response.json()
    return render_template('index.html', pokemons=data['results'])


@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search = request.form['search']
        url = f'https://pokeapi.co/api/v2/pokemon/{search.lower()}'
        response = requests.get(url)
        if response.status_code == 200:
            data = [response.json()]
        else:
            data = []
    else:
        data = []
    return render_template('index.html', pokemons=data)


if __name__ == '__main__':
    app.run(debug=True)
