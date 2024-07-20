from django import forms
from django.forms import ModelForm, BooleanField

from blog.models import Blog


class StyleFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class BlogForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "slug", "content", "preview", "published", "number_views")
