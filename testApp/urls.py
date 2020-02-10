from django.conf.urls import url
from testApp import views

app_name = 'testApp'

urlpatterns = [
    url('^$',views.login, name='login'),
    url('^project/$',views.project,name='project'),
    url('^change_pass/$',views.change_pass, name='change_pass'),
    url('^dash/$',views.dashboard, name='dashboard'),
    url('^emp_dash/$',views.emp_dash, name ='emp_dash'),
]