##Modles for cocktail website database, Ross Wilson & Georgios Kampanos


from django.db import models
from django.contrib.auth.models import User
import datetime

class Bartender(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, default = "")
    email = models.EmailField(max_length=75, unique = True, default = "")
    age_range = models.CharField(max_length=5, default = "")
    sign_up_date = models.DateField(auto_now=False,auto_now_add=True, default = datetime.date.today())
    time_last_used = models.DateTimeField(auto_now=True, auto_now_add=False, default = datetime.date.today())
    city = models.CharField(max_length = 64, default = "")
    workplace = models.CharField(max_length = 64, default = "")

    def __unicode__(self):
        return self.name

class CocktailTastePalette(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, default = "")

    def __unicode__(self):
        return self.name

class CocktailBase(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, default = "")

    def __unicode__(self):
        return self.name

class Cocktail(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, default = "")
    image = models.CharField(max_length=256, default = "")
    rating = models.SmallIntegerField(default = 0)
    user_rated = models.SmallIntegerField(default = 0)
    base = models.ForeignKey(CocktailBase)
    ingredients = models.CharField(max_length = 512, default = "")
    how_to_make_comment = models.CharField(max_length=256, default = "")
    bartender = models.ForeignKey(Bartender)
    taste_palette = models.ForeignKey(CocktailTastePalette)
    views = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    ID = models.AutoField(primary_key=True)
    '''user_id= models.ForeignKey(User)
    cocktail_id = models.ForeignKey(Cocktail)'''
    comment_text = models.CharField(max_length = 256)

    def __unicode__(self):
        return self.name

class Brand(models.Model):
    ID = models.AutoField(primary_key = True)
    brand_name = models.CharField(max_length = 64)

    def __unicode__(self):
        return self.brand_name


class Advert(models.Model):
    ID = models.AutoField(primary_key=True)
    '''brand_id = models.ForeignKey(Brand)
    image = models.CharField(max_length =256)
    date_added = models.DateField(auto_now = False, auto_now_add = True)
    date_to_expire = models.DateField()'''

    def __unicode__(self):
        return self.ID
    
