from django.contrib import admin
from survey.models import Question, QuestionDetail, Answer

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question']
    list_display = ('sort','idx', 'question', 'status')

class QuestionDetailAdmin(admin.ModelAdmin):
    search_fields = ['ans']
    list_display = ('question', 'ans')

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['num']
    list_display = ('question', 'num', 'etc')

admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionDetail, QuestionDetailAdmin)
admin.site.register(Answer, AnswerAdmin)
# admin.site.register(SurveyQuestion)
# admin.site.register(SurveyAnswer)