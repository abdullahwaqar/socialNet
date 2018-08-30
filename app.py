from flask import Flask, render_template, request
from models import create_post, get_posts
from flask_cors import CORS

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)
    posts = get_posts()
    print(posts)
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)