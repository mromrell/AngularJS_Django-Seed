from django.forms import ModelForm
from apps.public.models import Image

class ImageForm(ModelForm):
    class Meta:
        model = Image