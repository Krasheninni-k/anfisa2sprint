from django.contrib import admin

from .models import Category, Topping, Wrapper, IceCream
admin.site.register(Topping)
admin.site.register(Wrapper)

class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'price',
        'output_order',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
        'price',
        'output_order'
    )    
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)

admin.site.register(IceCream, IceCreamAdmin)

admin.site.empty_value_display = 'Пусто'

class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',        
    )

admin.site.register(Category, CategoryAdmin)
