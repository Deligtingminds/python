from django.test import TestCase

# Create your tests here.

#define class this will create the greeting
class Greeting(models.Model):
  #corrector field with a max length of 255
  message = models.CharField(max_length=255)  
