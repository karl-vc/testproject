from django.conf.urls import url
from testApp import views

app_name = 'testApp'

urlpatterns = [
    url('^$',views.login, name='login'),
    url('^project/$',views.project,name='project'),
]