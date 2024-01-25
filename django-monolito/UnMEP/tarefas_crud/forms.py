from django import forms
from .models import Tarefa

class Tarefa_form(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo','data','status','descrição']
        
    # class Meta:
    #     titulo = forms.fields.CharField(
    #         max_length=200,
    #         empty_value='Titulo da tarefa',
    #         label="titulo"
    #     )
    #     data_field = forms.fields.DateField(widget = AdminDateWidget)
    #     status = forms.fields.ChoiceField()