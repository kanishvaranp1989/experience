// static/auth.js

// AWS region and user pool configuration
const region = 'us-east-2';
const userPoolId = 'us-east-2_fznwnb1eC';
const clientId = '1g75k5eskepdumocifnk85tqhd';

// configure AWS SDK
AWS.config.region = region;
const cognito = new AWS.CognitoIdentityServiceProvider();

async function login(event) {
    console.log('login() invoked');
    if (event && event.preventDefault) {
        event.preventDefault();
    }
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const params = {
        AuthFlow: 'USER_PASSWORD_AUTH',
        ClientId: clientId,
        AuthParameters: {
            USERNAME: username,
            PASSWORD: password
        }
    };
    try {
        const result = await cognito.initiateAuth(params).promise();
        console.log('login success', result);
        const tokens = result.AuthenticationResult;
        localStorage.setItem('idToken', tokens.IdToken);
        localStorage.setItem('accessToken', tokens.AccessToken);
        // after successful login redirect to results1 route with tokens
        updateUI();
        const url = new URL(window.location.origin + '/results1');
        url.searchParams.set('token', tokens.AccessToken);
        url.searchParams.set('id_token', tokens.IdToken);
        window.location.href = url.toString();
    } catch (err) {
        alert('Authentication failed: ' + err.message);
    }
}

function logout(event) {
    if (event && event.preventDefault) {
        event.preventDefault();
    }
    const idToken = localStorage.getItem('idToken');
    if (idToken) {
        cognito.globalSignOut({ AccessToken: localStorage.getItem('accessToken') }, () => {});
    }
    localStorage.removeItem('idToken');
    localStorage.removeItem('accessToken');
    window.location.reload();
    updateUI();
}

// attach the listeners and update UI on load
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('myFormfileLogin');
    if (loginForm) {
        loginForm.addEventListener('submit', login);
    }
    updateUI();
});

function updateUI() {
    const loggedIn = !!localStorage.getItem('idToken');
    document.getElementById('loginDiv').style.display = loggedIn ? 'none' : 'block';
    document.getElementById('logoutDiv').style.display = loggedIn ? 'block' : 'none';
}
