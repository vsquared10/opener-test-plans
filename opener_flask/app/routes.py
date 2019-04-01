from app import app, db
from app.forms import LoginForm, EditProfileForm
from app.models import Users, TestPlans, SupplementalDocuments
from flask import render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/test_plans_list')
@login_required
def test_plans_list():
    data = TestPlans.query.all()
    return render_template('test_plans_list.html', title="Test Plans List", data=data)

@app.route('/test_plan/<int:id>')
@login_required
def test_plan_detail(id):
    test_plan = TestPlans.query.filter_by(test_id=id).first_or_404()
    user = Users.query.filter_by(id=test_plan.author).first_or_404()
    author = user.first_name + ' ' + user.last_name
    supp_docs = SupplementalDocuments.query.filter_by(test_id=test_plan.test_id).all()
    return render_template('test_plan_detail.html', test_plan=test_plan,
                            author=author, supp_docs=supp_docs)

@app.route('/user/<email>', methods=['GET', 'POST'])
@login_required
def user(email):
    # user = Users.query.filter_by(email=email).first_or_404()
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.phone = form.phone.data
        db.session.commit()
        flash('Your changes have been saved.')
    return render_template('user.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('test_plans_list'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('test_plans_list')
        return redirect(next_page)
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
