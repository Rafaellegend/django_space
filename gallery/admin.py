from django.contrib import admin

from gallery.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
  list_display = ("id", "name", "subtitle","public")
  list_display_links = ("id", "name")
  search_fields = ("name",)
  list_filter = ("category",)
  list_editable = ("public",)
  list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)