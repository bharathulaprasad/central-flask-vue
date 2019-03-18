import json
import os
import uuid
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///central.local.db')
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', 'static/local/uploads')

db = SQLAlchemy(app)


class Application(db.Model):
    pk = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(250))
    logo = db.Column(db.String(250))
    url = db.Column(db.String(250))

    def serialize(self):
        return {
            'pk': self.pk,
            'name': self.name,
            'logo': self.logo,
            'url': self.url
        }


db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/v1/applications/')
def applications():
    query_result = Application.query.all()
    data = [i.serialize() for i in query_result]
    return jsonify(data)


@app.route('/api/v1/create/', methods=['POST'])
def create():
    request_data = request.data
    data = json.loads(request_data)
    name = data['name']
    logo = data['logo']
    url = data['url']
    application = Application(name=name, logo=logo, url=url)
    db.session.add(application)
    db.session.commit()

    return jsonify(True)


@app.route('/api/v1/upload/', methods=['POST'])
def upload():
    file = request.files['logo']
    filename = secure_filename(file.filename)
    file_ext = filename.split('.')[1]
    random_name = uuid.uuid4()
    generated_name = str(random_name) + '.' + file_ext
    logo_path = os.path.join(app.config['UPLOAD_FOLDER'], generated_name)
    file.save(logo_path)

    logo_url = '/' + logo_path
    return logo_url


if __name__ == '__main__':
    app.run(host='0.0.0.0')
