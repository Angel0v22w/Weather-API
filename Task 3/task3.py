from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')

def index():
    name = 'Rosalia'
    return render_template('index.html', title='Welcome', username=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)