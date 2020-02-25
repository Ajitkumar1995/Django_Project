from django import forms

class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
    #Explicitly by the programmer by using clean methods
    def clean_name(self):
        inputname=self.cleaned_data(['name'])
        if len(inputname)<4:
            raise forms.ValidationError('The minimum no of charcater in the name field should be 4')
        return inputname
    def clean_rollno(self):
        inputrollno=self.cleaned_data['rollno']
        print('Validating roll no field')
        return inputrollno
    def clean_email(self):
        inputemail=self.cleaned_data['email']
        print('validating email field')
        return inputemail
    def clean_feedback(self):
        inputfeedback=self.cleaned_data['feedback']
        print('Validating feedback field')
        return inputfeedback

#django's inbuilt core validators
'''
from django.core import validators
class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
'''

#How to check original pwd and reentered pwd are same or not
'''
from django import forms
from django.core import validators

class FeedBackForm(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Re-Enter password',widget=forms.PasswordInput)
    rollno=forms.IntegerField()
    email=forms.EmialField()
    feedback=forms.CharField(widget=forms.Textarea)
    
    def clean(self):
        print('validating password match')
        total_cleaned_data=super().clean()
        fpwd=total_cleaned_data['password']
        spwd=total_cleaned_data['rpassword']
        if fpwd!=spwd:
            raise forms.ValidationError('Both password must be matched')
'''