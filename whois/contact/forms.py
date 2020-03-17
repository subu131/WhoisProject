from django import forms
from .models import Contact




class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name','phone','email','domain','notes',)
        labels = {
            'name' : 'Full Name'
        }
        widgets = {
          'notes': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }

    def __init__(self,*args,**kwargs):
        super(ContactForm,self).__init__(*args,**kwargs) 
        self.fields['notes'].required = False
       # self.fields['notes'].widget.attrs['columns'] = 5
       # self.fields['notes'].widget.attrs['row'] = 10