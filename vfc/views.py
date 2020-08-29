import logging
from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .utils import parse_request_body

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def signup(request):
    template = loader.get_template("signup.html")
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render({'message': "Welcome Back!"}))


def logout(request):
    # Impliment actual logout
    return HttpResponseRedirect("/")


def main(request):
    data = parse_request_body(request.body.decode('UTF-8'))
    LOG.info(data)
    user = authenticate(username=data['username'], 
                        password=data['password'])
    if user is not None:
        template = loader.get_template("main.html")
        return HttpResponse(template.render())
    
    LOG.info(f"No record found for {data['username']}")
    template = loader.get_template("login.html")
    return HttpResponse(template.render(
        {'message': "Invalid Login! Please sign up or try again!"}))


def complete_signup(request):
    data = parse_request_body(request.body.decode('UTF-8'))
    for field, value in data.items():
        if field == 'signup-submit':
            continue
        if not value or value == '':
            return HttpResponseServerError(f'Value for {field} is blank!')
    if data['password'] != data['passwordrepeat']: 
        return HttpResponseServerError('Passwords entered do not match!')   
    
    user = User.objects.create_user(
        data['username'], data['email'], data['password'])
    user.save()
    
    LOG.info(f"User created: {data['username']}, {data['email']} {data['password']}")
    template = loader.get_template("login.html")
    return HttpResponse(template.render({'message': "Sign Up Successful! Please Log In"}))
    