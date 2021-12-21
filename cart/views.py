from django.shortcuts import render, redirect, reverse, HttpResponse


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


def adjust_cart(request, item_id):
    """
    Adjust the contents of the shopping cart
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    Remove an item from the shopping cart
    """
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        request.session['cart'] = cart

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
