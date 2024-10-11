from django.urls import path
from . import views

app_name = 'blogsite'
urlpatterns = [
    path('', views.PostlistView.as_view),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>', views.post_detail, name='post_detail')
]