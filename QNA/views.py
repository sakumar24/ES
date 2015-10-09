from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse

from .models import Question,Answer

def index(request):

	return render(request,'QNA/index.html',[])

def show_all(request):

	questions = Question.objects.all()
	qa_dict = {}
	for que in questions:
		ans  = que.answer_set.order_by('likes')[0]

		qa_dict[que] = ans
		#print(que.question_text+ans.answer_text)
		
	context = {
		'qa_dict': qa_dict, 
	}
	
	return render(request,'QNA/show_all.html',context)


def detail(request, search_text):

	question = get_object_or_404(Question, question_text=search_text)
	
	context = {
		'question': question,
	}
	return render(request, 'QNA/detail.html', context)


def show_course(request, course):
	
	questions = get_list_or_404(Question, course_name=course)

	print(questions)
	context = {
		'questions': questions,
		'course': course,
	}
	return render(request, 'QNA/show_course.html', context)