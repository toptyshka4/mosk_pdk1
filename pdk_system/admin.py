from django.contrib import admin
from .models import Depo, Train, Wagon, TrainWagon, Remark

admin.site.register(Depo)
admin.site.register(Train)
admin.site.register(Wagon)
admin.site.register(TrainWagon)
admin.site.register(Remark)
