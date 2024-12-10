from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    logged_in = request.args.get('logged_in') == 'true'
    return render_template('home.html', logged_in=logged_in)

@app.route('/explore')
def explore_site():
    return render_template('explore.html')


@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        return redirect(url_for('home', logged_in='true'))
    return render_template('signin.html')


@app.route('/join', methods=['GET', 'POST'])
def join_membership():
    if request.method == 'POST':
        return redirect(url_for('home', logged_in='true'))
    return render_template('join.html')

@app.route('/profile', methods=['GET','POST'])
def user_profile():
    logged_in = request.args.get('logged_in') == 'true'
    user_response = None
    if request.method == 'POST':
        user_response = request.form.get('user') # Fetch the value of the selected radio button

    context = {
        'username': 'Ceina',
        'user': user_response,
        'logged_in': logged_in
    }

    return render_template('profile.html', **context)


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)