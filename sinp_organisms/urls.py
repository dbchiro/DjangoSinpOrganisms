from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import OrganismMemberViewset, OrganismViewset

app_name = "sinp_organisms"

router = SimpleRouter(trailing_slash=False)

router.register(r"organisms", OrganismViewset)
router.register(r"members", OrganismMemberViewset)

urlpatterns = [path("organisms/", include(router.urls))]
