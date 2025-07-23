from allauth.account.views import ConfirmEmailView


class CustomEmailConfirmView(ConfirmEmailView):
    """A custom view to overide the default allauth view for email confirmation"""
    template_name = 'accounts/email_confirm.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.confirm(request)
        return super().get(request, *args, **kwargs)