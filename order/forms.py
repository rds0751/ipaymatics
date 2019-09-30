from django import forms

Price = (
            (102, '₹ 100'),
            (510, '₹ 500'),
        (1020, '₹ 1000'),
        (2040, '₹ 2000'),
        (5100, '₹ 5000'),
        (10200, '₹ 10000'),
)
class OrderForm(forms.Form):

    txnid = forms.CharField(widget = forms.HiddenInput())
    productinfo = forms.CharField(widget = forms.HiddenInput())
    amount = forms.ChoiceField(choices=Price)

    # buyer details
    firstname = forms.CharField(required=False,widget = forms.HiddenInput())
    lastname = forms.CharField(required=False, widget = forms.HiddenInput())
    email = forms.EmailField(required=False,widget = forms.HiddenInput())
    phone = forms.RegexField(regex=r'\d{10}', min_length=10, max_length=10)
    address1 = forms.CharField(required=False,widget=forms.Textarea(attrs={"rows":3, "cols":20}))
    address2 = forms.CharField(required=False, widget = forms.HiddenInput())
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


