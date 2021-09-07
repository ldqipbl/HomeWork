from django.shortcuts import render
from .forms.dz_app.forms import New_prodact_form
from .models import Prodacts_info


def prodact(request):
    model_prodacts_info = Prodacts_info.objects.all()

    text = {
        "model":model_prodacts_info
    }
    
    return render(request, "dz_app/goods_list.html", text)


def create_new_prodact(request):
    if request.method == "POST":
        form = New_prodact_form(request.POST)
        if form.is_valid():
            Prodacts_info.objects.create(**form.cleaned_data)
    else:
        form = New_prodact_form()

    text = {
        "form":form
    }

    return render(request, "dz_app/good_create.html", text)
