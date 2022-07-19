from django.contrib import admin
from .models import about
from .models import slider
from .models import whyus
from .models import whyusinfo
from .models import service
from .models import team
from .models import partner
from .models import bg
from .models import footerinfo
from .models import contactform






# Register your models here.
admin.site.register(about)
admin.site.register(slider)
admin.site.register(whyus)
admin.site.register(whyusinfo)
admin.site.register(service)
admin.site.register(team)
admin.site.register(partner)
admin.site.register(bg)
admin.site.register(footerinfo)
admin.site.register(contactform)