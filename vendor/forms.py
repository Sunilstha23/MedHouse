from django import forms
from django.contrib.auth import authenticate, get_user_model
from .models import Vendor,VendorImage, User

user = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Enter your password'}))

    def clean(self):
        data = self.cleaned_data
        email  = data.get("email")
        password  = data.get("password")

        user = authenticate(email=email, password=password)

        if user is None:
            raise forms.ValidationError("Invalid credentials")

        return data


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('full_name', 'email', 'gender', 'address', 'dob', 'description','contact_number', 'pan_number', 'vat_number', 'shop_name', 'business_name')

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    GENDER_TYPES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    ]

    full_name        = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your full name'}))
    email            = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your email'}))
    address          = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your address'}))
    description      = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows':5, 'cols':20, 'class':'form-control','placeholder': 'Write about your pharmacy'}))
    gender           = forms.CharField(label='Gender', widget=forms.Select(choices=GENDER_TYPES,attrs={'class':'form-control','placeholder': 'Enter your gender'}))
    dob              = forms.DateField(label='Date Of Birth', widget=forms.TextInput(attrs={'class':'form-control datepicker' ,'placeholder': 'Enter your date of birth'}))
    contact_number   = forms.IntegerField(label='Contact Number', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your contact number'}))
    pan_number       = forms.CharField(label='PAN Number', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your PAN number'}))
    vat_number       = forms.CharField(label='VAT Number', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your VAT number'}))
    shop_name        = forms.CharField(label='Pharmacy Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your pharmacy name'}))
    business_name    = forms.CharField(label='Registered Business Name', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your registered business name'}))
    password         = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Enter your password'}))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Confirm password'}))

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password
    
    def clean_email(self):
          data = self.cleaned_data['email']
          if User.objects.filter(email=data).count() > 0:
              raise forms.ValidationError("We have a user with this user email-id")
          return data


class RegistrationImageForm(forms.ModelForm):
    class Meta:
        model = VendorImage
        fields = ('image',)
    image = forms.ImageField(required=False)
