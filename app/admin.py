from django.contrib import admin

from .models import Data

@admin.register(Data)
class InsightAdmin(admin.ModelAdmin):
    list_display = ('id','sector', 'topic', 'insight','region')
   