from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length = 50, required = True, widget = forms.TextInput(attrs={'class': 'commentator'}))
    text = forms.CharField(required = True, widget = forms.Textarea(attrs={'class': 'comment_text'}))