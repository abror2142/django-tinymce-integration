from django.shortcuts import get_object_or_404, redirect, render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from http import HTTPStatus
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from django.db.models.signals import pre_save, post_save
import os
import uuid
from .forms import ProductForm
from .models import Product


def product_list(request: HttpRequest):
    products = Product.objects.all(),
    return render(request, 'product-list.html', {"products": products})


def product(request: HttpRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product.html", {"product": product})


def create_product(request: HttpRequest):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    state = {
        "form": form,
        "button_text": "Add",
        "title": "Add a product"
    }
    return render(request, 'product-form.html', state)


def update_product(request: HttpRequest, pk: int):
    instance = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('index')
    state = {
        "form": form,
        "button_text": "Update",
        "title": "Update a product"
    }
    return render(request, 'product-form.html', state)


def delete_product(request: HttpRequest, pk: int) -> HttpResponse:
    instance = get_object_or_404(Product, pk=pk)
    instance.delete()
    return redirect('index')


@csrf_exempt
def upload_image(request):
    if request.method != "POST":
        return JsonResponse({'Error Message': "Wrong request"})
    
    file_obj = request.FILES['file']

    file_name_suffix = file_obj.name.split(".")[-1]
    if file_name_suffix not in ["avif", "jpg", "png", "gif", "jpeg"]:
        return JsonResponse({"Error Message": f"Wrong file suffix ({file_name_suffix}), supported are .jpg, .png, .gif, .jpeg"})

    # Generating uuid for image name
    id = uuid.uuid4()
    file_obj.name = str(id) + "." + file_name_suffix

    path = os.path.join(settings.MEDIA_ROOT, 'product')

    # Creating /media/product folder if it doesn't exist
    if not os.path.exists(path):
        os.makedirs(path)

    file_path = os.path.join(path, file_obj.name)

    file_url = f'{settings.MEDIA_URL}/product/{file_obj.name}'

    with open(file_path, 'wb+') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)

        return JsonResponse({
            'message': 'Image uploaded successfully',
            'location': file_url
        })