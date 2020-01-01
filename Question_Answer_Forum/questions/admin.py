from django.contrib import admin
from .models import Question, Answer
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Question)
admin.site.register(Answer)