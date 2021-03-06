from django.db import models
from django.db.models.deletion import SET_NULL
from account.models import User


class Ratio(models.Model):
    m_avg_per = models.DecimalField("市場平均PER", max_digits=7, decimal_places=2)
    m_cur_growth = models.DecimalField(
        "今期営業増益率", max_digits=7, decimal_places=2)
    m_next_growth = models.DecimalField(
        "来期営業増益率", max_digits=7, decimal_places=2)
    m_ratio = models.DecimalField("東証１部平均PEG", max_digits=7, decimal_places=2)
    p_avg_per = models.DecimalField(
        "マザーズ単純平均PER", max_digits=7, decimal_places=2)
    p_cur_growth = models.DecimalField(
        "今期営業増益率", max_digits=7, decimal_places=2)
    p_next_growth = models.DecimalField(
        "来期営業増益率", max_digits=7, decimal_places=2)
    p_ratio = models.DecimalField("新興PEG", max_digits=7, decimal_places=2)
    is_active = models.BooleanField("有効", default=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)


class Industry(models.Model):
    name = models.CharField('33業種', max_length=190)
    company_num = models.IntegerField('社数', default=0)
    sales_sum = models.CharField(
        '業界の売上高の合計',
        null=True,
        blank=True,
        max_length=50)
    profit_sum = models.CharField(
        '業界の営業利益の合計',
        null=True,
        blank=True,
        max_length=50)
    extended_now = models.DecimalField(
        '売上高の伸び率業界平均（今期）%',
        null=True,
        max_digits=5,
        decimal_places=1)
    extended_next = models.DecimalField(
        '売上高の伸び率業界平均（来期）%',
        null=True,
        max_digits=5,
        decimal_places=1)
    order = models.CharField(
        '順序',
        max_length=50,
        default="",
        null=True,
        blank=True)


class Sheet(models.Model):
    title = models.CharField("タイトル", max_length=255)
    user = models.ForeignKey(
        User,
        verbose_name="ユーザー",
        related_name="sheets",
        on_delete=models.CASCADE)
    stock_year = models.IntegerField("株価年")
    stock_month = models.IntegerField("株価月")
    stock_day = models.IntegerField("株価日")
    finished_month = models.IntegerField("発行済月")
    finished_day = models.IntegerField("発行済日")

    a_brand_code = models.CharField(
        "A-銘柄コード", max_length=255, null=True, blank=True)
    a_company_name = models.CharField(
        "A-企業名", max_length=255, null=True, blank=True)
    a_stock_price = models.CharField(
        "A-株価", max_length=255, null=True, blank=True)
    a_market_cap = models.CharField(
        "A-時価総額", max_length=255, null=True, blank=True)
    a_share_num = models.CharField(
        "A-発行済株", max_length=255, null=True, blank=True)
    a_positive_one = models.CharField(
        "A-定性評価-1", max_length=255, null=True, blank=True)
    a_positive_two = models.CharField(
        "A-定性評価-1", max_length=255, null=True, blank=True)
    a_positive_three = models.CharField(
        "A-定性評価-1", max_length=255, null=True, blank=True)
    a_positive_four = models.CharField(
        "A-定性評価-1", max_length=255, null=True, blank=True)
    a_positive_comment_one = models.IntegerField("A-ポジティブコメント数-1", null=True)
    a_negative_comment_one = models.IntegerField("A-ネガティブコメント数-1", null=True)
    a_positive_comment_two = models.IntegerField("A-ポジティブコメント数-2", null=True)
    a_negative_comment_two = models.IntegerField("A-ネガティブコメント数-2", null=True)
    a_shareholder_rank = models.IntegerField("A-株主順位", default=-1)
    a_capital_adequacy_ratio = models.DecimalField(
        "A-自己資本比率", max_digits=5, decimal_places=1, null=True)
    a_pbr = models.DecimalField(
        "A-PBR",
        max_digits=8,
        decimal_places=2,
        null=True)
    a_sales = models.IntegerField("A-営業CF", null=True)
    a_invest = models.IntegerField("A-投資CF", null=True)
    a_profit_category = models.ForeignKey(
        Industry,
        verbose_name="A-33業種分類",
        null=True,
        blank=True,
        related_name="sheet_a",
        on_delete=models.SET_NULL)
    a_sales_previous = models.CharField(
        "A-売上高-前期", max_length=255, null=True, blank=True)
    a_sales_now = models.CharField(
        "A-売上高-今期",
        max_length=255,
        null=True,
        blank=True)
    a_sales_next = models.CharField(
        "A-売上高-来期", max_length=255, null=True, blank=True)
    a_profit_previous = models.CharField(
        "A-営業利益-前期", max_length=255, null=True, blank=True)
    a_profit_now = models.CharField(
        "A-営業利益-今期", max_length=255, null=True, blank=True)
    a_profit_next = models.CharField(
        "A-営業利益-来期", max_length=255, null=True, blank=True)
    a_profit_updated = models.IntegerField("A-最高純益を更新", default=-1)
    a_sales_comment_now = models.IntegerField("A-今期稼ぐ力", default=-1)
    a_sales_comment_next = models.IntegerField("A-来期稼ぐ力", default=-1)
    a_yield_percent = models.DecimalField(
        "A-配当利回り", max_digits=5, decimal_places=2, null=True)
    a_comment_chart = models.IntegerField("A-チャート", default=-1)
    a_comment_ma = models.IntegerField("A-移動平均線", default=-1)
    a_comment_compare = models.IntegerField("A-チャート-移動平均線", default=-1)
    a_expected_per = models.DecimalField(
        "A-今期予想PER", max_digits=5, decimal_places=2, null=True)
    a_per_comment = models.IntegerField("A-PER-判定", default=-1)
    a_peg_comment = models.IntegerField("A-PEG-判定", default=-1)
    a_psr_comment = models.IntegerField("A-PSR-判定", default=-1)
    a_trust_val = models.CharField(
        "A-信用買残", max_length=255, null=True, blank=True)
    a_memo = models.TextField("A-メモ", null=True)

    b_brand_code = models.CharField(
        "B-銘柄コード", max_length=255, null=True, blank=True)
    b_company_name = models.CharField(
        "B-企業名", max_length=255, null=True, blank=True)
    b_stock_price = models.CharField(
        "B-株価", max_length=255, null=True, blank=True)
    b_market_cap = models.CharField(
        "B-時価総額", max_length=255, null=True, blank=True)
    b_share_num = models.CharField(
        "B-発行済株", max_length=255, null=True, blank=True)
    b_positive_one = models.CharField(
        "B-定性評価-1", max_length=255, null=True, blank=True)
    b_positive_two = models.CharField(
        "B-定性評価-1", max_length=255, null=True, blank=True)
    b_positive_three = models.CharField(
        "B-定性評価-1", max_length=255, null=True, blank=True)
    b_positive_four = models.CharField(
        "B-定性評価-1", max_length=255, null=True, blank=True)
    b_positive_comment_one = models.IntegerField("B-ポジティブコメント数-1", null=True)
    b_negative_comment_one = models.IntegerField("B-ネガティブコメント数-1", null=True)
    b_positive_comment_two = models.IntegerField("B-ポジティブコメント数-2", null=True)
    b_negative_comment_two = models.IntegerField("B-ネガティブコメント数-2", null=True)
    b_shareholder_rank = models.IntegerField("B-株主順位", default=-1)
    b_capital_adequacy_ratio = models.DecimalField(
        "B-自己資本比率", max_digits=5, decimal_places=1, null=True)
    b_pbr = models.DecimalField(
        "B-PBR",
        max_digits=8,
        decimal_places=2,
        null=True)
    b_sales = models.IntegerField("B-営業CF", null=True)
    b_invest = models.IntegerField("B-投資CF", null=True)
    b_profit_category = models.ForeignKey(
        Industry,
        verbose_name="B-33業種分類",
        null=True,
        blank=True,
        related_name="sheet_b",
        on_delete=models.SET_NULL)
    b_sales_previous = models.CharField(
        "B-売上高-前期", max_length=255, null=True, blank=True)
    b_sales_now = models.CharField(
        "B-売上高-今期",
        max_length=255,
        null=True,
        blank=True)
    b_sales_next = models.CharField(
        "B-売上高-来期", max_length=255, null=True, blank=True)
    b_profit_previous = models.CharField(
        "B-営業利益-前期", max_length=255, null=True, blank=True)
    b_profit_now = models.CharField(
        "B-営業利益-今期", max_length=255, null=True, blank=True)
    b_profit_next = models.CharField(
        "B-営業利益-来期", max_length=255, null=True, blank=True)
    b_profit_updated = models.IntegerField("B-最高純益を更新", default=-1)
    b_sales_comment_now = models.IntegerField("B-今期稼ぐ力", default=-1)
    b_sales_comment_next = models.IntegerField("B-来期稼ぐ力", default=-1)
    b_yield_percent = models.DecimalField(
        "B-配当利回り", max_digits=5, decimal_places=2, null=True)
    b_comment_chart = models.IntegerField("B-チャート", default=-1)
    b_comment_ma = models.IntegerField("B-移動平均線", default=-1)
    b_comment_compare = models.IntegerField("B-チャート-移動平均線", default=-1)
    b_expected_per = models.DecimalField(
        "B-今期予想PER", max_digits=5, decimal_places=2, null=True)
    b_per_comment = models.IntegerField("B-PER-判定", default=-1)
    b_peg_comment = models.IntegerField("B-PEG-判定", default=-1)
    b_psr_comment = models.IntegerField("B-PSR-判定", default=-1)
    b_trust_val = models.CharField(
        "B-信用買残", max_length=255, null=True, blank=True)
    b_memo = models.TextField("B-メモ", null=True)

    c_brand_code = models.CharField(
        "C-銘柄コード", max_length=255, null=True, blank=True)
    c_company_name = models.CharField(
        "C-企業名", max_length=255, null=True, blank=True)
    c_stock_price = models.CharField(
        "C-株価", max_length=255, null=True, blank=True)
    c_market_cap = models.CharField(
        "C-時価総額", max_length=255, null=True, blank=True)
    c_share_num = models.CharField(
        "C-発行済株", max_length=255, null=True, blank=True)
    c_positive_one = models.CharField(
        "C-定性評価-1", max_length=255, null=True, blank=True)
    c_positive_two = models.CharField(
        "C-定性評価-1", max_length=255, null=True, blank=True)
    c_positive_three = models.CharField(
        "C-定性評価-1", max_length=255, null=True, blank=True)
    c_positive_four = models.CharField(
        "C-定性評価-1", max_length=255, null=True, blank=True)
    c_positive_comment_one = models.IntegerField("C-ポジティブコメント数-1", null=True)
    c_negative_comment_one = models.IntegerField("C-ネガティブコメント数-1", null=True)
    c_positive_comment_two = models.IntegerField("C-ポジティブコメント数-2", null=True)
    c_negative_comment_two = models.IntegerField("C-ネガティブコメント数-2", null=True)
    c_shareholder_rank = models.IntegerField("C-株主順位", default=-1)
    c_capital_adequacy_ratio = models.DecimalField(
        "C-自己資本比率", max_digits=5, decimal_places=1, null=True)
    c_pbr = models.DecimalField(
        "C-PBR",
        max_digits=8,
        decimal_places=2,
        null=True)
    c_sales = models.IntegerField("C-営業CF", null=True)
    c_invest = models.IntegerField("C-投資CF", null=True)
    c_profit_category = models.ForeignKey(
        Industry,
        verbose_name="C-33業種分類",
        null=True,
        blank=True,
        related_name="sheet_c",
        on_delete=models.SET_NULL)
    c_sales_previous = models.CharField(
        "C-売上高-前期", max_length=255, null=True, blank=True)
    c_sales_now = models.CharField(
        "C-売上高-今期",
        max_length=255,
        null=True,
        blank=True)
    c_sales_next = models.CharField(
        "C-売上高-来期", max_length=255, null=True, blank=True)
    c_profit_previous = models.CharField(
        "C-営業利益-前期", max_length=255, null=True, blank=True)
    c_profit_now = models.CharField(
        "C-営業利益-今期", max_length=255, null=True, blank=True)
    c_profit_next = models.CharField(
        "C-営業利益-来期", max_length=255, null=True, blank=True)
    c_profit_updated = models.IntegerField("C-最高純益を更新", default=-1)
    c_sales_comment_now = models.IntegerField("C-今期稼ぐ力", default=-1)
    c_sales_comment_next = models.IntegerField("C-来期稼ぐ力", default=-1)
    c_yield_percent = models.DecimalField(
        "C-配当利回り", max_digits=5, decimal_places=2, null=True)
    c_comment_chart = models.IntegerField("C-チャート", default=-1)
    c_comment_ma = models.IntegerField("C-移動平均線", default=-1)
    c_comment_compare = models.IntegerField("C-チャート-移動平均線", default=-1)
    c_expected_per = models.DecimalField(
        "C-今期予想PER", max_digits=5, decimal_places=2, null=True)
    c_per_comment = models.IntegerField("C-PER-判定", default=-1)
    c_peg_comment = models.IntegerField("C-PEG-判定", default=-1)
    c_psr_comment = models.IntegerField("C-PSR-判定", default=-1)
    c_trust_val = models.CharField(
        "C-信用買残", max_length=255, null=True, blank=True)
    c_memo = models.TextField("C-メモ", null=True)

    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
