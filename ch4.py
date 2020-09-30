from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, ValidationError

class NameForm(Form):
    name = StringField("What is your name?", validators=[Required()])
    email = StringField("What is your UofT Email address?", validators=[Required()])
    submit = SubmitField("Submit")

    def validate_email(form, field):
        if (field.data.find('@') == -1):
            raise ValidationError("Not a valid email address. Please include an '@'.")


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'krabbypattysecretformula'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        email = form.email.data
        utoronto = email.find('utoronto')

        # inserting email logic
        if (utoronto == -1 or email.find('@') > utoronto):
            session['email'] = "Please use your UofT email"
        else:
            session['email'] = "Your UofT email is " + email

        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
            session['name'] = form.name.data
            return redirect(url_for('index'))
    return render_template('index_ch4.html', form = form, name = session.get('name'), email = session.get('email'))

if __name__ == '__main__':
    app.run(debug=True)