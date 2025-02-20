from django import forms
from django.core.exceptions import ValidationError

from .models import Mailing
from client.models import Client
from message.models import Message


class MailingForm(forms.ModelForm):
    """ Форма для создания и изменения рассылки """

    class Meta:
        model = Mailing
        fields = ('title', 'start_date', 'end_date', 'periodicity', 'client', 'message',)
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        """
        При инициации формы, получаем информацию о пользователе и фильтруем кверисеты, что бы отображались
        только клиенты и сообщения принадлежащие текущему пользователю.
        """
        self.request = kwargs.pop('request')
        user = self.request.user
        super().__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.filter(owner=user)
        self.fields['message'].queryset = Message.objects.filter(owner=user)

    def clean_date(self):
        """ Метод проверяет что бы дата окончания рассылки не была меньше даты начала """

        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise ValidationError('Дата начала не может быть позже даты окончания')

        return cleaned_data
