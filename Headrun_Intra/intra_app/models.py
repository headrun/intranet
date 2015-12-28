from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
import os

BASE_DIR = getattr(settings, "BASE_DIR", None)
# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    personal_mailid = models.CharField(max_length=128, blank=True, null=True)
    phnum = models.IntegerField(blank=True, null=True)
    age  = models.IntegerField(blank=True, null=True)
    dob  = models.DateTimeField(default=timezone.now, blank=True, null=True)
    doj  = models.DateTimeField(default=timezone.now, blank=True, null=True)
    presentaddress = models.TextField(blank=True, null=True)
    permanentaddress = models.TextField(blank=True, null=True)
    choices = ((0, 'SSCbelow'), (1, 'SSC'), (2, 'Graduate'), (3, 'Graduate and Above'))
    HQualification = models.IntegerField(default=3, blank=True, choices=choices, null=True)
    bankac  = models.CharField(max_length=32, null=True, blank=True)
    image   = models.FileField(upload_to=os.path.join(BASE_DIR, 'static', 'uploads', 'img'), blank=True, null=True)
    def __unicode__(self):
        return "Name: %s, Age: %s, Email: %s, DOB: %s" % (self.user.username, self.age, self.personal_mailid, self.dob)


