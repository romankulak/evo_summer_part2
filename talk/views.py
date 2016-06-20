# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post
from .forms import PostForm
from django.views.decorators.csrf import csrf_exempt
import json
import random


@csrf_exempt
def home(req):

    tmpl_vars = {
        'all_posts': Post.objects.reverse(),
        'form': PostForm()
    }
    return render(req, 'talk/index.html', tmpl_vars)

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        response_data = {}
        post_text = request.POST.get('the_post')
        if bool(Post.objects.filter(text=post_text)):
            post = Post.objects.get(text=post_text)
        else:
            WORDS = ("пресвятейший", "суперсвятейший", "жгучий", "могучий", "дремучий", "п'ющий", "поющий")
            post = Post(text=post_text, epit=random.choice(WORDS))
            post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['epit'] = post.epit

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
