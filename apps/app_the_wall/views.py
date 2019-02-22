from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *

def quotes(request):
    #if check to see if user has logged in.
    # request.session['user_id'] was created in the views.py file in the login app under the success method
    if 'user_id' in request.session:
        context = {
            'users': User.objects.all(),
            'quotes': Quote.objects.all(),
            'comments': Comment.objects.all(),
            'logged_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "app_the_wall/wall.html", context)
    else:
        return redirect('/')

def post_quote(request):
    errors = User.objects.quote_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/quotes')
    else:
        quote = Quote.objects.create(user=User.objects.get(id=request.session['user_id']), author=request.POST['author'],quote=request.POST['quote'])
        # request.session['message_id'] = message.id
        return redirect('/quotes')


def comments(request):
    comment = Comment.objects.create(quote=Quote.objects.get(id=request.POST['quote']),user=User.objects.get(id=request.session['user_id']),comment=request.POST['comment'])
    # request.session['comment_id'] = comment.id
    return redirect('/quotes')

def delete_quote(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    quote.delete()
    return redirect('/quotes')

def like_quote(request, quote_id):
    user = User.objects.get(id=request.session['user_id'])
    quote = Quote.objects.get(id=quote_id)
    quote.like.add(user)
    quote.save()
    return redirect('/quotes')

def like_comment(request, comment_id):
    user = User.objects.get(id=request.session['user_id'])
    comment = Comment.objects.get(id=comment_id)
    comment.like.add(user)
    comment.save()
    return redirect('/quotes')





# Create your views here.
