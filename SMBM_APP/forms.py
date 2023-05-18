from django import forms
from .import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomPasswordInput(forms.PasswordInput):
    def render(self, name, value, attrs=None, renderer=None):
        attrs['class'] = 'form-control'
        attrs['id']='password1'
        return super().render(name, value, attrs, renderer)

class CustomPasswordInput2(forms.PasswordInput):
    def render(self, name, value, attrs=None, renderer=None):
        attrs['class'] = 'form-control'
        attrs['id']='password2'
        return super().render(name, value, attrs, renderer)

class CustumerRegForm(UserCreationForm):
    password1 = forms.CharField(widget=CustomPasswordInput)
    password2 = forms.CharField(widget=CustomPasswordInput2)
    class Meta:
        model=User
        fields=('username','email','password1','password2')
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','id':'name'}),
            'email':forms.TextInput(attrs={'class':'form-control','id':'email'}),            
        }


class StuffRegForm(UserCreationForm):
    password1 = forms.CharField(widget=CustomPasswordInput)
    password2 = forms.CharField(widget=CustomPasswordInput2)
    class Meta:
        model=User
        fields=('username','email','password1','password2')
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','id':'name'}),
            'email':forms.TextInput(attrs={'class':'form-control','id':'email'}),
        }

    def save(self,commit=True):
        user=super().save(commit=False)
        user.is_staff=True
        if commit:
            user.save()
        return user
    

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback 
        fields=['feedback','user_id']
        widgets={
            'feedback':forms.Textarea(attrs={'class':'form-control',  'id':'feedback', 'placeholder':'Leave a feedback here'}),
            'user_id':forms.Select(attrs={'class':'form-control',  'id':'user_id','readonly': 'readonly'}),
        }
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = args[0]
        
        if instance:
            self.fields['user_id'].queryset = User.objects.filter(id=instance['user_id'])
        else:
            self.fields['user_id'].queryset = User.objects.all()

class SlotForm(forms.ModelForm):

    class Meta:

        model =  models.Slot

        fields = ['date','adult','concession','child']  

        widgets ={
             
            'date':forms.DateInput(attrs={'class':'form-control','id':'date','type':'date'}),
            'adult':forms.TextInput(attrs={'class':'form-control', 'id':'adultPrice', 'name':'adultPrice','type':'number'}),
            'concession':forms.TextInput(attrs={'class':'form-control', 'id':'concessionPrice', 'name':'adultPrice','type':'number'}),
            'child':forms.TextInput(attrs={'class':'form-control', 'id':'childPrice', 'name':'childPrice','type':'number'}),

        }         


class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None) 
        super().__init__(*args, **kwargs)
        try:
            self.fields['rewards_id'].queryset =models.Rewards.objects.filter(user_id=request)
   
        except:   
            self.fields['rewards_id'].queryset =models.Rewards.objects.filter(user_id=request.user)
   
    
    class Meta:
  
        
        # geeks_field = forms.MultipleChoiceField(choices = models.Rewards.objects.filter(user_id=request.user))
        fields='__all__'
        model=models.Booking
        fields ='__all__'
 
        widgets ={
            'type':forms.TextInput(attrs={'class':'form-control','id':'type','hidden':'true'}),
            'date':forms.DateInput(attrs={'class':'form-control','id':'date','type':'date','hidden':'true'}),
            'time':forms.TextInput(attrs={'class':'form-control','id':'time','hidden':'true'}),
            'adult':forms.TextInput(attrs={'class':'form-control', 'id':'adult', 'name':'adultPrice','type':'number','hidden':'true'}),
            'concession':forms.TextInput(attrs={'class':'form-control', 'id':'concession', 'name':'adultPrice','type':'number','hidden':'true'}),
            'child':forms.TextInput(attrs={'class':'form-control', 'id':'child', 'name':'childPrice','type':'number','hidden':'true'}),
            'special_request':forms.Textarea(attrs={'class':'form-control', 'id':'special_request', 'name':'special_request','rows':'4','required':False}),
            'user_id':forms.Select(attrs={'class':'form-control',  'id':'user_id','readonly': 'readonly','hidden':'true'}),
            'rewards_id':forms.SelectMultiple(attrs={'class':'form-control',  'id':'rewards_id','readonly': 'readonly'}),
            'slot_id':forms.Select(attrs={'class':'form-control',  'id':'slot_id','readonly': 'readonly','hidden':'true'}),
        } 

   