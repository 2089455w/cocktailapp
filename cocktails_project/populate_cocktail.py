import os
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cocktails_project.settings')

import django
django.setup()

from cocktail.models import Cocktail, User

def addCocktail(name, image, rating, user_rated, how_to_make_comment, user_id, taste_palette, views):
    c = Cocktail.objects.get_or_create(name=name,
                                       image = image,
                                       rating = rating,
                                       user_rated = user_rated,
                                       how_to_make_comment = how_to_make_comment,
                                       user_id = user_id,
                                       taste_palette = taste_palette,
                                       views = views)[0]
    return c

def addUser(name, email, age_range, sign_up_date, time_last_used, city, workplace, fave_cocktail):
    u = User.objects.get_or_create(name = name,
                                   email = email,
                                   age_range = age_range,
                                   sign_up_date = sign_up_date,
                                   time_last_used = time_last_used,
                                   city = city,
                                   workplace = workplace,
                                   fave_cocktail = fave_cocktail)[0]

def populate():
    u = addUser(name = "mckabanos",
                email = "thekabanos@gmail.com",
                age_range = "",
                sign_up_date = datetime.date.today(),
                time_last_used = datetime.date.today(),
                city = "Glasgow, UK",
                workplace = "Cova Bar"
                fave_cocktail = "White russian"
                )
    print "Egg ======== " + u
    addCocktail(name = "French Martini",
                image = "",
                rating = 0,
                user_rated = 3,
                how_to_make_comment = "",
                user_id = u,
                taste_palette = 2,
                views = 0)
    #addCocktail("Vesper Martini", "", 0, "", "", u, "", 0)
    #addCocktail("Porn Star Martini", "", 0, "", "", u, "", 0)


    for u in User.objects.all():
        for c in Cocktail.objects.filter(user_id = u):
            print "- {0} - {1}".format(str(u), str(c))

if __name__ == '__main__':
    print "Starting Cocktail population script..."
    populate()
