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
        fields = ['title', 'content', 'image', 'published_date']
        # fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'published_date': forms.SelectDateWidget(empty_label=("Year", "Month", "Day"),)
        }
    # Validating the fields

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = Post.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(id=instance.id)
        if qs.exists():
            raise forms.ValidationError(
                'Title has been already used. Please enter new one')
        return title

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) > 1000:
            raise forms.ValidationError('Content is too long to save')
        return content
