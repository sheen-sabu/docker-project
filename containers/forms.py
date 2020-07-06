from django import forms

class ContainerForm(forms.Form):
    tagname = forms.CharField(max_length=300)

    def clean(self):
        cleaned_data = super(ContainerForm, self).clean()
        tagname = cleaned_data.get('tagname')
        if not tagname:
            raise forms.ValidationError('You have to enter the docker tagname!')