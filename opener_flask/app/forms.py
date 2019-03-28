from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Regexp
from app.models import Users

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

phone_patterns = ['\d{3}-\d{3}-\d{4}', '\d{3} \d{3} \d{4}', '\d{10}',
                  '\(\d{3}\)\d{7}', '\(\d{3}\) \d{3} \d{4}',
                  '\(\d{3}\)-\d{3}-\d{4}']
patterns = ('|').join(phone_patterns)

class EditProfileForm(FlaskForm):
    phone = StringField('Phone Number',
                        validators=[Regexp(patterns,
                                           message='must be a valid 10 digit phone number')])
    # password = PasswordField('New Password',
    #                          validators=[
    #                             EqualTo('confirm', message='Passwords must match'),
    #                             DataRequired()
    #                             ])
    #
    # confirm  = PasswordField('Repeat Password')
    submit = SubmitField('Submit')
