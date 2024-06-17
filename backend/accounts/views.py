from .forms import StoreCodeLoginForm
from django.contrib.auth.views import LoginView as AuthLoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(AuthLoginView):
    template_name = 'accounts/login.html'
    form_class = StoreCodeLoginForm
    success_url = reverse_lazy('index:index')  # ログイン成功後に index ページにリダイレクト

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return self.success_url



