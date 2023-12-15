
from allauth.socialaccount.signals import pre_social_login
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver
from django.core.exceptions import PermissionDenied

@receiver(pre_social_login)
def restrict_by_email_domain(sender, request, sociallogin, **kwargs):
    email_domain1 = 'student.gyarab.cz'
    email_domain2 = 's.gyarab.cz'
    email = sociallogin.account.extra_data.get('email', '')

    if not email.endswith('@' + email_domain1 or email_domain2):
        # If the email does not end with '@gyarab.cz', deny access
        raise PermissionDenied('Access denied. Only @gyarab.cz emails are allowed.')