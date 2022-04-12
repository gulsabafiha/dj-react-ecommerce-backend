from unicodedata import name
from django.urls import path 
from base.views import user_views as views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/',views.registerUser,name="user-register"), 
    path('profile/',views.getUserProfile,name="user-profile"),
    path('profile/update/',views.updateUserProfile,name="update-profile"),
    path('',views.getUsers,name="users"),
    path('delete/<str:pk>/',views.deleteUser,name='user-delete'),
    path('update/<str:pk>/',views.updateUser,name='update-delete'),
    path('<str:pk>/',views.getUsersById,name='user'),
   
]