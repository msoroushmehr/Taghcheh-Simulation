from datetime import datetime
from enum import auto
from pyexpat import model
from tabnanny import verbose
from time import timezone
from timeit import default_timer
from django import forms
from .models import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import User
from django.template import loader
from django.core.mail import EmailMultiAlternatives
import random 
from random import randint, randrange
from .widgets import BootstrapDateTimePickerInput

# class DateForm(forms.Form):
#     date = forms.DateTimeField(
#         input_formats=['%d/%m/%Y %H:%M'], 
#         widget=BootstrapDateTimePickerInput()
#     )


class SignupForm(forms.ModelForm):
    email = forms.EmailField(label="ایمیل", max_length=300)


    class Meta:
        model = User
        fields = ('email', )
 
 
 
class FinalForm(forms.ModelForm):
    username = forms.CharField(label="نام کاربری", max_length=300, help_text=None)
    # password = forms.CharField(max_length=4, widget = forms.Textarea(
    #     attrs = {
    #         'hidden': '',
    #     }
    # ))
    def __init__(self, *args, **kwargs):
        super(FinalForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "نام کاربری"
        # self.fields['password'].widget = forms.HiddenInput()
        
    class Meta:
        model = User
        fields = ('username',)
        # widgets = {
        #     'password': forms.HiddenInput(),
        # }

        # help_texts = {
        #     'username': None
        # }

 
        

class SignuppForm(forms.Form):
    passs = forms.CharField(max_length=4, label='')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['passs'].initial = ''





class TestFormm(forms.Form):
    test_f = forms.CharField(max_length=4, label='')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')




class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
        
        
        
    )

    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):
        """
        Send a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = "".join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, "text/html")

        email_message.send()

    def get_users(self, email):
        """Given an email, return matching user(s) who should receive a reset.

        This allows subclasses to more easily customize the default policies
        that prevent inactive users and users with unusable passwords from
        resetting their password.
        """
        
    
        

    def save(
        self,
        domain_override=None,
        subject_template_name="فعالسازی حساب طاقچه",
        email_template_name="emailre.html",
        use_https=False,
        from_email=None,
        request=None,
        html_email_template_name=None,
        extra_email_context=None,
    ):
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        email = self.cleaned_data["email"]
        
        for user in self.get_users(email):
            user_email = getattr(user, email)
            context = {
                "email": user_email,
               
                **(extra_email_context or {}),
            }
            self.send_mail(
                subject_template_name,
                email_template_name,
                context,
                from_email,
                user_email,
                html_email_template_name=html_email_template_name,
            )




DISPLAY_CHOICES = (
    ("locationbox", "خریداری می کنم"),
    ("displaybox", "خرید را لغو می کنم")
)

class MyForm(forms.Form):
    display_type = forms.ChoiceField(widget=forms.RadioSelect, choices=DISPLAY_CHOICES, label='', error_messages={'required': 'یکی از گزینه ها را انتخاب کنید'})
    
    

INFINITY_CHOICES = (
    ('1', 100000),
    ('2'
     , 200000),
    ('3', 500000)
)    
    
class InfinityForm(forms.Form):
    infinity_type = forms.ChoiceField(widget=forms.RadioSelect, choices=INFINITY_CHOICES, label='')
    
    
    
