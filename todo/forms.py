from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    title = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(
                                attrs={
                                    "placeholder":"Enter Todo title",
                                    "class":"form-control",
                                    "autofocus": True
                                    }
                                )
                            )
    description = forms.CharField(required=False,
                            widget=forms.widgets.TextInput(
                                attrs={
                                    "placeholder":"Enter Todo description",
                                    "class":"form-control"
                                    }
                                )
                            )
    class Meta:
        model = Todo
        fields = ('title','description')
