from django.db import models
<<<<<<< HEAD
from django.conf import settings

# Create your models here.
# model for the calendar event
class calendarEvent(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_name = models.CharField(max_length= 100, null= False)
    event_time = models.TimeField((u"event Time"), auto_now_add=True, blank=True)
    event_location = models.CharField(max_length = 1000, null= False)

=======
#from django.contrib.auth.models import User
#from PIL import Image

# Create your models here.
#start of stuff to add images
#class Catagory(models.Model):
   # cname = models.CharField(max_length =200)
  #  purdate = models.DateTimeField('purchase-date')
 #   createdby = models.ForeignKey(User)

#class Product (models.Mode):
 #  pname = models.CharField(max_length=200)    
 #  discription = models.CharField(max_length=500)
 #  pirce = models.IntegerField()
 #  noitem = models.IntegerField()
 #   createdby = models.ForeignKey(User)
 #   cid = models.ImageField(upload_to='photo')

#class Cart(modles.Mode):
#    uid = models.ForeignKey(User)
#    pid = models.ForeignKey(Product)
#    noitem = models.IntegerField()
#   purdate = models.DateTimeField("purchase-date")
#    deldate = models.DateTimeField("delivary-date")
#end of stuff to add images
>>>>>>> f254549c67e7c115b7fa609e33952fd7d39fd353
