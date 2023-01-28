from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name='apiOverview' ),
    path('list/', views.showAll, name='product-list' ),
    path('viewProduct/<int:pk>', views.viewProduct, name='view-product' ),
    path('createProduct/', views.createProduct, name='create-product' ),   
]

    