from flask import Flask, render_template, request

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

@app.route('/profile', methods=['GET','POST'])
def user_profile():
    user_response = None
    if request.method == 'POST':
        user_response = request.form.get('user') # Fetch the value of the selected radio button

    context = {
        'username': 'Ceina Ellison',
        'user': user_response
    }

    return render_template('profile.html', **context)


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)