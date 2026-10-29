from django.shortcuts import render


def home(request):
    products = [
        {"product": "Computer", "price": 3000},
        {"product": "Laptop", "price": 1500},
        {"product": "iPhone 17", "price": 3500},
        {"product": "mouse", "price": 100}

    ]

    return render(request, "products.html", {"products": products})
