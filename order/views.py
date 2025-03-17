from django.shortcuts import get_object_or_404, render
from MainPage.models import food, wine, other_products

# Create your views here.
def order(request, type, id):
    if type == "food":
        product = get_object_or_404(food, id=id)
    elif type == "wine":
        product = get_object_or_404(wine, id=id)
    elif type == "other_products":
        product = get_object_or_404(other_products, id=id)
    else:
        product = None  # Handle invalid type

    return render(request, 'order.html', {'product': product, 'type': type})