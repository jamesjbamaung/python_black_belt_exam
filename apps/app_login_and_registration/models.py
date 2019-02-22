from __future__ import unicode_literals
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._+-]+\.[a-zA-Z]+$')

#creating manager class
class UserManager(models.Manager):
    def basic_validator(self, postData):
        #defining object errors that will contain error messages if errors exist
        errors = {}
        email_match = User.objects.filter(email=postData['email'])

        if len(postData['first_name']) == 0:
            #if user input first_name from form data on html.index is less than 2 characters, add an error message to errors
            errors['first_name'] = "you must enter a first name"
            return errors
        elif len(postData['first_name']) < 2:
            #if user input first_name from form data on html.index is less than 2 characters, add an error message to errors
            errors['first_name'] = "name must be at least 2 characters"
            return errors
        if len(postData['last_name']) == 0:
            #if user input last_name from form data on html.index is less than 2 characters, add an error message to errors
            errors['last_name'] = "you must enter a first name"
            return errors        
        elif len(postData['last_name']) < 2:
            #if user input last_name from form data on html.index is less than 2 characters, add an error message to errors
            errors['last_name'] = "name must be at least 2 characters"
            return errors
        if len(postData['email']) == 0:
            errors['email'] = 'No email was enertered'
            return errors
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Email address is not valid'
            return errors
        elif len(email_match) > 0:
            errors['email'] = 'Email has already been registered'
            return errors
        elif len(postData['password']) < 8:
            #if the password is less than 8 characters add error message
            errors['password'] = "password should be at least 8 characters"
            return errors
        elif postData['password'] != postData['confirm_password']:
            #if check to compare values of password and confirmation fields
            errors['password'] = "Passwords do not match"
            return errors
        #i need to check if the email is unique to the User database
        #to do this i need to compare it to every email in the database
        #i need to creat a for loop to iterate through every users email
        #defining variable all_users to use in a for loop
        all_users = User.objects.all()
        for user in all_users:
            #if the email from the form is equal to a user email, then add error message
            if postData['email'] == user.email:
                errors['email'] = "email is already registered in database"
            # if postData['login_password'] == user.password.encode():
            # #bcrypt.checkpw(postData['login_password'].encode(), user.password.encode()):
            #     errors['login_password'] = "try again"
        return errors





    def login_validator(request, postData):
        errors = {}
        user = User.objects.filter(email=postData['login_email'])
        if len(postData['login_email']) == 0:
            errors['login_email'] = "email not entered"
        if len(postData['login_password']) == 0:
            errors['login_password'] = "email not entered"
        elif len(user) == 0:
            errors['login_email'] = "email is not registered"
        else:
            user = User.objects.get(email=postData['login_email'])
            print("befor if check")
            print(postData['login_password'].encode())
            print(user.password.encode())
            if bcrypt.checkpw(postData['login_password'].encode(), user.password.encode()):
                print('password matches')
            else:
                print('/////////////////////////////////////////////////////')
                print('/////////////////////////////////////////////////////')
                print('/////////////////////////////////////////////////////')
                print('/////////////////////////////////////////////////////')
                errors['login_password'] = "invalid credentials"
        return errors

    def update_validator(request, postData):
        #defining object errors that will contain error messages if errors exist
        errors = {}
        email_match = User.objects.filter(email=postData['email'])

        if len(postData['first_name']) == 0:
            errors['first_name'] = "you must enter a first name"
            return errors
        elif len(postData['first_name']) < 2:
            #if user input first_name from form data on html.index is less than 2 characters, add an error message to errors
            errors['first_name'] = "first name must be at least 2 characters"
            return errors
        if len(postData['last_name']) == 0:
            #if user input last_name from form data on html.index is less than 2 characters, add an error message to errors
            errors['last_name'] = "you must enter a last name"
            return errors
        if len(postData['last_name']) < 2:
            #if user input last_name from form data on html.index is less than 2 characters, add an error message to errors
            errors['last_name'] = "last name must be at least 2 characters"
            return errors
        if len(postData['email']) == 0:
            errors['email'] = 'No email was enertered'
            return errors
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Email address is not valid'
            return errors
        elif len(email_match) > 0:
            errors['email'] = 'Email has already been registered'
            return errors
        elif len(postData['password']) < 8:
            #if the password is less than 8 characters add error message
            errors['password'] = "password should be at least 8 characters"
            return errors
        elif postData['password'] != postData['confirm_password']:
            #if check to compare values of password and confirmation fields
            errors['password'] = "Passwords do not match"
            return errors
        return errors

    def quote_validator(request, postData):
        errors = {}
        if len(postData['author']) == 0:
            errors['author'] = "enter an author name"
            return errors
        elif len(postData['author']) < 3:
            errors['author'] = "Author name should be at least 3 characters"
            return errors
        if len(postData['quote']) == 0:
            errors['quote'] = "enter a quote"
            return errors
        if len(postData['quote']) < 10:
            errors['quote'] = "Quote should be at least 10 characters"
            return errors
        return errors


                                                                            # else:
                                                                            #     errors['login_password'] = "try again"
                                                                            #     return errors



                                                                            # all_users = User.objects.all()
                                                                            # for user in all_users:
                                                                            #     if postData['login_email'] == user.email:
                                                                            #         # login_user = User.objects.get(email=postData['login_password'])
                                                                            #         # if bcrypt.checkpw(postData['login_email'].encode(), login_user.password.encode()):
                                                                            #         return errors
                                                                            #         # else:
                                                                            #         #     errors['login_password'] = "try again"
                                                                            #     else: 
                                                                            #         errors['login_email'] = "email is not registered"
                                                                            #         return errors

                                                                            # # login_user = User.objects.get(email=postData['login_email'])
                                                                            # # if bcrypt.checkpw(postData['login_password'].encode(), login_user.password.encode()):
                                                                            # #     return errors
                                                                            # errors['login_password'] = "try again"
                                                                            # return errors


#creating User class
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #linking UserManager to the User class
    objects = UserManager()

    def __repr__(self):
        return f"<User Name: {self.first_name} {self.last_name}>"
