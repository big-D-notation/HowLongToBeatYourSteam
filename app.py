from flask import (
    Flask,
    render_template,
)

from core.games_info_getter import GamesInfoGetter


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/results/<id>')
def results(id):
    game_info = GamesInfoGetter.get_games_info(id)
    return render_template('results.html', results=game_info)

if __name__ == '__main__':
    app.run(debug=True)

