from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
            widget=forms.Textarea(
                attrs={'rows':5, 'placeholder':'What is on your mind ?'}
            ),
            max_length=4000,
            help_text='The maximum length of the message is 4000.'
        )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
    
    def __init__(self, *args, **kwargs):
        super(NewTopicForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs['placeholder'] = 'Your topic\'s subject.'