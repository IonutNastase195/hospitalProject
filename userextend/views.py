from random import randint

from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from userextend.forms import UserForm
from userextend.models import UserHistory


def generate_six_token():
    six_digit_code = randint(0, 999999)
    formatted_code = f"{six_digit_code:06d}"
    return formatted_code


sixtoken = generate_six_token()


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.first_name = new_user.first_name.title()
        new_user.last_name = new_user.last_name.title()


        # Generarea unui username

        new_user.username = f'{new_user.first_name[0].lower()}{new_user.last_name.replace(' ', '').lower()}_{str(generate_six_token())}'
        new_user.save()

        details_user = {
            'fullname': f'{new_user.first_name} {new_user.last_name}',
            'username': f'{new_user.username}'
        }
        subject = 'Cont nou in djangoproject'
        message = get_template('mail.html').render(details_user)
        mail = EmailMessage(
            subject,
            message,
            EMAIL_HOST_USER,
            [new_user.email]
        )

        mail.content_subtype = 'html'
        # mail.send()

        # Implementare istoric
        history = (f'A fost adaugat urmatorul user:first_name: {new_user.first_name}, last_name: {new_user.last_name},'
                   f'email: {new_user.email}')

        UserHistory.objects.create(text=history)

        return redirect('login')
