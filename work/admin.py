from work.models import Industry, Ratio
from django.contrib import admin

# Register your models here.


class RatioAdmin(admin.ModelAdmin):
    list_display = (
        'm_avg_per',
        'm_cur_growth',
        'm_next_growth',
        'm_ratio',
        'p_avg_per',
        'p_cur_growth',
        'p_next_growth',
        'p_ratio',
        'is_active',
    )


class IndustryAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('custom/css/admin.css',)
        }
    list_display = (
        'name',
        'company_num',
        'sales_sum',
        'profit_sum',
        'extended_now',
        'extended_next',
    )


admin.site.register(Ratio, RatioAdmin)
admin.site.register(Industry, IndustryAdmin)
