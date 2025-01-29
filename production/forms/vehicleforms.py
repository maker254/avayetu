from django import forms
from production.models import Vehicle,EOL


class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"
    
class EOLCreateForm(forms.ModelForm):
    class Meta:
        model = EOL
        fields = "__all__"