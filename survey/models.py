from django.db import models

class Question(models.Model):
    sort = models.CharField(max_length=1)
    idx = models.IntegerField()
    question = models.TextField(null=True)
    status = models.CharField(max_length=1, default='y')

    def __str__(self):
        return self.question


class QuestionDetail(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans = models.TextField(null=True)



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    num = models.IntegerField()
    etc = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.num

# class Answer(models.Model):
#     # 응답 아이디
#     answer_idx = models.AutoField(primary_key=True)
#
#     # 설문 아이디
#     survey_idx = models.IntegerField()
#
#     # 응답 번호
#     survey_index = models.IntegerField()