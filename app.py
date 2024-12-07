from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/explore')
def explore_site():
    return render_template('explore.html')


@app.route('/signin')
def sign_in():
    return render_template('signin.html')


@app.route('/join')
def join_membership():
    return render_template('join.html')




if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)