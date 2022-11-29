from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        # This will render a form
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
