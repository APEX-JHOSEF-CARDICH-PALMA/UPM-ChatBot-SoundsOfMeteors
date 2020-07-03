from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect
from django.urls import reverse

def chatbot(request):
    context = {
    }
    if request.method == 'GET':
        context['username'] = request.user
        template = loader.get_template("sonidosdelcielo/page-chat.html")
        return HttpResponse(template.render(context,request))
   # return redirect(reverse('home'),context)

