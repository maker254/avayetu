from django import forms
from production.models import Customer,GenealogyFile


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
    
    name = forms.CharField(widget=forms.TextInput({
        'placeholder':'Customer Name',
        'style':"border: 0.5px solid #464c53!important; height: 1.8rem !important; border-radius: 0.2rem !important;"
        }))

class GenealogyUploadForm(forms.ModelForm):
    class Meta:
        model = GenealogyFile
        fields = "__all__"