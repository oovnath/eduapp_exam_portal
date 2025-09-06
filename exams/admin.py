from django.contrib import admin
from .models import ExamTable, QuestionTable
# Register your models here.
# admin.site.register(ExamTable)
@admin.register(ExamTable)
class ExamTableAdmin(admin.ModelAdmin):
    filter_horizontal = ('questionarray',) 

admin.site.register(QuestionTable)