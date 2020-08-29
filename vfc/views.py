import logging
from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect
from django.template import Context, loader


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


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def complete_signup(request):
    params = request.body.decode('UTF-8').split("&")
    data = {}
    for param in params:
        field, value = param.split('=')
        if field == 'signup-submit':
            continue
        if not value:
            return HttpResponseServerError(f'Value for {field} is blank!')
        data[field] = value
    if data['password'] != data['passwordrepeat']: 
        return HttpResponseServerError('Passwords entered do not match!')   
    
    template = loader.get_template("login.html")
    return HttpResponse(template.render({'message': "Sign Up Successful! Please Log In"}))
    