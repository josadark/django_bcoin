from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('',views.home, name='welcome-home'),
    path('about/',views.about, name='welcome-about'),
    path('demo-plot/',views.demo_plot_view,name='welcome-demo'),
    path('maps/',views.maps,name='welcome-maps'),
    path('login/',views.login_view,name='welcome-login'),
    path('logout/',views.logout_view,name='welcome-logout'),
    path('portfolio/',views.portfolio_view,name='welcome-portfolio'),
    path('stockview/',views.stockview,name='stock-view'),
    path('crypto/',views.crypto,name='welcome-crypto'),
    path('cryptoview/',views.cryptoview,name='cryptoview'),
    path('create_portfolio/',views.create_portfolio_view,name='create_portfolio'),
    path('edit_portfolio/',views.edit_portfolio,name='edit_portfolio'),
    path('view_portfolio/',views.view_portfolio,name='view_portfolio'),

    url(r'^stockview/(?P<stockID>\w+)/$', views.stockview, name='stock-view'),
    url(r'^cryptoview/(?P<stockID>\w+)/$', views.cryptoview, name='cryptoview'),
    url(r'^grabcsv/(?P<csvID>\w+)/$', views.grabcsv, name='grabcsv'),
    url(r'^edit_portfolio/(?P<portfolioID>\w+)/$', views.edit_portfolio, name='edit_portfolio'),
    url(r'^view_portfolio/(?P<portfolioID>\w+)/$', views.view_portfolio, name='view_portfolio')
]
