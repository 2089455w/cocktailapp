from django.contrib import admin

from cocktail.models import Bartender, Cocktail, Comment, Brand, Advert, CocktailTastePalette, CocktailBase

class BartenderAdmin(admin.ModelAdmin):
    list_display = ( 'ID', 'name', 'email', 'age_range', 'workplace', 'city', 'time_last_used', 'sign_up_date' )

class CocktailAdmin(admin.ModelAdmin):
    list_display = ( 'ID', 'name', 'image', 'rating', 'user_rated', 'base', 'ingredients', 'how_to_make_comment', 'bartender', 'taste_palette', 'views' )

class CocktailTastePaletteAdmin(admin.ModelAdmin):
    list_display = ( 'ID', 'name', )

class CocktailBaseAdmin(admin.ModelAdmin):
    list_display = ( 'ID', 'name', )


admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(CocktailTastePalette, CocktailTastePaletteAdmin)
admin.site.register(CocktailBase, CocktailBaseAdmin)

admin.site.register(Bartender, BartenderAdmin)

admin.site.register(Comment)
admin.site.register(Brand)
admin.site.register(Advert)



# Register your models here.
