from django.contrib import admin
#import models here
from .models import Post
from .models import Candle
from .models import Stock
from .models import StockDatabase


# Register models here.
admin.site.register(Post)
admin.site.register(Candle)
admin.site.register(Stock)
admin.site.register(StockDatabase)
