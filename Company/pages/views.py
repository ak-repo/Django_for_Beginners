from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def home_page_view(request):
    context = {
        "inventory_list": ["widget 1", "widget 2", "widget 3"],
        "greeting": "Thank you for visiting",
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 main street"
        context["phone_number"] = "1258854680"
        return context

