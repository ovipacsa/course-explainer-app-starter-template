from flask import Flask, render_template
from views import index, course, videos_page, contact

app = Flask(__name__)
app.secret_key = "dev-secret-key"

app.add_url_rule('/', endpoint='index', view_func=index)
app.add_url_rule('/course/<course_id>', endpoint='course', view_func=course)
app.add_url_rule('/videos', endpoint='videos', view_func=videos_page)
app.add_url_rule('/contact', endpoint='contact', view_func=contact, methods=["GET", "POST"])

if __name__ == '__main__':
    app.run(debug=True)