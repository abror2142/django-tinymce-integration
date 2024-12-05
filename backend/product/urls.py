from django.urls import path
from .views import upload_image, create_product, update_product, product, delete_product

urlpatterns = [
    path('<int:pk>/', product, name="product"),
    path('<int:pk>/update/', update_product, name='update_product'),
    path('create/', create_product, name='create_product'),    
    path('<int:pk>/delete/', delete_product, name='delete_product'),    
    path('upload-image/', upload_image, name='upload_image'), # TinyMCE upload function
]
