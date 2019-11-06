# -*- coding: utf-8 -*-

from django.views.generic import CreateView
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import re

import django.http as http

class Index(CreateView):
    template_name = 'web/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

@login_required()
def updatePassword(request):
    return render_to_response('principal.html', context_instance=RequestContext(request))

@require_POST
def ajax_login(request):
    username = request.POST['username'].lower()
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            print ('No se ha podido iniciar sesion')
            return http.HttpResponseRedirect(reverse('inicio', args=(1,)))
    else:
        print ('No se ha podido iniciar sesion 2')
        return http.HttpResponseRedirect(reverse('inicio', args=(1,)))

    return http.HttpResponseRedirect(reverse('inicio'))

def ajax_logout(request):
    logout(request)
    return http.HttpResponseRedirect(reverse('inicio'))
