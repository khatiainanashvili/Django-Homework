from django.contrib import admin # type: ignore
from .models import Birds
# Register your models here.

admin.site.register(Birds)