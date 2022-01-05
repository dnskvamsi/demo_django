from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Payment
from .models import Customer
from django.db.models import F
import decimal
from django.db import transaction


def process_payment(request):

    if request.method == "POST":

        form = Payment(request.POST)

        if form.is_valid():
            x = form.cleaned_data["payor"]
            y = form.cleaned_data["payee"]
            z = decimal.Decimal(form.cleaned_data["amount"])

            payor = Customer.objects.select_for_update().get(name=x)
            payee = Customer.objects.select_for_update().get(name=y)

        with transaction.atomic():
            payor.balance -= z
            payor.save()

            payee.balance += z
            payee.save()

            return HttpResponseRedirect("/")

    else:
        form = Payment()

    return render(request, "index.html", {"form": form})
