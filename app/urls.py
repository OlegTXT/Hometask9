from django.urls import path
from app.views import ProductList, CreateProduct, UpdateProduct, delete_product, Login


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('create/', CreateProduct.as_view(), name='product_create'),
    path('update/<int:pk>', UpdateProduct.as_view(), name='product_update'),
    path('delete/<int:pk>', delete_product, name='product_delete'),
    path('login/', Login.as_view(), name='login')
]

