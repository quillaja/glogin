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
2. Do your database migrations in Django's usual way.

## Use
To use this as the sign-up and authentication (sign-in) for your website, follow Google's instructions for using (Google Sign-In for Websites)[https://developers.google.com/identity/sign-in/web/sign-in#before_you_begin]. In brief, you add some Javascript to activate Google's end of the magic, and ultimately get an *id token* from Google. This is what you need.

Once you have that id token, use Ajax and POST it to `/glogin/login/` as `id_token`. The response will be a simple text message telling what happened.

To log the user out, you must use Ajax to GET or POST to `/glogin/logout/`. This should be done in the `auth2.signOut().then()` function described in Google's documentation for Google Sign-In.

## Data
The following properties are available on the User model, accessed for example, by `user.google.<prop>`:

1. user - A reference to the Django User model associated with this data.
2. email - The user's email. Should be identical to `user.email`.
3. given_name - The user's first name. Should be identical to `user.first_name`.
4. family_name - The user's last name. Should be identical to `user.last_name`.
5. picture - An url to the user's Google profile image. Undoubtably the most useful of these properties.
6. locale - The user's locale, eg. `en`.