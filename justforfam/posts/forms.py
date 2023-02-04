from django import forms
from tinymce.widgets import TinyMCE

from justforfam.posts.models import TextPost


class TextPostForm(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = TextPost
