from django.contrib import admin
from django.contrib.auth.models import Group

from accounts.forms import UserForm
from accounts.models import User, Category, Commodity, Shop, Feature


class FavouriteInline(admin.TabularInline):
    model = User.favourites.through
    verbose_name = 'کالا های مورد علاقه'
    verbose_name_plural = 'کالا های مورد علاقه'
    extra = 0


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    form = UserForm
    inlines = [FavouriteInline]


class ShopInline(admin.TabularInline):
    model = Commodity.shops.through
    verbose_name = 'فروشنده'
    verbose_name_plural = 'فروشنده'
    extra = 0


class FeatureInline(admin.TabularInline):
    model = Commodity.features.through
    verbose_name = 'ویژگی'
    verbose_name_plural = 'ویژگی'
    extra = 0


class CommodityAdmin(admin.ModelAdmin):
    inlines = [ShopInline, FeatureInline]
    exclude = ('shops', 'features')


# admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Commodity, CommodityAdmin)
admin.site.register(Shop)
admin.site.register(Feature)
