from django import forms
from cpmeye.models import Submission, User


class UserForm(forms.ModelForm):
  username = forms.CharField(label="Username.")
  email = forms.CharField(label="Email.")
  password = forms.CharField(widget=forms.PasswordInput(), label="Password.")

  class Meta:
      model = User
      fields = ['username', 'email', 'password']


class SubmissionForm(forms.ModelForm):
    title = forms.CharField(max_length = 64)
    content = forms.CharField(max_length = 256)
    class Meta:
        model = Submission
        fields = ['title', 'content']
        
class VotingForm(forms.ModelForm):
  class Meta:
    model=Submission
