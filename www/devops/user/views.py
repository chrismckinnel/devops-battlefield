from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.contrib.auth import logout as auth_logout, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.http import JsonResponse

from devops.user import service
from devops.user import forms


class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        kwargs = {'pk': user.id}
        auth_login(self.request, user)
        return HttpResponseRedirect(reverse_lazy('profile', kwargs=kwargs))


class LogoutView(RedirectView):
    url = '/'
    permanent = False

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        response = super(LogoutView, self).get(request, *args, **kwargs)
        return response


class ProfileView(DetailView):
    template_name = 'user/profile.html'
    model = User


class CreateInstanceView(FormView):
    http_method_names = ['post']
    form_class = forms.InstanceForm

    def form_valid(self, form):
        user_id = form.cleaned_data.get('user_id')
        if not user_id:
            return JsonResponse({'success': False, 'reason': 'No user'})
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'reason': 'No user'})
        service.create_instance(user=user)
        return JsonResponse({'success': True})
