from django.contrib import admin # type: ignore
from .models import Birds, Country, User
# Register your models here.

admin.site.register(Birds)
admin.site.register(Country)
admin.site.register(User)
