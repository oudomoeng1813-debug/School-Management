from django import forms
from .models import Student, Subject, Teacher

# Optional: Define gender choices once and reuse them
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class StudentForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select rounded-pill',
        })
    )

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'dob': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control rounded-pill'
            }),
            'address': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
        }


class TeacherForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select rounded-pill',
        })
    )

    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'dob': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control rounded-pill'
            }),
            'address': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
        }
