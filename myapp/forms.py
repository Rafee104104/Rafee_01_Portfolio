from django import forms
from .models import *
from django.contrib.auth.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class LoginForm(AuthenticationForm):
    # username = forms.CharField(label='Username', widget=forms.TextInput(
    #     attrs={
    #         'class' : 'form-control',
    #         'placeholder' : 'Input Username'
    #     }
    # ))
    # password = forms.CharField(label='Password', widget=forms.PasswordInput(
    #     attrs={
    #         'class' : 'form-control',
    #         'placeholder' : 'Input Password'
    #     }
    # ))
    class Meta:
        model = CustomUser
        fields = ['username','password']
        # fields = ('__all__')

class RegistrationForm(UserCreationForm):
    # username = forms.CharField(label='Username', widget=forms.TextInput(
    #         attrs={
    #             'class' : 'form-control',
    #             'placeholder' : 'Input Username'
    #         }
    # ))
    # email = forms.CharField(label='Email', widget=forms.TextInput(
    #         attrs={
    #            'class' : 'form-control',
    #             'placeholder' : 'Input Email'
    #         }
    # ))
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
    #     attrs={
    #         'class' : 'form-control',
    #         'placeholder' : 'Input Password'
    #     }
    # ))
    # password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
    #     attrs={
    #         'class' : 'form-control',
    #         'placeholder' : 'Confirm Password'
    #     }
    # ))
    # user_type = forms.ChoiceField(choices = [
    #     ('','-Select an option-'),
    #     ('jobSeeker','JobSeeker'),
    #     ('jobRecruiter','JobRecruiter'),
    # ],widget = forms.Select(attrs={
    #     "class":"form-select w-50"
    # }))
    # user_type = forms.CharField(label='User Type', widget=forms.TextInput(
    #     attrs={
    #         'class' : 'form-control',
    #         'placeholder' : 'User Type'
    #     }
    # ))
    # display_name = forms.CharField(label='Display Name', widget=forms.TextInput(
    #     attrs={
    #         'class' : 'form-control',
    #         'placeholder' : 'Display Name'
    #     }
    # ))

    class Meta:
        model = CustomUser
        fields = ['username','email','password1','password2']
        # fields = ('__all__')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'title', 'email', 'phone', 'address','about','profile_image']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'percentage']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'start_year', 'end_year', 'result']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job_title', 'company', 'start_date', 'end_date', 'description']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies', 'project_url']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']