from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'random_string'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'admin':
            error = 'Invalid username or password. please try again!'
        else:
            flash('You are successfully logged in')
            flash('Logout before login again')
            return redirect(url_for('index'))
    return render_template('log_in.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)