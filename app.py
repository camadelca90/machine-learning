import flask


app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/case1')
def case1():
    return flask.render_template('case1.html')

@app.route('/case2')
def case2():
    return flask.render_template('case2.html')

@app.route('/case3')
def case3():
    return flask.render_template('case3.html')

@app.route('/case4')
def case4():
    return flask.render_template('case4.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)