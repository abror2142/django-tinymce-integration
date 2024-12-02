from django.dispatch import receiver
from django.db.models.signals import pre_save

from .models import Product
from .utils import parse_image_path_from_html, delete_file


@receiver(pre_save, sender=Product)
def my_handler(sender, signal, instance, **kwargs):
    print("SIGNALLLLLL")
    # instance is what will be saved in the Database
    # product is the object before this saving
    if instance.pk is not None:
        product = Product.objects.get(pk=instance.pk)
        # things to be done to delete images that are deleted from editor:
            # make map of previous and instance image names:
            # compare them
            # delete if previos image list has items that are not present in the new one 
        prev_images = parse_image_path_from_html(product.desc)
        current_images = parse_image_path_from_html(instance.desc)
        for img_path in prev_images:
            if img_path not in current_images:
                img_path=img_path[1:] # removes first /
                delete_file(img_path)
    