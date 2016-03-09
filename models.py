from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Google(models.Model):
    """
    Extends the existing Django user model with additional profile information
    that is provided from the "profile" and "email" OAuth scopes. Most of this information
    is duplicate of that in the Django user model, but "picture" and "locale" are
    unique to here. Of these, "picture" is the most useful, as it is an url to the user's
    Google profile image.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    given_name = models.CharField(max_length=256)
    family_name = models.CharField(max_length=256)
    picture = models.UrlField(max_length=512)
    locale = models.CharField(max_length=16)
    