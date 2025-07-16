from django.db import models

# Create your models here.

class Post(models.Model): # POST Bhaneko many ho so foreignkey use gareko
    title = models.CharField(max_length= 255)
    content = models.TextField() # text wala field ma jati pani halna milxa
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE) # models.CASCADE = if superuser gets deleted then all the post gets deleted 
    created_at = models.DateTimeField(auto_now_add=True) # first creation ko bela time wala value basxa
    updated_at = models.DateTimeField(auto_now=True) # update garesi value time ko ni update hunxa
    published_at = models.DateTimeField(null=True,blank=True)  
    
    def __str__(self):
        return self.title

# published_at => data xaina => null value xa 
# published_at => data rakhne => data nai hunxa 

## 1-1 Relationship 
# 1 user can have only 1 profile => 1
# 1 profile is associated to only 1 user => 1
# OneToOneField() => Any model

## 1-M Relationship
# 1 user can add M post => M
# 1 post is associated to only 1 user => 1
# IN django use ForeignKey() => Use in many side model


# M-M Relationship
# 1 student can learn from M teachers => M
# 1 teacher can teach M students => M
# ManyToManyField() => Any place 