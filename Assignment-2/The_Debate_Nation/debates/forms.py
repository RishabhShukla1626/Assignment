from django import forms
from .models import Debates, Arguments

class PostForm(forms.ModelForm):

    class Meta():
        model = Debates
        fields = ('debate_title', 'description', 'vote_total', 'vote_ratio')
    
class ArgumentsForm(forms.ModelForm):

    class Meta():
        model = Arguments
        fields = ('argument', 'opinion', )