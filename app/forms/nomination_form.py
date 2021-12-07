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
    class Meta:
        model = Nomination
        exclude = ['candidate', 'candidate_id']
        fields = [
            'qualification', 'profession', 'eduction', 'present_address', 'phone_number', 'email_address',
            'father_name', 'mother_name', 'is_approve', 'position', 'symbol_name', 'status', 'certificate_name'
        ]

        widgets = {
            'certificate_name': TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'certificate_name'}),
            'qualification': TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'qualification'}),
            'profession': TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'profession'}),
            'eduction': TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'eduction'}),
            'present_address': TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'present_address'}),
            'phone_number': TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'phone_number'}),
            'email_address': EmailInput(attrs={'class': 'form-control form-control-sm', 'id': 'email_address'}),
            'father_name': TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'father_name'}),
            'mother_name': TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'mother_name'}),
            'is_approve': CheckboxInput(attrs={'class': 'form-control form-control-sm', 'id': 'is_approve'}),
            'status': CheckboxInput(attrs={'class': 'form-control form-control-sm', 'id': 'status'}),
            'position': Select(attrs={'class': 'form-control form-control-sm', 'id': 'position'}),
            'symbol_name': Select(attrs={'class': 'form-control form-control-sm', 'id': 'symbol_name'}),
        }
