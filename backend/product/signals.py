from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete

from .models import Product
from .utils import parse_image_path_from_html, delete_file


@receiver(pre_save, sender=Product)
def my_handler(instance, **kwargs):
    """
        instance - is what will be saved in the Database
        product - is the object before being saved (updated)

        Things to be done to delete images that are deleted from editor:
            * make map of product and instance image names
            * compare them (considering image names are unique)
            * delete if product image list contains image sources 
                that are not present in the new instance
    """
    if instance.pk is not None:
        product = Product.objects.get(pk=instance.pk)
        prev_images = parse_image_path_from_html(product.description)
        current_images = parse_image_path_from_html(instance.description)
        for img_path in prev_images:
            if img_path not in current_images:
                img_path=img_path[1:] # removes first /
                delete_file(img_path)


@receiver(post_delete, sender=Product)
def product_image_delete(origin, **kwargs):
    """
        origin is the product which has been deleted from database
        ** Deleting object doesn't delete image files associated with that

        Things to be done to clear the image files:
            * Make list of object's image src
            * Delete them one by one.
    """
    images = parse_image_path_from_html(origin.description)
    print(images)
    for img_path in images:
        img_path = img_path[1:]
        delete_file(img_path)
    

    