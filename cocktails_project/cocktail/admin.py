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

class CommentAdmin(admin.ModelAdmin):
    list_display = ( 'ID', 'user_id', 'cocktail_id', 'comment_title', 'comment_text' )

class BrandAdmin(admin.ModelAdmin):
    list_display = ( 'ID', 'brand_name' )

class AdvertAdmin(admin.ModelAdmin):
    list_display = ( 'ID', 'brand_id', 'advert_title', 'advert_image', 'date_added', 'date_added', 'date_to_expire' )

admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(CocktailTastePalette, CocktailTastePaletteAdmin)
admin.site.register(CocktailBase, CocktailBaseAdmin)

admin.site.register(Bartender, BartenderAdmin)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Advert, AdvertAdmin)



# Register your models here.
