# Django TinyMCE Integration using django-tinymce!

## About the Project:

This project integrates the WYSIWYG Editor - TinyMCE - to the Django project.

We can easily get WYSIWYG Editor using the [django-tinymce](https://django-tinymce.readthedocs.io/en/) library.

However, the challange (at least I faced) is to handle the image upload functions which are useful for storing content.

This Project includes features:
 - django-tinymce image upload functions
    - option for storing in Base64 encoded format
    - option for storing as a file in the media directory.
  - Image deletion after removing the image from the editor(during updates).

** I do not own anything in this repo. Thanks to people who write tutorials which I used extensively.

** Basically, I tried to connect them to test and use them for personal projects.

** FEEL FREE to give feedback :)

## How to RUN?

Steps to follow:
 1. **RENAME** the .env-developer to .env
 2. **POPULATE** .env file with correct values
 3. **MAKE** virtual env to avoid dependency conflicts
 4. **INSTALL** libraries in backend/requirements.txt file
 5. **ACTIVATE** environment
 6. **RUN** `python manage.py runserver`
 7. **GO TO** http://localhost:8000 to check the result
 8. **CHECK** admin page of the website using http://localhost:8000/admin/

## What to expect?

You will have a TinyMCE WYSIWYG editor working correctly(partly of course) inside Django Project.

You can explore `settings.py` for `django-tinymce` configuration

And you can  check the upload_image function inside the app-views which is used to manage image uploads in the TinyMCE editor.

Django Signal is used to delete unnecessary images programmatically(inside `signals.py`).

## Last but not least

Thank you. FEEL FREE to fork, pull a request or report an issue. 
Happy Coding :)
