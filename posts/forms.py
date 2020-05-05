from django import forms
from posts.models import Post


class PostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
