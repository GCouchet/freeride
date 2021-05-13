from rest_framework import routers
from .views import LocationViewSet, CountryViewSet, CityViewSet

router = routers.DefaultRouter()
router.register(r'location', LocationViewSet, basename='location')
router.register(r'country', CountryViewSet, basename='country')
router.register(r'city', CityViewSet, basename='city')
urlpatterns = router.urls
