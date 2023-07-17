from django.urls import path

from . import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('all-products/', views.AllProductsList.as_view()),
    path('products/search/', views.search),
    path('userinfo/', views.get_user_info),
    path('products/<slug:category_slug>/<slug:product_slug>/',
         views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]