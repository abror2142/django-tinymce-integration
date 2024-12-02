from django.shortcuts import get_object_or_404, render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from django.db.models.signals import pre_save, post_save
import os
import uuid
from .forms import ProductForm
from .models import Product


def all_products(request):
    state = {
        'products': Product.objects.all(),
    }
    return render(request, 'products.html', state)


def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved!")
    state = {
        "form": form
    }
    return render(request, 'create-product.html', state)


def update_product(request, pk):
    instance = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponse("Updated!")
    return render(request, 'update-product.html', {'form': form})


def product(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "product.html", {"product": product})


@csrf_exempt
def upload_image(request, pk=None):
    if request.method != "POST":
        return JsonResponse({'Error Message': "Wrong request"})


    # If it's not series and not article, handle it differently
    file_obj = request.FILES['file']

    file_name_suffix = file_obj.name.split(".")[-1]
    if file_name_suffix not in ["avif", "jpg", "png", "gif", "jpeg"]:
        return JsonResponse({"Error Message": f"Wrong file suffix ({file_name_suffix}), supported are .jpg, .png, .gif, .jpeg"})

    # Generating uuid for image name
    id = uuid.uuid4()
    file_obj.name = str(id) + "." + file_name_suffix

    # Creating /media/product folder
    if not os.path.exists(settings.MEDIA_ROOT):
        os.mkdir(settings.MEDIA_ROOT)
        if not os.path.exists(os.path.join(settings.MEDIA_ROOT, 'product')):
            os.mkdir(os.path.join(settings.MEDIA_ROOT, 'product'))

    file_path = os.path.join(settings.MEDIA_ROOT, 'product', file_obj.name)

    with open(file_path, 'wb+') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)

        return JsonResponse({
            'message': 'Image uploaded successfully',
            'location': os.path.join(settings.MEDIA_URL, 'product', file_obj.name)
        })