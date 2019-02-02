from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from users.models.photos import Photo





class ImageForm(ModelForm):

    class Meta:
        model = Photo
        fields = ('picture',)

    class ImageForm(forms.ModelForm):
        class Meta:
            model = Photo
            fields = ('picture',)


    def clean_picture(self):
        picture = self.cleaned_data.get('picture', False)
        picture_size = picture.file.__sizeof__()
        limit_mb = 150 # accept only 150 mb
        if picture_size > (limit_mb * 1024):
            raise ValidationError(" size of file is  limited")
        return picture




