from django import forms

Price = (
            (1, '1'),
        (1000, '1000'),
        (3000, '3000'),
        (15000, '15000'),
)
class OrderForm(forms.Form):

    txnid = forms.CharField(widget = forms.HiddenInput())
    productinfo = forms.CharField(widget = forms.HiddenInput())
    amount = forms.ChoiceField(choices=Price)

    # buyer details
    firstname = forms.CharField()
    lastname = forms.CharField(required=False)
    email = forms.EmailField()
    phone = forms.RegexField(regex=r'\d{10}', min_length=10, max_length=10)
    address1 = forms.CharField(required=False,widget=forms.Textarea(attrs={"rows":3, "cols":20}))
    address2 = forms.CharField(required=False,widget=forms.Textarea(attrs={"rows":3, "cols":20}))
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    country = forms.CharField(required=False)
    zipcode = forms.RegexField(regex=r'\d{6}', min_length=6, max_length=6, required=False)

    txnid.widget.attrs.update({'class': 'form-control form-control-lg'})
    productinfo.widget.attrs.update({'class': 'form-control form-control-lg'})
    amount.widget.attrs.update({'class': 'form-control form-control-lg'})
    firstname.widget.attrs.update({'class': 'form-control form-control-lg'})
    lastname.widget.attrs.update({'class': 'form-control form-control-lg'})
    email.widget.attrs.update({'class': 'form-control form-control-lg'})
    phone.widget.attrs.update({'class': 'form-control form-control-lg'})
    address1.widget.attrs.update({'class': 'form-control form-control-lg'})
    address2.widget.attrs.update({'class': 'form-control form-control-lg'})
    city.widget.attrs.update({'class': 'form-control form-control-lg'})
    state.widget.attrs.update({'class': 'form-control form-control-lg'})
    country.widget.attrs.update({'class': 'form-control form-control-lg'})
    zipcode.widget.attrs.update({'class': 'form-control form-control-lg'})


