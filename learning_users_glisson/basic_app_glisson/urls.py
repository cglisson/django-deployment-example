from django.conf.urls import url
from basic_app_glisson import views

# Template URLs
app_name = 'basic_app_glisson'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
