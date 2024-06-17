from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

class StoreCodeLoginForm(BaseForm):
    store_code = forms.CharField(label='Store Code')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        store_code = self.cleaned_data.get('store_code')
        password = self.cleaned_data.get('password')

        if store_code and password:
            try:
                user = User.objects.get(store_code=store_code)
                if user.check_password(password):
                    self.user_cache = user
                else:
                    raise forms.ValidationError("Invalid password")
            except User.DoesNotExist:
                raise forms.ValidationError("Invalid store code")

        return self.cleaned_data

    def get_user(self):
        return self.user_cache
