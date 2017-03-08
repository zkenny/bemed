from django import forms

class ECForm(forms.Form):
    start_date = forms.DateField(help_text="Enter the date you started the activity.")

    # def clean_renewal_date(self):
    #     data = self.cleaned_data['renewal_date']
        
    #     #Check date is in the past. 
    #     if data > datetime.date.today():
    #         raise ValidationError(_('Invalid date - you cannot input activities you have not started yet'))

    #     # Remember to always return the cleaned data.
    #     return data