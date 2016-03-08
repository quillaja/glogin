from django.contrib.auth.models import User
from django.conf import settings
from oauth2client import client, crypt

class GoogleModelBackend(object):
    """
    Authenticate a user from their google account. The User is stored in the
    database as per Django's normal user model. The user's username is the id
    number google returns when checking the auth token. The authenticate method
    also adds the attribute 'image_url' which is an url where the user's google
    profile image can be gotten.
    
    This backend relies on having google's 'oauth2client', and also on having the
    google client ID in settings at GOOGLE_OAUTH2_CLIENT_ID_WEB. 
    """
    
    def get_user(self, user_primary_key):
        """Get a user from the database by it's primary key."""
        try:
            return User.objects.get(pk=user_primary_key)
        except User.DoesNotExist:
            raise ValueError('user with pk= %s does not exist' % (user_primary_key))
    
    def authenticate(self, token=None):
        """
        Takes an id token given to the app by Google, fetches data using it,
        verifies the data, then gets the User from the database or, if the user
        does not exist, creates a new User with the info fetched from Google.
        Returns a User instance or None.
        """
        
        try:
            if not token:
                raise ValueError('Argument "token" cannot be None.')
            
            idinfo = client.verify_id_token(token, settings.GOOGLE_OAUTH2_CLIENT_ID_WEB)
            # If multiple clients access the backend server:
            if idinfo['aud'] not in [settings.GOOGLE_OAUTH2_CLIENT_ID_WEB]:
                raise crypt.AppIdentityError("Unrecognized client.")
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise crypt.AppIdentityError("Wrong issuer.")
            
            #if passes these checks, then username is in 'sub'
            try:
                user = User.objects.get(username=idinfo['sub'])
            except User.DoesNotExist:
                user = None
            
            if not user:
                #user does not exist. create.
                user = User.objects.create_user(idinfo['sub'], email=idinfo['email'])
                user.first_name = idinfo['given_name']
                user.last_name = idinfo['family_name']
                user.image_url = idinfo['picture'] #TODO: not working...
                user.set_unusable_password()
                user.save()
                
            return user
        
        except:
           return None