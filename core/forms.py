from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from image.models import Image, Comment
# from core.models import Feedback
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Fieldset, Field, ButtonHolder, Submit, Div
# from crispy_forms.bootstrap import PrependedAppendedText


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username')


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = [
#             'anonymous',
#             'content',
#             'rate_management',
#             'rate_security',
#             'rate_environment',
#             'rate_price',
#             'rate_convenience'
#         ]

class ProfileUpdateForm(forms.Form):
    email = forms.EmailField()
    phone = forms.IntegerField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    image = forms.ImageField()
    city = forms.CharField(required=False)
    state = forms.CharField(required=False, label='State/Province')
    country = forms.CharField(required=False)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Fieldset(
#                 '',
#                 Field('email'),
#                 Field('phone'),
#                 Div(
#                     Div(
#                         Field('first_name'),
#                         css_class='form-group col-md-4'
#                     ),
#                     Div(
#                         Field('last_name'),
#                         css_class='form-group col-md-4'
#                     ),
#                     Div(
#                         Field('image'),
#                         css_class='form-group col-md-4'
#                     ),
#                     css_class='form-row'
#                 ),
#                 Div(
#                     Div(
#                         Field('city'),
#                         css_class='form-group col-md-4'
#                     ),
#                     Div(
#                         Field('state'),
#                         css_class='form-group col-md-4'
#                     ),
#                     Div(
#                         Field('country'),
#                         css_class='form-group col-md-4'
#                     ),
#                     css_class='form-row'
#                 ),
#             ),
#             ButtonHolder(
#                 Submit('submit', 'Update', css_class='btn btn-primary')
#             )
#         )

