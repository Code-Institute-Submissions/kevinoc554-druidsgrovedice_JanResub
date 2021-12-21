from django.shortcuts import render, redirect


def view_cart(request):
    """
    A view to return and display the contents of the user's shopping cart
    """
    return render(request, 'cart/shopping_cart.html')


def add_to_cart(request, item_id):
    """
    A view to add a specific quantity of an item to the shopping cart
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart

    return redirect(redirect_url)