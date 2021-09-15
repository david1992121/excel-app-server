from ratio.models import Ratio
from django.contrib import admin

# Register your models here.
class RatioAdmin(admin.ModelAdmin):
    list_display = ('m_avg_per', 'm_cur_growth', 'm_next_growth', 'm_ratio', 'p_avg_per', 'p_cur_growth', 'p_next_growth', 'p_ratio', 'is_active', )

admin.site.register(Ratio, RatioAdmin)