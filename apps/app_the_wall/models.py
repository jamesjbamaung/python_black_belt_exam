from django.db import models
from apps.app_login_and_registration.models import User
#import User class from app_login_and_registration


#we already have a user class in app login and registation
#we need to define 2 more classes

class Quote(models.Model):
    #accessing User class from login and registration
    user = models.ForeignKey(User, related_name="messages")
    author = models.CharField(max_length=45)
    quote = models.TextField()
    #added many to many like field relating likes to the user to made the message
    like = models.ManyToManyField(User, related_name="liked_messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Comment(models.Model):
    quote = models.ForeignKey(Quote, related_name="comments")
    user = models.ForeignKey(User, related_name='comments')
    #added many to many like field relating likes to the user to made the commment
    like = models.ManyToManyField(User, related_name="liked_comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

