from django.contrib import admin

from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):

	list_display = ('question_text','course_name','appeared_date','appeared_marks','views',)

class AnswerAdmin(admin.ModelAdmin):

	list_display = ('question','views','likes','answerd_by')


admin.site.register(Question, QuestionAdmin) 
admin.site.register(Answer, AnswerAdmin)