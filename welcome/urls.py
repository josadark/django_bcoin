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
    path('screens/',views.screens,name='welcome-screens'),
    path('suggestions/',views.suggestions,name='welcome-suggestions'),
    path('stockview/',views.stockview,name='stock-view'),
    path('crypto/',views.crypto,name='welcome-crypto'),
    path('cryptoview/',views.cryptoview,name='cryptoview'),
    path('create_portfolio/',views.create_portfolio_view,name='create_portfolio'),
    path('create_screen/',views.create_screen,name='create_screen'),
    path('edit_portfolio/',views.edit_portfolio,name='edit_portfolio'),
    path('view_portfolio/',views.view_portfolio,name='view_portfolio'),
    path('view_public_portfolio/<str:portfolioID>/',views.view_public_portfolio,name='view_public_portfolio'),
    path('view_screened/<str:portfolioID>/',views.view_screened,name='view_screened'),
    path('delete_selected_portfolio/',views.delete_selected_portfolio,name='delete_selected_portfolio'),
    path('delete_portfolio/',views.delete_portfolio,name='delete_portfolio'),
    path('chineseMarket/',views.chineseMarket,name='chineseMarket'),
    path('groups/',views.groups,name='groups'),
    path('removing_portfolio_asset/<str:portfolioID>/<str:stockID>/<int:stockCount>/', views.removing_portfolio_asset, name='removing_portfolio_asset'),

    url(r'^portfolio_addition/(?P<stockID>\w+)/$', views.portfolio_addition, name='portfolio_addition'),
    url(r'^deleting/(?P<portfolioID>\w+)/$', views.deleting, name='deleting'),
    url(r'^stockview/(?P<stockID>\w+)/$', views.stockview, name='stock-view'),
    url(r'^cryptoview/(?P<stockID>\w+)/$', views.cryptoview, name='cryptoview'),
    url(r'^grabcsv/(?P<csvID>\w+)/$', views.grabcsv, name='grabcsv'),
    url(r'^edit_portfolio/(?P<portfolioID>\w+)/$', views.edit_portfolio, name='edit_portfolio'),
    url(r'^edit_portfolio_fields/(?P<portfolioID>\w+)/$', views.edit_portfolio_fields, name='edit_portfolio_fields'),
    url(r'^view_portfolio/(?P<portfolioID>\w+)/$', views.view_portfolio, name='view_portfolio'),
    url(r'^remove_portfolio_asset/(?P<portfolioID>\w+)/$', views.remove_portfolio_asset, name='remove_portfolio_asset'),
    url(r'^add_to_portfolio/(?P<stockID>\w+)/$', views.add_to_portfolio, name='add_to_portfolio'),
    url(r'^delete_selected_portfolio/(?P<portfolioID>\w+)/$', views.delete_selected_portfolio, name='delete_selected_portfolio'),
    url(r'^adding/(?P<stockID>\w+)/(?P<portfolioID>\w+)/$', views.adding, name='adding')
]
