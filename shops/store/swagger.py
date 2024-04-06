from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# Import your API view classes here
from .views import RegisterView, SearchView, IndexView
# Include schemas in schema view

schema_view = get_schema_view(
    openapi.Info(
        title="Register",
        default_version="v1",
        description="llows users to register shops with their details including name, latitude, and longitude.",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
schema_view1 = get_schema_view(
    openapi.Info(
        title="Search",
        default_version="v1",
        description=" Enables users to search for nearby shops based on their current location.",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
schema_view2 = get_schema_view(
    openapi.Info(
        title="Index Page",
        default_version="v1",
        description=" Displays information about the application.",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)