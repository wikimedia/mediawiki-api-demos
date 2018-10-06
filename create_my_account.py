import requests
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
session = requests.Session()
URL = "https://test.wikipedia.org/w/api.php"
 
# App config.
DEBUG = True
APP = Flask(__name__)
APP.config.from_object(__name__)
APP.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class MWCreateAccountForm(Form):
    """ Design MediaWiki Create Account form using Flask's Form class
   """
    name = TextField('name:', validators=[validators.required()])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
    retype = TextField('password:', validators=[validators.required(), validators.Length(min=3, max=35)])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])          
 
@APP.route("/", methods=['GET', 'POST'])
def form():
    """ Render form template and handle form submission request
   """
    form = MWCreateAccountForm(request.form)
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        retype = request.form['password']
        email = request.form['email']
        start_create_account(name,password,retype, email)
    return render_template('create_my_account_form.html', form=form)
 
def start_create_account(name, password,retype,email):
    """ Fetch create account token"""
    
    create_account_token = fetch_create_account_token()
    Response = session.post(url=URL, data={
        'action': 'createaccount',
        'createtoken':create_account_token,
        'username': name,
        'password': password,
        'retype': password,
        'createreturnurl': 'http://example.com/',
        'format':'json',
    })
    data = Response.json()
    print (data)

def fetch_create_account_token():
    """ Fetch create account token"""
    Response = session.get(
        url=URL,
        params={
            'action': 'query',
            'meta': 'tokens',
            'type': 'createaccount',
            'format': 'json',})
    data = Response.json()
    return data['query']['tokens']['createaccounttoken']
    print (data)

def captcha_authentication():
    """Fetch captcha to help authenticate account creation
    """
    Response = session.get(
        url=URL,
        params={
            "query": "cancreateaccounts",
            "id": "captchaAuthenticationRequest",
            "metadata": "type",
            "provider": "CaptchaAuthenticationRequest",
            "fields": "captchaId",
            "required": "required",
            "account": "CaptchaAuthenticationRequest"})
    data = Response.json()
    return data['query']['id']['metadata']
    print (data)

if __name__ == "__main__":
    APP.run()