from django.forms import ModelForm
from app.models import todo, image


class todoForm(ModelForm):
    class Meta:
        model = todo
        fields = ["title", "description", "status", "priority"]


class imageupload(ModelForm):
    class Meta:
        model = image
        fields = ["images"]
