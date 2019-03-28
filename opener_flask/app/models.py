from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    phone = db.Column(db.String(15))
    position = db.Column(db.String(100))
    manager_level = db.Column(db.String(100))
    password_hash = db.Column(db.String(128))
    testplans = db.relationship('TestPlans', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User: {}, {}>'.format(self.id, self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        print(self.password_hash)
        return check_password_hash(self.password_hash, password)

class TestPlans(db.Model):
    test_id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(100))
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_submitted = db.Column(db.DateTime)
    days_since_last_activity = db.Column(db.Integer)
    past_submission_attempts = db.Column(db.Integer)
    status = db.Column(db.String(100), index=True)
    risk = db.Column(db.String(50), index=True)
    supplemental_documents = db.relationship('SupplementalDocuments',
                                              backref='test_plan',
                                              lazy='dynamic')

    def __repr__(self):
        return '<Test Plan: {}, {}>'.format(self.test_id, self.title)


class SupplementalDocuments(db.Model):
    doc_id = db.Column(db.Integer, primary_key=True, nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey('test_plans.test_id'), nullable=False)
    title = db.Column(db.String(100))
    uri = db.Column(db.String(150))

    def __repr__(self):
        return '<Supplemental Document: {}, {}>'.format(self.doc_id, self.title)
