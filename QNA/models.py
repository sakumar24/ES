from django.db import models

class Question(models.Model):
	
	question_text = models.TextField(max_length=500)
	course_name = models.CharField(max_length=80)
	views = models.IntegerField(default=0)
	important_votes = models.IntegerField(default=0)
	asked_by = models.CharField(max_length=20,blank=True)
	posted_date = models.DateField(auto_now_add=True)
	appeared_date = models.DateField(blank=True,null=True)
	appeared_marks = models.FloatField(blank=True,null=True)

	def __str__(self):
		return self.question_text

	class Meta:
		ordering = ('course_name',)


# class Appeared(models.Model):

# 	question = models.ForeignKey(Question)
# 	#question = models.ManyToManyField(Question)
# 	appeared_date = models.DateField()
# 	appeared_marks = models.FloatField()

# 	def __str__(self):
# 		return "Date: "+str(self.appeared_date)+" Marks: "+str(self.appeared_marks)

# 	class Meta:
# 		ordering = ('appeared_date','appeared_marks')


class Answer(models.Model):

	question = models.ForeignKey(Question)
	answer_text = models.TextField(max_length=1500)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)
	answerd_by = models.CharField(max_length=20,blank=False)
	answerd_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.answer_text

	class Meta:
		order_with_respect_to = 'question'

# python manage.py makemigrations QNA
# python manage.py sqlmigrate QNA 0001
# python manage.py migrate