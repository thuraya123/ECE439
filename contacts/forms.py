from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'id_number', 'email', 'password']  # Add other fields

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        id_number = cleaned_data.get('id_number')
        email = cleaned_data.get('email')

        # Check if a contact with the same name, ID, or email already exists
        if Contact.objects.filter(name=name).exclude(id=self.instance.id).exists():
            self.add_error('name', 'A contact with this name already exists.')

        if Contact.objects.filter(id_number=id_number).exclude(id=self.instance.id).exists():
            self.add_error('id_number', 'A contact with this ID already exists.')

        if Contact.objects.filter(email=email).exclude(id=self.instance.id).exists():
            self.add_error('email', 'A contact with this email already exists.')
