from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='welcome-home'),
    path('about/',views.about, name='welcome-about'),
    path('demo-plot/',views.demo_plot_view,name='welcome-demo')
]
