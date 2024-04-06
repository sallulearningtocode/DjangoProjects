from django.urls import path
from .views import IndexView, RegisterView, SearchView
from .swagger import schema_view,schema_view1,schema_view2
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('registershop/', RegisterView.as_view(), name='registershop'),
    path('search/', SearchView.as_view(), name='search'),
    
    path('swagger/register', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-register'),
    path('swagger.json/register', schema_view.without_ui(cache_timeout=0), name='schema-json-register'),

    path('swagger/search', schema_view1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-search'),
    path('search/swagger.json', schema_view1.without_ui(cache_timeout=0), name='schema-json-search'),
    
    path('swagger/index', schema_view2.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-index'),
    path('swagger.json/index', schema_view2.without_ui(cache_timeout=0), name='schema-json-index'),
]