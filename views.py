from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def glogin(request):
    """
    Logs a user in. Requires the Google id token to be POSTED here and called "id_token".
    """
    
    if request.user.is_authenticated():
        return HttpResponse('already logged in')
        
    if request.method == 'POST':
        try:
            #get google token and authenticate.
            user = authenticate(token=request.POST['id_token'])
            if user:
                #user exists
                login(request, user)
                return HttpResponse('successful login')
            else:
                #user doesn't exist or can't log in
                return HttpResponse('user %s could not be logged in' % (str(user)))
        except Exception as e:
            return HttpResponse(str(e))

def glogout(request):
    """
    Logs out whatever user is logged in.
    """
    
    rval = 'no user was logged in'
    if request.user and request.user.is_authenticated():
        logout(request)
        rval = 'successful logout'
        
    return HttpResponse(rval)
