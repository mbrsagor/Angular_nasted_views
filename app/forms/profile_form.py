from django.forms import ModelForm, TextInput, FileInput, NumberInput, DateInput, Select
from app.models.user import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'address', 'union', 'word_number', 'birth_date', 'gender', 'profile_picture'
        ]
        exclude = ['user', 'user_id']

        widgets = {
            'address': TextInput(attrs={'class': 'form-control', 'id': 'address'}),
            'union': TextInput(attrs={'class': 'form-control', 'id': 'union'}),
            'word_number': NumberInput(attrs={'class': 'form-control', 'id': 'word_number'}),
            'birth_date': DateInput(attrs={'class': 'form-control', 'id': 'birth_date', 'type': 'date'}),
            'gender': Select(attrs={'class': 'form-control', 'id': 'gender'}),
            'profile_picture': FileInput(attrs={'class': 'custom-file-input', 'id': 'imageUpload'}),
        }
