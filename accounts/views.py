from allauth.account.views import ConfirmEmailView


class CustomEmailConfirmView(ConfirmEmailView):
    template_name = 'accounts/email_confirm.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.confirm(request)
        return super().get(request, *args, **kwargs)