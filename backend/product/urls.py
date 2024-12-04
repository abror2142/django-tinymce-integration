from django.urls import path
from .views import upload_image, create_product, product_list, update_product, product

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:pk>/', product, name="product"),
    path('<int:pk>/update-product/', update_product, name='update_product'),
    path('create-product/', create_product, name='create_product'),    
    path('upload-image/', upload_image, name='upload_image'), # TinyMCE upload function
]
