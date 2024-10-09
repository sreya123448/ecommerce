from django.urls import path
from . import views

urlpatterns = [
    path('superadmin_view/',views.View_SuperAdmin,name='superadmin_view'),
    path('superadmin_create/',views.Create_SuperAdmin,name='superadmin_create'),
    path('superadmin_edit/<int:id>',views.SuperAdmin_Edit,name='edit'),
    path('delete/<int:id>',views.delete)
]