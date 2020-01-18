from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def render_form():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def login():
    if request.form['username'] and request.form['email']:
        return render_template('check.html', email=request.form['email'], username=request.form['username'])
    else:
        return render_template('error.html')

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
