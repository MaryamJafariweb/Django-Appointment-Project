from django import forms


class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=0, max_value=9)


class CouponApplyForm(forms.Form):
    code = forms.CharField()
