from django.contrib import admin
#import models here
from .models import Post
from .models import Candle
from .models import Stock
from .models import StockDatabase
from .models import Profile
from .models import SimpleStock
from .models import StockHandle
from .models import moment
from .models import IPO
from .models import CryptoStock
from .models import Portfolio
from .models import StockAsset
from .models import PublicPortfolio
from .models import Screen
from .models import ScreenAsset
from .models import PublicStockAsset
from .models import ChinaStock

# Register models here.
admin.site.register(Post)
admin.site.register(Candle)
admin.site.register(Stock)
admin.site.register(StockDatabase)
admin.site.register(Profile)
admin.site.register(SimpleStock)
admin.site.register(StockHandle)
admin.site.register(moment)
admin.site.register(IPO)
admin.site.register(CryptoStock)
admin.site.register(Portfolio)
admin.site.register(StockAsset)
admin.site.register(PublicPortfolio)
admin.site.register(Screen)
admin.site.register(ScreenAsset)
admin.site.register(PublicStockAsset)
admin.site.register(ChinaStock)
