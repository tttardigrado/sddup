from django.template.response import TemplateResponse
from .models import Contact


def contacts(request):
    return TemplateResponse(
        request,
        "snippets/contact_page.html",
        {"contacts": Contact.objects.all()},
    )
