import requests
import jwt
from flask import Flask,render_template, redirect, request, session, url_for
import auth as auth
import boto3
REGION_NAME = 'us-east-2' # e.g., 'us-east-1'
import chat as chat_module
CLIENT_ID = '1g75k5eskepdumocifnk85tqhd'
USER_POOL_ID = 'us-east-2_fznwnb1eC' # Only needed for ADMIN_NO_SRP_AUTH
login_html='resume.html'

app = Flask(__name__, template_folder='/Users/kanishvaranp/Documents/project_1/')

client = boto3.client('cognito-idp', region_name=REGION_NAME)
@app.route('/')
def index():
    return render_template("resume.html")

@app.route('/login' , methods=['POST'])
def login():
        try:
          USERNAME=request.form['username']
          PASSWORD=request.form['password']
          if not USERNAME or not PASSWORD:
               return render_template("resume.html", error="USERNAME and PASSWORD are mandatory")
          responses=auth.login_aws(USERNAME,PASSWORD)
          #print(responses)
          return render_template("results1.html", token=responses['AccessToken'], id_token=responses['IdToken'])
        except Exception as e: 
           return render_template("resume.html", error=str(e))

@app.route('/logout',methods=['POST'])
def logout():
     try:    
          access_token=request.form['token']
          print(access_token)
          resposes=auth.logout_globally(access_token)
          return render_template("resume.html", logout='Logged out')
     except Exception as e:
          return render_template("resume.html", error=str(e))

@app.route('/chat', methods=['POST'])
def chat_route():
     try:
          payload = request.get_json() or {}
          message = payload.get('message')
          id_token = payload.get('id_token')
          if not message:
               return { 'reply': 'No message provided' }, 400
          reply = chat_module.chat_handle(message, id_token)
          return { 'reply': reply }
     except Exception as e:
          return { 'reply': f'Error: {str(e)}' }, 500


@app.route('/settings', methods=['POST'])
def settings_route():
     try:
        payload = request.get_json() or {}
        email = payload.get('email')
        message = payload.get('message')
        id_token = payload.get('id_token')
        if not email:
            return { 'message': 'Email is required' }, 400
        if not message:
            return { 'message': 'Message is required' }, 400
        # TODO: persist the contact form submission (e.g., to DB or email).
        print(f"Contact form: email={email} message={message} id_token={'present' if id_token else 'none'}")
        # Respond with JSON to the frontend
        return { 'message': 'Thank you! We received your message.' }
     except Exception as e:
          return { 'message': str(e) }, 500
if __name__ == "__main__":
    app.run(debug=True)  
