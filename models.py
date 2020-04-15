from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Notes(db.Model):
    __tablename__='notes'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    todos = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "todos": self.todos
        }