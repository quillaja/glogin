# glogin
A simple Google OAuth2 backend for Django. 

## Installation
Get the app into your django website.

## Configuration
#### 1. pre-reqs
1. Get Google's `oauth2client` package from pip.
2. Get an oauth2 client id from Google via their developer console.
3. Configure the normal Django auth and sessions apps and middleware.

#### 2. your site/app's settings
1. Add this app to the list of the installed apps in django's settings.py
2. Assuming the app is in the "glogin" folder, add `glogin.backend.GoogleModelBackend` to settings.py in `AUTHENTICATION_BACKENDS`
3. Add the setting `GOOGLE_OAUTH2_CLIENT_ID_WEB` to settings.py and with a string value of the oauth2 client id from step 1.2.

#### 3. other django stuff
1. Add glogin's urls to the site urls.py in the usual way. Ex: `url(r'^glogin/?', include('glogin.urls'))`

## Info
Stuff and things.
