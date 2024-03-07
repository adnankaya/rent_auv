from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _





@login_required()
def me_profile(request):
    context = {"title": _("My Profile Page")}

    return render(request, "users/me-profile.html", context)