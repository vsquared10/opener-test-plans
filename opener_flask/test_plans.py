from app import app, db
from app.models import Users, TestPlans, SupplementalDocuments

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Users': Users, 'TestPlans': TestPlans,
            'SupplementalDocuments': SupplementalDocuments}

test_user = Users.query.get(1)
test_user.set_password('password')
db.session.commit()
