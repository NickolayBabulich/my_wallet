from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator


def send_verification_email(request, user):
    current_site = request.get_host()
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    verification_url = f"http://{current_site}/auth/verify/{uid}/{token}/"

    timeout_minutes = getattr(settings, 'PASSWORD_RESET_TIMEOUT', 30)

    context = {
        'user': user,
        'domain': current_site,
        'uid': uid,
        'token': token,
        'timeout_minutes': timeout_minutes,
        'verification_url': verification_url,
    }

    message = render_to_string('account/email_verification.html', context)

    email = EmailMessage(
        'Активация аккаунта',
        message,
        settings.EMAIL_HOST_USER,
        [user.email]
    )
    email.content_subtype = "html"
    email.send()
