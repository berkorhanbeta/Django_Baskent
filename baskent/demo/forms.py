from django import forms

# Our class structure for Form page.
# We can add a form in more than one HTML file with a single code.
class createMessage(forms.Form):
    fullName = forms.CharField(label="Full Name")
    mailAddress = forms.CharField(label="E-Mail Address")
    uMessage = forms.CharField(label="Your Message")