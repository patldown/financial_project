from django.contrib import admin

# Register your models here.
### Let's admins utilize and edit the models

from .models import Question

admin.site.register(Question)