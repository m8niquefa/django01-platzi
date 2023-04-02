from django.contrib import admin
from .models import Question, Choice

# To each Choice, provide an extra form so that data can be entered inline with three answers per question:
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Register your models here. To make a model visible on the admin site, register the model with admin.site.register():
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    inlines = [ChoiceInline]

    #To see extra information in the django admin
    list_display = ("question_text", "pub_date", "was_published_recently")
    
    #To add filters to the admin page
    list_filter = ["pub_date"]

    #To add a search bar to the admin page
    search_fields = ["question_text"]



admin.site.register(Question, QuestionAdmin)
