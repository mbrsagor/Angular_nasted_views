from django.forms import ModelForm, TextInput, FileInput, Select, CheckboxInput, EmailInput
from app.models.nomination import Symbol, Nomination


class SymbolForm(ModelForm):
    class Meta:
        model = Symbol
        fields = (
            '__all__'
        )
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'address'}),
            'image': FileInput(attrs={'class': 'custom-file-input', 'id': 'imageUpload'}),
        }


class NominationForm(ModelForm):
    model = Nomination
    exclude = ['user', 'user_id']
    fields = (
        '__all__'
    )
    widgets = {
        'qualification': TextInput(attrs={'class': 'form-control', 'id': 'qualification'}),
        'profession': TextInput(attrs={'class': 'form-control', 'id': 'profession'}),
        'eduction': TextInput(attrs={'class': 'form-control', 'id': 'eduction'}),
        'present_address': TextInput(attrs={'class': 'form-control', 'id': 'present_address'}),
        'phone_number': TextInput(attrs={'class': 'form-control', 'id': 'phone_number'}),
        'email_address': EmailInput(attrs={'class': 'form-control', 'id': 'email_address'}),
        'father_name': TextInput(attrs={'class': 'form-control', 'id': 'father_name'}),
        'mother_name': TextInput(attrs={'class': 'form-control', 'id': 'mother_name'}),
        'is_approve': CheckboxInput(attrs={'class': 'form-control', 'id': 'is_approve'}),
        'position': Select(attrs={'class': 'form-control', 'id': 'position'}),
        'symbol_name': Select(attrs={'class': 'form-control', 'id': 'symbol_name'}),
    }
