import secrets
import string

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject='Подтверждение почты',
            message=f"Привет, перейди по ссылке, что бы подтвердить почту {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def generate_password():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = "".join(secrets.choice(alphabet) for i in range(12))
        if (
                any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3
        ):
            break
    return password


def password_recovery(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(f'Получен адрес {email}')
        user = get_object_or_404(User, email=email)
        print(f'Пользователь {user}')
        password = ''
        new_password = generate_password()
        user.set_password(new_password)
        user.save()

        message = f"Привет, это твой новый 12-ти символьный пароль, который ты тоже забудешь: {new_password}. \
                                Если вы не запрашивали восстановление пароля, просто игнорируйте это сообщение."

        send_mail(
            subject="Восстановление пароля",
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
        )
        return redirect(reverse('users:login'))
    return render(request, 'users/password_recovery.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user