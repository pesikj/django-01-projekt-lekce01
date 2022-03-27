from django.views.generic import CreateView, ListView, TemplateView
import crm.models as models
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = "index.html"

class CompanyCreateView(CreateView):
    model = models.Company
    template_name = "company/create_company.html"
    fields = ["name", "status", "phone_number", "email", "identification_number"]
    success_url = reverse_lazy("index")

class CompanyListView(ListView):
    model = models.Company
    template_name = "company/list_company.html"

class OpportunityCreateView(CreateView):
    model = models.Opportunity
    template_name = "opportunity/create_opportunity.html"
    fields = ["value", "company", "sales_manager", "description", "status"]
    success_url = reverse_lazy("index")

class OpportunityListView(ListView):
    model = models.Opportunity
    template_name = "opportunity/list_opportunity.html"