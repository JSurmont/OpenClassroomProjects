from django.contrib import admin
from django.contrib import admin
from listings.models import Band, Listing


class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre',)  # liste les champs que nous voulons sur l'affichage de la liste


admin.site.register(Band, BandAdmin)  # nous modifions cette ligne, en ajoutant un deuxième argument


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'band', 'year', 'sold',)


admin.site.register(Listing, ListingAdmin)
