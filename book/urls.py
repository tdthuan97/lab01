from django.urls import path



from book import views,urls

urlpatterns = [
    path('',views.index, name='index'),
    path('listbook/',views.showbook, name='listbook')
]
