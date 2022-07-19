from django.contrib import admin
from .models import hero
from .models import heroabout
from .models import about
from .models import herosec
from .models import fleetmap
from .models import iridummap
from .models import shipdetail
from .models import client

# Register your models here.
admin.site.register(hero)
admin.site.register(heroabout)
admin.site.register(about)
admin.site.register(herosec)
admin.site.register(fleetmap)
admin.site.register(iridummap)
admin.site.register(shipdetail)
admin.site.register(client)