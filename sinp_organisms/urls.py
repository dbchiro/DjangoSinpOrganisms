from django.urls import path

from .views import OrganismMemberViewset, OrganismViewset

app_name = "sinp_organisms"

urlpatterns = [
    path(
        "organisms",
        OrganismViewset.as_view({"get": "list"}),
        name="organism_list",
    ),
    path(
        "organisms/<int:pk>",
        OrganismViewset.as_view({"get": "retrieve"}),
        name="organism",
    ),
    path(
        "organisms/<int:pk>/members",
        OrganismMemberViewset.as_view({"get": "list"}),
        name="organism_member_list",
    ),
    path(
        "organisms/member/<int:pk>",
        OrganismMemberViewset.as_view({"get": "retrieve"}),
        name="organism_member",
    ),
]
