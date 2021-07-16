=================
 GETTING STARTED
=================


Available endpoints
-------------------

* ``/organisms/`` > list all organisms
* ``/organisms/<int:pk>`` > retrieve one organism by organism id 
* ``/organisms/<int:pk>/members`` > retrieve one organism members by organism id 


Supported Python versions
-------------------------

* Coming soon


Supported Django versions
-------------------------

* Django 2.2 (not tested)
* Django 3.2


Supported Django Rest Framework versions
----------------------------------------

* Django Rest Framework 3.12


Installation
------------

.. code-block:: bash

    $ pip install -U dj-sinp-organisms


Configuration
-------------
    
Configure ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        (...),
        'rest_framework',
        'sinp_nomenclatures',
        'sinp_organisms',
        (...),
    )
    

Configure ``urls.py``:

.. code-block:: python

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api-auth/', include('rest_framework.urls')),
        (...),
        path('api/v1/', include('sinp_nomenclatures.urls')),
        path('api/v1/', include('sinp_organisms.urls')),
        (...),
    ]
