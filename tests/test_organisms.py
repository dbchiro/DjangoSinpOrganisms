from django.test import Client

# def test_version():
#     assert __version__ == "0.1.0"


# Using the standard RequestFactory API to create a form POST request
c = Client()
request = c.post(
    "/api/v1/nomenclatures/nomenclatures",
    {"code": "test", "mnemonic": "test", "label": "test", "type": 1},
)
