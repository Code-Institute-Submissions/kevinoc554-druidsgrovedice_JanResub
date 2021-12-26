from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """
    A view to render the checkout form
    """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'The shopping cart is empty')
        return redirect(reverse('products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
    }

    return render(request, 'checkout/checkout.html', context)
