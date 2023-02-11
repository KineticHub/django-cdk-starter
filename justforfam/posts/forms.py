from django import forms
from tinymce.widgets import TinyMCE

from justforfam.posts.models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        fields = ['title', 'subtitle', 'banner_image', 'type', 'content']
        model = Post
