from django.db import models

# Create your models here.
class Ratio(models.Model):
    m_avg_per = models.DecimalField("市場平均PER", max_digits=7, decimal_places=2)
    m_cur_growth = models.DecimalField("今期営業増益率", max_digits=7, decimal_places=2)
    m_next_growth = models.DecimalField("来期営業増益率", max_digits=7, decimal_places=2)
    m_ratio = models.DecimalField("東証１部平均PEG", max_digits=7, decimal_places=2)
    p_avg_per = models.DecimalField("マザーズ単純平均PER", max_digits=7, decimal_places=2)    
    p_cur_growth = models.DecimalField("今期営業増益率", max_digits=7, decimal_places=2)
    p_next_growth = models.DecimalField("来期営業増益率", max_digits=7, decimal_places=2)
    p_ratio = models.DecimalField("新興PEG", max_digits=7, decimal_places=2)
    is_active = models.BooleanField("有効", default=True)