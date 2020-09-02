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
            "Davis",
            )
name_boy = random.choice(name_male)

pic_male = (
            "https://cdn.discordapp.com/attachments/617827601729191966/750482071553835148/unknown.png",
            "https://cdn.discordapp.com/attachments/617827601729191966/750482133222686780/unknown.png",
            "https://cdn.discordapp.com/attachments/617827601729191966/750482198657761403/unknown.png",
            "https://cdn.discordapp.com/attachments/617827601729191966/750482234712129636/unknown.png",           
            )
pic_boy = random.choice(pic_male)

bios_male = (
            "I am 21 years old and I enjoys walking, tennis and writing. I am creative and loveable, but can also be very standoffish and a bit unintelligent.",
            "I am 22 years old and love long walks on the beach with you :). I love to create sandcastles then destroy them with 50 pounds of dynamite.",
            "I am 24 years old and am looking for someone that owns a farm.  I have always wanted to work on a farm.  Looking for a good man",
            "I am 25 years old and like working on cars.  I am a certified diesel mechanic but only do it for a hobby.",
            "I am 24 years old and am now trying to start my life with someone who I love.",
            )
bio_boy = random.choice(bios_male)

jobs_male = (
            "Linemen",
            "Army",
            "Pilot",
            "Truck driver",
            "Mechanic",
            "Police Officer",
            "Teacher",
            "Registered Nurses",
            "First-Line Supervisors of Retail Sales Workers",
            "Retail Salespersons",
            "Software Developers, Applications",
            "Customer Service Representatives",
            "Marketing Managers",
            "First-Line Supervisors of Food Preparation and Serving Workers",
            "Computer Systems Analysts",
            "Web Developers",
            "Management Analysts",
            "Medical and Health Services Managers",
            "Information Technology Project Managers",
            )
job_boy = random.choice(jobs_male)

name_female = (
              "Mary", 
              "Patricia", 
              "Jennifer", 
              "Linda", 
              "Elizabeth", 
              "Barbara", 
              "Susan", 
              "Jessica", 
              "Sarah", 
              "Karen", 
              "Nancy", 
              "Margaret", 
              "Lisa", 
              "Betty", 
              "Dorothy", 
              "Sandra", 
              "Ashley", 
              "Kimberly", 
              "Donna", 
              "Emily",
              "Clara",
              )
name_girl = random.choice(name_female)

pic_female = (
            "https://cdn.glitch.com/b1c5e0cc-6e5e-47f5-be38-d143eb316e6e%2Fgirl_pic4.png?v=1599008496120",
            "https://cdn.glitch.com/b1c5e0cc-6e5e-47f5-be38-d143eb316e6e%2Fgirl_pic3.png?v=1599008497357",
            "https://cdn.glitch.com/b1c5e0cc-6e5e-47f5-be38-d143eb316e6e%2Fgirl_pic2.png?v=1599008498922",
            "https://cdn.glitch.com/b1c5e0cc-6e5e-47f5-be38-d143eb316e6e%2Fgirl_pic1.png?v=1599008499986",
            
            )
pic_girl = random.choice(pic_female)

bios_female = (
            "I am 21 years old and I enjoys walking, tennis and writing. I am creative and loveable, but can also be very standoffish and a bit unintelligent.",
            "I am 22 years old and love long walks on the beach with you :). I love to create sandcastles then destroy them with 50 pounds of dynamite.",
            "I am 24 years old and am looking for someone that owns a farm.  I have always wanted to work on a farm.  Looking for a good man",
            "I am 25 years old and like working on cars.  I am a certified diesel mechanic but only do it for a hobby.",
            "I am 24 years old and am now trying to start my life with someone who I love.",
            )
bio_girl = random.choice(bios_female)

jobs_female = (
            "Linemen",
            "Army",
            "Pilot",
            "Truck driver",
            "Mechanic",
            "Police Officer",
            "Teacher",
            "Registered Nurses",
            "First-Line Supervisors of Retail Sales Workers",
            "Retail Salespersons",
            "Software Developers, Applications",
            "Customer Service Representatives",
            "Marketing Managers",
            "First-Line Supervisors of Food Preparation and Serving Workers",
            "Computer Systems Analysts",
            "Web Developers",
            "Management Analysts",
            "Medical and Health Services Managers",
            "Information Technology Project Managers",
            )
job_girl = random.choice(jobs_female)



def main(request):
    data = parse_request_body(request.body.decode('UTF-8'))
    LOG.info(data)
    user = authenticate(username=data['username'], 
                        password=data['password'])
    
    if user is not None:
        template = loader.get_template("main.html")
        return HttpResponse(template.render({"name": user.username, "money": user.webaccount, "points": user.points, "marriage": user.marriage, "name_boy": name_boy, "pic_boy": pic_boy, "bio_boy": bio_boy, "job_boy": job_boy, "name_girl": name_girl, "pic_girl": pic_girl, "bio_girl": bio_girl, "job_girl": job_girl}))

              
            
    
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
    


