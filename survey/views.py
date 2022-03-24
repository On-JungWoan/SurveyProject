from django.shortcuts import render, redirect
from .models import Question, QuestionDetail, Answer

def index(request):
    return render(request, 'survey/index.html')

def main(request, question_sort):
    question = Question.objects.filter(sort=question_sort)
    survey_list = question.order_by('idx')
    context = {'survey_list':survey_list}
    return render(request, 'survey/main.html', context)

def answer(request, question_sort):
    if request.method == 'POST':
        question = Question.objects.filter(sort=question_sort)[1]
        dto = Answer(question=question, num=request.POST.get('num'))
        dto.save()
        if (request.POST.get('num')=='1'):
            return redirect('survey:Detail', question_sort=question_sort)
        else:
            return redirect('survey:Next', question_sort=question_sort)

def Detail(request, question_sort):
    question = Question.objects.filter(sort=question_sort)
    survey_list = question.order_by('idx')
    context = {'survey_list': survey_list}
    return render(request, 'survey/ABDetail.html', context)

def Next(request, question_sort):
    if (question_sort=='D'):
        return render(request, 'survey/success.html')

    sort_list = ['A', 'B', 'C', 'D']
    idx = sort_list.index(question_sort)
    question_sort = sort_list[idx + 1]
    return redirect('survey:main', question_sort=question_sort)


def save_survey(request, question_sort):
    if request.method == 'POST':
        questions = Question.objects.filter(sort=question_sort)

        for question in questions:
            idx = str(question.idx)
            if idx == 0: continue
            nums = request.POST.getlist('num'+idx)

            for num in nums:
                dto = Answer(question=question, num=num)
                dto.save()

            etc = request.POST.getlist('etc'+idx)
            if etc:
                dto = Answer(question=question, num=0, etc=etc)
                dto.save()
    return redirect('survey:Next', question_sort=question_sort)