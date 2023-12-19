from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookList, name="books"),
    path('update_book/<int:id>', views.BookUpdate, name='update_book'),
    path('delete_book/<int:id>', views.BookDelete, name='delete_book'),
    
    

]