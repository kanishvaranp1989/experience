from flask import Flask, redirect, request, session, url_for
import boto3
import json
REGION_NAME = 'us-east-2' # e.g., 'us-east-1'
CLIENT_ID = '1g75k5eskepdumocifnk85tqhd'
USER_POOL_ID = 'us-east-2_fznwnb1eC' # Only needed for ADMIN_NO_SRP_AUTH

app = Flask(__name__)

client = boto3.client('cognito-idp', region_name=REGION_NAME)
@app.route('/login')
def login_aws(username, password):
    response = client.initiate_auth(
        ClientId=CLIENT_ID,
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        }
    )    
    print("AUTH executed")
    # Returns tokens (IdToken, AccessToken, RefreshToken)
    #return response['AuthenticationResult']['AccessToken']
    return response['AuthenticationResult']
    
def logout_globally(access_token):
    # This requires an Access Token with the 'aws.cognito.signin.user.admin' scope
    response = client.global_sign_out(
        AccessToken=access_token
    )
    return response['ResponseMetadata']['HTTPStatusCode']

#print(login_aws(USERNAME,PASSWORD))
#print(logout_globally('eyJraWQiOiJZWThcL2V5c2JhYmZUZzFvc1BLZ0N5bGRpWUc1Ym1Nb2pvcXVCaExpVk16UT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJjMTZiNTUzMC03MDYxLTcwMzEtN2NkNC01NDNlNWFlYWJmYjUiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0yLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMl9mem53bmIxZUMiLCJjbGllbnRfaWQiOiIxZzc1azVlc2tlcGR1bW9jaWZuazg1dHFoZCIsIm9yaWdpbl9qdGkiOiI4NTRmZGU2Ni1mMWIxLTRhZDktYWY3MS00MzQ2NmUzOThiMmEiLCJldmVudF9pZCI6IjQxMzY2YjZiLWQ2YzctNDcxMy04M2U1LTA1MDNjMGQwMjJjZCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE3NzE0NjQ5MDIsImV4cCI6MTc3MTQ2ODUwMiwiaWF0IjoxNzcxNDY0OTAyLCJqdGkiOiIzNDBiMDIxOC03NjA1LTRhNWYtYjAyMy1lZjgwNjIyMWJjZDAiLCJ1c2VybmFtZSI6ImMxNmI1NTMwLTcwNjEtNzAzMS03Y2Q0LTU0M2U1YWVhYmZiNSJ9.ksqiPvPCE1LHlVWu_YPzaLfZDeJIn3bZK654FfhCdV0lWLnDtdXc6zS9_IR-MTtaLkLxSI7u2sjdqTI2SzMTsgxhJ597bfEGMN96xtF6oxJSbFsA7XlNDDnxAKhBY9s0iO0p_c3pvHWxK3beYg399Wg7eAxgoh9nmmpwoStQWnXVHTyraiS09yow1VxBCBmwHQoFdGlMBjW_Lnrz9XYJGCDvs5lLcP1Y3dGPaessD_oE7Atgrn-H4JePAcCk6a5MxomvTYgcPW1by-Gz_kNpsFXX-cj-in3FwPOEEeXKpJU23PxkBi3FIt9ku2-DAT0EwRIEmUAXLNMsPHYKE2---w'))