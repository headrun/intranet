from django.conf.urls import url
from django.contrib import admin
from intra_app import views as appviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', appviews.home, name='home'),
    url(r'^logout/$', appviews.logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    #url(r'^register/$', register),
    url(r'^policy/(?P<policy>[A-Z|a-z|_].*)/$', appviews.policy, name='policy'),
    url(r'^policies/$', appviews.policies, name='policies'),
    url(r'^profile/$', appviews.profile, name='profile'),
]
