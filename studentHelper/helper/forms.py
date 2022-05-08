
from helper import models
from django import forms

#userData Form
class UserDataForm(forms.ModelForm):
    class Meta:
        model=models.UserData
        fields=['name','collage_name','type','email','mobile']
        labels={'name':'Full Name','collage_name':'collage name','type':'Type','email':'Email','mobile':'Mobile'}
        widgets={'type':forms.TextInput(attrs={'list':'items'})}
    def clean_mobile(self):
        value=self.cleaned_data['mobile']
        length=len(value)
        if length!=10:
            raise forms.ValidationError("Mobile Number should be 10 digits, Please Entered Correct Mobile No.")
        return value

#Notes Containig form
class NotesSubmission(forms.ModelForm):
    class Meta:
        model=models.Notes
        fields=['subject','notes_pdf']
        labels={'subject':'Subject','notes_pdf':'NotesPDF'}
        