from django.conf.urls import url
import views

urlpatterns = [
    url(r'^login/?', views.glogin),
    url(r'^logout/?', views.glogout),
]