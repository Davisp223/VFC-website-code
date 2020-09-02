import logging
from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib import messages
import random
from random import randint

from .models import User
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
        name_male = (
            "James",
            "John", 
            "Robert", 
            "Michael", 
            "William", 
            "David", 
            "Richard", 
            "Joseph", 
            "Thomas", 
            "Charles", 
            "Christopher", 
            "Daniel", 
            "Matthew", 
            "Anthony", 
            "Donald", 
            "Mark", 
            "Paul", 
            "Steven", 
            "Andrew", 
            "Kenneth",
            "Davis"
            )
        name_boy = random.choice(name_male)

        pic_male = (
            "https://cdn.discordapp.com/attachments/617827601729191966/750482071553835148/unknown.png",
            "https://cdn.discordapp.com/attachments/617827601729191966/750482133222686780/unknown.png",
            "https://cdn.discordapp.com/attachments/617827601729191966/750482198657761403/unknown.png",
            "https://cdn.discordapp.com/attachments/617827601729191966/750482234712129636/unknown.png",
            
            )
        pic_boy = random.choice(pic_male)
        bio_male = (
            "",
            "",
            "",
            "",
            
            )
        bio_boy = random.choice(bio_male)
        job_male = (
            "",
            "",
            "",
            "",
            
            )
        job_boy = random.choice(job_male)
        template = loader.get_template("main.html")
        return HttpResponse(template.render({"name": user.username, "money": user.webaccount, "points": user.points, "marriage": user.marriage, "name_boy": name_boy, "pic_boy": pic_boy, "bio_boy": bio_boy, "job_boy": job_boy}))

              
            
    
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
    


