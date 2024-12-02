from django.urls import path
from .views import upload_image, create_product, all_products, update_product, product

urlpatterns = [
    path('', all_products, name='all_products'),
    path('<int:pk>/', product, name="product"),
    path('<int:pk>/update-product/', update_product, name='update_product'),
    path('create-product/', create_product, name='create_product'),    
    path('upload-image/', upload_image, name='upload_image'),
]
