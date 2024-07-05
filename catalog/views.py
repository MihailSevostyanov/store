from django.shortcuts import render

from catalog.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'product_list.html', context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)



def contacts(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    print(f'{name} {phone} {message}')
    return render(request, 'contacts.html')
