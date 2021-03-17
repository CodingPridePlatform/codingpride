from django.contrib import admin
from .models import Question,QuestionLike

# Register your models here.
admin.site.register(Question)

class QuestionLikeAdmin(admin.ModelAdmin):
    list_display=('question','user')
admin.site.register(QuestionLike,QuestionLikeAdmin)