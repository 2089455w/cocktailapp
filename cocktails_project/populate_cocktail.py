import os
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cocktails_project.settings')

import django
django.setup()

from cocktail.models import Cocktail, User

def addCocktail(name, image, rating, user_rated, how_to_make_comment, user_id, taste_pallet, views):
    c = Cocktail.objects.get_or_create(name=name,
                                       image = image,
                                       rating = rating,
                                       user_rated = user_rated,
                                       how_to_make_comment = how_to_make_comment,
                                       user_id = user_id,
                                       taste_pallet = taste_pallet,
                                       views = views)[0]
    return c

def addUser(name, email, age_range, sign_up_date, time_last_used, city, workplace):
    u = User.objects.get_or_create(name = name,
                                   email = email,
                                   age_range = age_range,
                                   sign_up_date = sign_up_date,
                                   time_last_used = time_last_used,
                                   city = city,
                                   workplace = workplace)[0]

def populate():
    u = addUser(name = "mckabanos",
                email = "thekabanos@gmail.com",
                age_range = "",
                sign_up_date = datetime.date.today(),
                time_last_used = datetime.date.today(),
                city = "Glasgow, UK",
                workplace = "Cova Bar")
    print "Egg ======== " + u
    addCocktail(name = "French Martini",
                image = "",
                rating = 0,
                user_rated = "",
                how_to_make_comment = "",
                user_id = u,
                taste_pallet = "",
                views = 0)
    #addCocktail("Vesper Martini", "", 0, "", "", u, "", 0)
    #addCocktail("Porn Star Martini", "", 0, "", "", u, "", 0)


    for u in User.objects.all():
        for c in Cocktail.objects.filter(user_id = u):
            print "- {0} - {1}".format(str(u), str(c))

if __name__ == '__main__':
    print "Starting Cocktail population script..."
    populate()