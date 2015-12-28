#from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from models import *
import re
USER_PROF_FIELDS = ['personal_mailid', 'phnum', 'age', 'dob', 'doj', 'presentaddress', 'permanentaddress', 'choices', 'HQualification', 'image']
# Create your views here.

@login_required
def home(request):
    '''
    if not request.user.is_authenticated():
      return render(request, 'home.html', {})
    else:
      return HttpResponseRedirect('/policies')
    '''
    return HttpResponseRedirect('/policies')


def get_json(object_name={}, list_of_fields=[]):
    return dict([(field, getattr(object_name, field)) for field in list_of_fields])

@login_required
def profile(request):
    data = get_json(UserProfile.objects.get(id=request.user.id), USER_PROF_FIELDS)
    data['image'] = re.sub("[A-Z|a-z|0-9|\/|_|\s|\&|\(|\)|\!|\@|\#]+static/", '/static/', data['image'].url)
    return render(request, 'profile.html', {'UserProfile': data})

@login_required
def policies(request):
    return render(request, 'policies.html')

@login_required
def policy(request, policy=''):
    if not policy:
        return HttpResponseRedirect('/')
    else:
        templ = "%s.html" % (policy)
    return render(request, templ)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

