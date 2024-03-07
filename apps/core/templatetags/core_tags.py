from django import template

from allauth.account.utils import has_verified_email


# internals

register = template.Library()


@register.simple_tag
def is_email_verified(user, email):
    return has_verified_email(user, email)
