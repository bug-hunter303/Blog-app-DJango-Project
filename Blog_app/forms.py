from django import forms
from Blog_app.models import Post  # for validation 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # kun model aanusar
        fields = ["title","content"]