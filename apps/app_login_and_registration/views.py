from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *
#importing message and commment classes from the_wall model.py file
from ..app_the_wall.models import *





def index(request):
    return render(request, "app_login_and_registration/index.html")

def success(request):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = User.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key,value in errors.items():
            messages.error(request, value)
        #redirect back to the home page
        return redirect('/')

    else:
        print('///////////////////////////////////////////////////')

        #defining encoded password as variable name password
        pword = request.POST['password']
        hashed = bcrypt.hashpw(pword.encode(), bcrypt.gensalt())
        #creating user with form data on index.html page, password is set equal to the variable password defined on the line 11
        user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'], password=hashed.decode())
        #storing the user id of the user instance created
        request.session['user_id'] = user.id
                                # context = {
                                #     'user': User.objects.get(id=int(request.session['id']))
                                # }
                                #rendering success.html page with context passed in
                                #'user' in context will be used on the front end to access the first name, last name and password of associated user
        return redirect('/quotes')

def successful_login(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    else:
        #getting user with the associated email
        #this will be used to store the user's id in session
        user = User.objects.get(email=request.POST['login_email'])
        request.session['user_id'] = user.id
        return redirect('/quotes')





    #getting all users with the associated email entered into the form on index.html page
    
    # if len(user) > 0:
    # #if the query set is populated with at least one user then run code block

    #     #if check that compares encoded password from the first user matching query set to the encoded password entered in the form on indes.html
    #     if bcrypt.checkpw(request.POST['login_password'].encode(), user[0].password.encode()):
    #         context = {
    #             #defines a 'user' that corresponds to the user with the associate email
    #             'user': User.objects.get(email=request.POST['login_email'])
    #         }
    #         request.session['user_id'] = user[0].id
    #         #if the passwords match up render the success.html page passing in context
    #         return redirect('/wall')
    #     else:
    # #if there are no users matching the email provided on the form, redirect to the home page
    #         return redirect('/')
    # else:
    # #if there are no users matching the email provided on the form, redirect to the home page
    #     return redirect('/')

def log_out(request):
    request.session.clear()
    return redirect('/')

def my_account(request, user_id):
    context = {
        'logged_user': User.objects.get(id=user_id)
    }
    return render(request, "app_login_and_registration/my_account.html", context)

def posted_by(request, quote_user_id):
    # print(User.objects.get(id=message_user_id))
    context = {
        "logged_user": User.objects.get(id=quote_user_id),
        'logged_quote': Quote.objects.filter(user=User.objects.get(id=quote_user_id)),
    }
    return render(request, "app_login_and_registration/posted_by.html",context)


def edit_account(request):
    errors = User.objects.update_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/my_account/'+ str(request.session['user_id']))
    else:
        this_user = User.objects.get(id=request.session['user_id'])
        this_user.first_name = request.POST['first_name']
        this_user.last_name = request.POST['last_name']
        this_user.email = request.POST['email']
        #defining encoded password as variable name password
        pword = request.POST['password']
        hashed = bcrypt.hashpw(pword.encode(), bcrypt.gensalt())
        this_user.password = hashed 
        this_user.save()
        return redirect('/quotes')






