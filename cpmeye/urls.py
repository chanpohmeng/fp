from django.conf.urls import patterns, url

from cpmeye import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_submission/$', views.add_submission, name='add_submission'), # NEW MAPPING!
        url(r'^register/$', views.register, name='register'),
        url(r'^suggest_submission/$', views.suggest_submission, name='suggest_submission'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^voteup/$', views.voteup, name='voteup')
)