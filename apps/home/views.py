from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required



def index(request):

    context = {"title": _("Home page")}

    return render(request, "home/index.html", context)

# @login_required
def dashboard(request):

    context = {"title": _("Dashboard")}

    return render(request, "home/dashboard/index.html", context)


def pricing(request):

    context = {"title": _("Pricing page")}

    return render(request, "home/pricing/index.html", context)


def contact(request):

    context = {"title": _("Contact Us Page")}

    return render(request, "home/contact/index.html", context)


def aboutus(request):

    context = {"title": _("About Us Page")}

    return render(request, "home/aboutus/index.html", context)


def faq(request):

    context = {"title": _("F.A.Q Page")}

    return render(request, "home/faq/index.html", context)


def privacy(request):

    context = {"title": _("Privacy Page")}

    return render(request, "home/privacy/index.html", context)


def terms(request):

    context = {"title": _("Terms Page")}

    return render(request, "home/terms/index.html", context)
