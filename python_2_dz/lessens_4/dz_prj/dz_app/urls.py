from django.urls import path
import dz_app.views as dz_app


urlpatterns = [
    path('', dz_app.prodact, name='prodact'),
    path('create_product/', dz_app.create_new_prodact, name='create_prodact')
]
