from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
 url(r'^$', views.index, name='index'),
 path('categories', views.CategoryList.as_view(template_name='category/category_list.html'), name='category_list'),
 path('category/<int:pk>', views.CategoryDetail.as_view(template_name='category/category_detail.html'), name='category_detail'),
 path('create', views.CategoryCreate.as_view(template_name='category/category_form.html'), name='category_create'),
 path('update/<int:pk>', views.CategoryUpdate.as_view(template_name='category/category_form.html'), name='category_update'),
 path('delete/<int:pk>', views.CategoryDelete.as_view(template_name='category/category_confirm_delete.html'), name='category_delete'),
]