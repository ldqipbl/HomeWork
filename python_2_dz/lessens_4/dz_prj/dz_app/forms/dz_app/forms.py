from django import forms


class New_prodact_form(forms.Form):
    title = forms.CharField(
        label='Название продукта',
        max_length=50
    )

    created_at = forms.DateTimeField(
        label='Дата доставки',
        initial='0000-00-00'
    )

    price = forms.IntegerField(
        label='Цена',
        initial=0
    )

    count = forms.IntegerField(
        label='Колличество',
        initial=0
    )

    vendor = forms.CharField(
        label='Поставщик',
        max_length=100
    )

