from flask import Flask, render_template
from bokeh.embed import server_document

app = Flask(__name__)


@app.route('/')
def index():
    script = server_document('http://localhost:5006/bfx_ltc')
    return render_template('index.html', script=script, template='Flask')


@app.route('/extended')
def extended():
    script = server_document('http://localhost:5006/bfx_ltc_extended')
    return render_template('extended.html', script=script, template='Flask')


@app.route('/performance')
def performance():
    script = server_document('http://localhost:5006/bfx_ltc_performance')
    return render_template('extended.html', script=script, template='Flask')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
