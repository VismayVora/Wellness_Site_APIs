from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class DietLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)

    Solid = 'S'
    Liquid = 'L'
    FOOD_TYPE_CHOICES = [(Solid,'Solid'),(Liquid,'Liquid')]
    food_type = models.CharField(max_length=2, choices = FOOD_TYPE_CHOICES, default = Solid )

    quantity = models.IntegerField()
    consumption_time = models.DateTimeField(null = True, blank = True)
    calories = models.DecimalField(max_digits=6, decimal_places=3)
    notes = models.TextField(max_length = 300, null = True, blank = True)
    owner = models.ForeignKey(
        'accounts.User', related_name='DietLog', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
    
    def save(self, *args, **kwargs):
        super(DietLog, self).save(*args, **kwargs)

class WorkoutLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)

    duration = models.IntegerField()
    workout_time = models.DateTimeField(null = True, blank = True)
    notes = models.TextField(max_length = 300, null = True, blank = True)
    owner = models.ForeignKey(
        'accounts.User', related_name='WorkoutLog', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
    
    def save(self, *args, **kwargs):
        super(WorkoutLog, self).save(*args, **kwargs)

class HealthData(models.Model):
    owner = models.OneToOneField(
        'accounts.User', related_name='HealthData', on_delete=models.CASCADE, primary_key = True)  #Can I also use PrimaryKeyRelatedField over here?
    height = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=5,decimal_places=2)
    age = models.IntegerField()
    gender = models.CharField(max_length=2,choices=[('M','Male'),('F','Female')], blank=True)

'''
class Task_Category(models.Model):
	owner = models.ForeignKey(User,on_delete = models.CASCADE)
	title = models.CharField(max_length = 50)
	description = models.TextField(blank = True)
	
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = ("Category")
		verbose_name_plural = ("Categories")

class Task(models.Model):
	owner = models.ForeignKey(User, on_delete = models.CASCADE)
	category = models.ForeignKey(Task_Category,null=True,on_delete = models.SET_NULL)
	title = models.CharField(max_length = 50)
	description = models.TextField(blank = True)
	priority_no = models.PositiveIntegerField(blank = True)
	status = models.BooleanField(default=False,blank = True)
	duedate = models.DateTimeField(blank = True)
	
	def __str__(self):
		return self.title

	class Meta:
		ordering = ['status']
'''




    

