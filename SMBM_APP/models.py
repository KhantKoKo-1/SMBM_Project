from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Point(models.Model):

    current_point =models.IntegerField()
    used_point = models.IntegerField()
    user_id = models.OneToOneField( User,on_delete=models.CASCADE)


class Feedback(models.Model):
     
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True,null=True) 
     

class Rewards(models.Model):

    rewards = models.CharField(max_length=50)  
    status = models.BooleanField(default=True)  
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.rewards
    


class Slot(models.Model):
    
    type = models.CharField(max_length=20,null=True)
    adult = models.IntegerField()
    child = models.IntegerField()
    concession = models.IntegerField()   
    date = models.DateField(auto_now=False, auto_now_add=False,unique=True)
    avalible = models.BooleanField(default=True)
    am_10=models.IntegerField(default=10)
    am_11=models.IntegerField(default=10)
    pm_2=models.IntegerField(default=10)
    pm_3=models.IntegerField(default=10)
    pm_4=models.IntegerField(default=10)

class Booking(models.Model):
    
    type = models.CharField(max_length=20,null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)    
    time = models.CharField(max_length=200)
    adult = models.IntegerField()
    concession = models.IntegerField()
    child = models.IntegerField()
    special_request = models.CharField(max_length=300,null=True,blank=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    rewards_id = models.ManyToManyField(Rewards,null=True,default=None,blank=True)
    slot_id = models.ForeignKey(Slot,on_delete=models.CASCADE)
   

class Chat(models.Model):
    
    message = models.CharField(max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    from_user=models.CharField(max_length=500,null=True)