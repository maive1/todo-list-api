import os
from flask import Flask, render_template, request, jsonify, json
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db, Notes

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/prueba'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'prueba.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)
CORS(app)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/api/todos/user/<username>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def todos(username=None):
    if request.method == 'GET':
        notes = Notes.query.filter_by(username=username).first()
        if username is not None:
            return jsonify(notes.serialize()), 200
        else:
            return jsonify({"msg": "username not exist "}), 404

    if request.method == 'POST':
        todos = request.get_json('todos')

        notes = Notes()
        notes.username = username
        notes.todos = json.dumps(todos)

        db.session.add(notes)
        db.session.commit()

        return jsonify(notes.serialize()), 201
        
    if request.method == 'PUT':
        todos = request.json.get('todos')

        Notes = Notes.query.get(id).first()
        notes.username = username
        notes.todos = json.dumps(todos)

        db.session.commit()

        return jsonify(notes.serialize()), 200

    if request.method == 'DELETE':
        notes = Notes.query.get(id)
        db.session.delete(notes)
        db.session.commit()
        
        return jsonify({"resultado": "Notas eliminada"}), 200


if __name__ == '__main__':
    manager.run()