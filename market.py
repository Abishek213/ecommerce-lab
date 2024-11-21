from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World from Flask to Bihan'

@app.route('/about/<username>')
def about_page(username):
    return f'<h1> This is the about page of {username}</h1>'

# @app.route('/')
# def home_page():
#     return render_template('home.html')

# @app.route('/home1')
# @app.route('/')
# def home_page_1():
#     return render_template('home_1.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) # debug=True for reload