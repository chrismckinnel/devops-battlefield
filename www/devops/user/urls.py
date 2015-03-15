from django.conf.urls import patterns, url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from . import views


urlpatterns = patterns(
    '',
    url(r'^register/', CreateView.as_view(
        template_name='user/register.html',
        form_class=UserCreationForm,
        success_url='/')),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^profile/(?P<pk>\d+)/$',
        views.ProfileView.as_view(),
        name='profile'),
    url(r'^create-instance/$',
        views.CreateInstanceView.as_view(),
        name='create_instance'),
)
