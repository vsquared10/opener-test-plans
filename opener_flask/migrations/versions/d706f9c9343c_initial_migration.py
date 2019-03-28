"""initial migration

Revision ID: d706f9c9343c
Revises:
Create Date: 2019-03-27 20:17:07.476076

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = 'd706f9c9343c'
down_revision = None
branch_labels = None
depends_on = None

seed = {
    "users": [
        {"id":1, "first_name": "Victor", "last_name": "Vulovic",
         "position": "Developer", "manager_level": "Contributor",
         "email": "victorvulovic@gmail.com"},
        {"id":2, "first_name": "Marcus", "last_name": "Leng",
         "position": "Founder & CEO", "manager_level": "CEO",
         "email": "mleng@opener.com"},
        {"id":3, "first_name": "Jessica", "last_name": "Alba",
         "position": "Flight Test Manager", "manager_level": "Upper",
         "email": "jsmith@opener.com"},
        {"id":4, "first_name": "Jerry", "last_name": "Seinfeld",
         "position": "Flight Test Manager", "manager_level": "Upper",
         "email": "jseinfeld@opener.com"},
        {"id":5, "first_name": "Steve", "last_name": "Kerr",
         "position": "Associate Flight Test Manager", "manager_level": "Lower",
         "email": "skerr@opener.com"},
        {"id":6, "first_name": "Grey", "last_name": "Flint",
         "position": "Associate Flight Test Manager", "manager_level": "Lower",
         "email": "gflint@opener.com"},
        {"id":7, "first_name": "Francis", "last_name": "Macklemore",
         "position": "Associate Flight Test Manager", "manager_level": "Lower",
         "email": "fmacklemore@opener.com"},
        {"id":8, "first_name": "Lucia", "last_name": "Gallardo",
         "position": "Lead Engineer", "manager_level": "Contributor",
         "email": "lgallardo@opener.com"}
    ],
    "test_plans": [
        {"test_id": 12, "title": "SF Bay Area Test Flight", "author": 7,
         "date_submitted": datetime.strptime("03/12/2019", "%m/%d/%Y"),
         "days_since_last_activity": "10", "past_submission_attempts": 0,
         "status": "Pending 1st Manager Approval", "risk": "severe"},
        {"test_id": 7474890889, "title": "Crash Safety Test", "author": 4,
         "date_submitted": datetime.strptime("03/20/2019", "%m/%d/%Y"),
         "days_since_last_activity": "2", "past_submission_attempts": 0,
         "status": "Pending CEO Approval", "risk": "severe"},
        {"test_id": 3847792993, "title": "Battery Duration Stress Test", "author": 4,
         "date_submitted": datetime.strptime("02/22/2019", "%m/%d/%Y"),
         "days_since_last_activity": "28", "past_submission_attempts": 0,
         "status": "Fully Approved - In Progress", "risk": "high"},
        {"test_id": 2080844423, "title": "Extreme Cold Flight", "author": 6,
         "date_submitted": datetime.strptime("01/21/2019", "%m/%d/%Y"),
         "days_since_last_activity": "60", "past_submission_attempts": 1,
         "status": "Upper Management Approved", "risk": "moderate"},
        {"test_id": 1234555098, "title": "Low-risk test 1", "author": 6,
         "date_submitted": datetime.strptime("01/21/2019", "%m/%d/%Y"),
         "days_since_last_activity": "60", "past_submission_attempts": 1,
         "status": "Pending Upper Management Approval", "risk": "low"},
        {"test_id": 1234999879, "title": "Low-risk test 2", "author": 6,
         "date_submitted": datetime.strptime("01/21/2019", "%m/%d/%Y"),
         "days_since_last_activity": "60", "past_submission_attempts": 1,
         "status": "Pending Upper Management Approval", "risk": "low"},
        {"test_id": 3849009388, "title": "High-risk, non-approved test 1", "author": 6,
         "date_submitted": datetime.strptime("01/21/2019", "%m/%d/%Y"),
         "days_since_last_activity": "60", "past_submission_attempts": 1,
         "status": "1st Manager Approved", "risk": "high"},
        {"test_id": 7478758999, "title": "Low-risk test 3", "author": 6,
         "date_submitted": datetime.strptime("01/21/2019", "%m/%d/%Y"),
         "days_since_last_activity": "60", "past_submission_attempts": 1,
         "status": "Pending Upper Management Approval", "risk": "low"}
    ],
    "supp_docs": [
        {"doc_id": 1, "test_id": 12, "title": "DesignPlans.pdf",
        "uri": "files/12/DesignPlans.pdf"},
        {"doc_id": 2, "test_id": 12, "title": "CostProjections.xls",
        "uri": "files/12/CostProjections.xls"},
        {"doc_id": 3, "test_id": 7474890889,
         "title": "Crash Safety Test Sample Document 1",
         "uri": "files/7474890889/Crash Safety Test Sample Document 1"},
        {"doc_id": 4, "test_id": 7474890889,
         "title": "Crash Safety Test Sample Document 2",
         "uri": "files/7474890889/Crash Safety Test Sample Document 2"},
        {"doc_id": 5, "test_id": 3847792993,
         "title": "Battery Duration Stress Test Sample Document 1",
         "uri": "files/3847792993/Battery Duration Stress Test Sample Document 1"},
        {"doc_id": 6, "test_id": 3847792993,
         "title": "Battery Duration Stress Test Sample Document 2",
         "uri": "files/3847792993/Battery Duration Stress Test Sample Document 2"},
        {"doc_id": 7, "test_id": 3847792993,
         "title": "Battery Duration Stress Test Sample Document 3",
         "uri": "files/3847792993/Battery Duration Stress Test Sample Document 3"},
        {"doc_id": 8, "test_id": 3847792993,
         "title": "Battery Duration Stress Test Sample Document 4",
         "uri": "files/3847792993/Battery Duration Stress Test Sample Document 4"},
        {"doc_id": 9, "test_id": 2080844423,
         "title": "Extreme Cold Flight Sample Document 1",
         "uri": "files/2080844423/Extreme Cold Flight Sample Document 1"},
        {"doc_id": 10, "test_id": 2080844423,
         "title": "Extreme Cold Flight Sample Document 2",
         "uri": "files/2080844423/Extreme Cold Flight Sample Document 2"},
        {"doc_id": 11, "test_id": 7474890889,
         "title": "Crash Safety Test Sample Document 3",
         "uri": "files/7474890889/Crash Safety Test Sample Document 3"},
        {"doc_id": 12, "test_id": 7474890889,
         "title": "Crash Safety Test Sample Document 4",
         "uri": "files/7474890889/Crash Safety Test Sample Document 4"},
        {"doc_id": 13, "test_id": 12,
         "title": "ProjectDescription.doc",
         "uri": "files/12/ProjectDescription.doc"},
        {"doc_id": 14, "test_id": 7474890889,
         "title": "Crash Safety Test Sample Document 5",
         "uri": "files/7474890889/Crash Safety Test Sample Document 5"},
        {"doc_id": 15, "test_id": 7474890889,
         "title": "Crash Safety Test Sample Document 6",
         "uri": "files/7474890889/Crash Safety Test Sample Document 6"}
    ]
}

def seed_data(users, test_plans, supp_docs):
    op.bulk_insert(users, seed['users'])
    op.bulk_insert(test_plans, seed['test_plans'])
    op.bulk_insert(supp_docs, seed['supp_docs'])


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    users = op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('position', sa.String(length=100), nullable=True),
    sa.Column('manager_level', sa.String(length=100), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_first_name'), 'users', ['first_name'], unique=False)
    op.create_index(op.f('ix_users_last_name'), 'users', ['last_name'], unique=False)
    test_plans = op.create_table('test_plans',
    sa.Column('test_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('author', sa.Integer(), nullable=False),
    sa.Column('date_submitted', sa.DateTime(), nullable=True),
    sa.Column('days_since_last_activity', sa.Integer(), nullable=True),
    sa.Column('past_submission_attempts', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.Column('risk', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['users.id'], ),
    sa.PrimaryKeyConstraint('test_id')
    )
    op.create_index(op.f('ix_test_plans_risk'), 'test_plans', ['risk'], unique=False)
    op.create_index(op.f('ix_test_plans_status'), 'test_plans', ['status'], unique=False)
    supp_docs = op.create_table('supplemental_documents',
    sa.Column('doc_id', sa.Integer(), nullable=False),
    sa.Column('test_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('uri', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['test_id'], ['test_plans.test_id'], ),
    sa.PrimaryKeyConstraint('doc_id')
    )
    seed_data(users, test_plans, supp_docs)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('supplemental_documents')
    op.drop_index(op.f('ix_test_plans_status'), table_name='test_plans')
    op.drop_index(op.f('ix_test_plans_risk'), table_name='test_plans')
    op.drop_table('test_plans')
    op.drop_index(op.f('ix_users_last_name'), table_name='users')
    op.drop_index(op.f('ix_users_first_name'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
