from django.contrib import admin
from .models import Address, WishListItem, WishList

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'street',
        'city',
        'post_code',
        'city',
        'country',
        'lat',
        'lng'
    )

class WishListItemInline(admin.TabularInline):
    model = WishListItem
    extra = 0
    fields = ('name', 'approved')
  
@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'address'
    )
    search_fields = (
        'name',
        'content',
        'email',
        'address__city'
    )
    readonly_fields = (
        "name", 
        "email",
        "content",
        "address"
    )
    list_filter = ('address__country', )
    inlines = [WishListItemInline]