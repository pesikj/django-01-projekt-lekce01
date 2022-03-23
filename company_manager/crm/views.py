from django.views.generic import CreateView, ListView, TemplateView
import crm.models as models

class IndexView(TemplateView):
    template_name = "index.html"

class AccountCreateView(CreateView):
    model = models.Account
    template_name = "account/create_account.html"
    fields = ["status", "phone_number", "email", "identification_number"]
