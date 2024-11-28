from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import View, CreateView, TemplateView

from apps.account.forms import CustomUserCreationForm
from apps.account.utils import send_verification_email


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('auth:signup_done')
    template_name = 'account/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object

        send_verification_email(self.request, user)

        return response


class SignUpDoneView(TemplateView):
    template_name = 'account/signup_done.html'

class SignUpConfirmView(TemplateView):
    template_name = 'account/signup_confirm.html'


class EmailVerificationView(TemplateView):
    def get(self, request, uidb64, token):
        User = get_user_model()
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)

            if not user.is_active and default_token_generator.check_token(user, token):
                user.is_active = True
                user.save()

                user.refresh_from_db()
                login(request, user)

                messages.success(request, 'Ваш email успешно подтвержден!')
                return redirect('auth:signup_confirm')

            else:
                if user.is_active:
                    messages.info(request, 'Ваш аккаунт уже активирован.')
                    return render(request, 'account/email_verification_error.html')
                else:

                    messages.error(request, 'Ссылка для активации недействительна!')
                    user.delete()

                return render(request, 'account/email_verification_error.html')

        except (TypeError, ValueError, OverflowError):
            messages.error(request, 'Ошибка при обработке ссылки активации.')
            return redirect('auth:signup')

        except User.DoesNotExist:

            messages.error(request, 'Пользователь не найден.')
            return redirect('auth:signup')
