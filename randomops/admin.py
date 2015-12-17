from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Faction)
admin.site.register(Operator)
admin.site.register(Side)
admin.site.register(Weapon)
admin.site.register(Gadget)
