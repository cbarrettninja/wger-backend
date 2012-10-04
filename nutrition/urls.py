from django.conf.urls import patterns, include, url

urlpatterns = patterns('nutrition.views',
    url(r'^nutrition/overview/$', 'overview'),
    
    # Plans
    url(r'^nutrition/add/$', 'add'),
    url(r'^nutrition/(?P<id>\d+)/view/$', 'view'),    
    url(r'^nutrition/(?P<id>\d+)/delete/$', 'delete_plan'),
    url(r'^nutrition/(?P<id>\d+)/edit/$', 'edit_plan'),
    url(r'^nutrition/(?P<id>\d+)/pdf/$', 'export_pdf'),
    
    # Meals
    url(r'^nutrition/(?P<id>\d+)/edit/meal/(?P<meal_id>\w*)$', 'edit_meal'),
    url(r'^nutrition/(?P<id>\d+)/add/meal/$', 'add_meal'),
    url(r'^nutrition/(?P<id>\d+)/delete/meal/$', 'delete_meal'),
    
    # Meal items
    url(r'^nutrition/(?P<id>\d+)/edit/meal/(?P<meal_id>\d+)/item/(?P<item_id>\w*)$', 'edit_meal_item'),
    url(r'^nutrition/delete/meal/item/(?P<item_id>\d+)$', 'delete_meal_item'),
    
    # Ingredients
    url(r'^nutrition/ingredient/overview/$', 'ingredient_overview'),
    url(r'^nutrition/ingredient/(?P<id>\d+)/view/$', 'ingredient_view'),
    url(r'^nutrition/ingredient/(?P<id>\w*)/edit/$', 'ingredient_edit'),
    url(r'^nutrition/ingredient/(?P<id>\d+)/delete/$', 'delete_ingredient'),
    url(r'^nutrition/ingredient/search/$', 'ingredient_search'),   
)
