# Generated by Django 3.2.7 on 2021-09-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='a_brand_code',
            field=models.CharField(max_length=255, null=True, verbose_name='A-銘柄コード'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_capital_adequacy_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='A-自己資本比率'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_company_name',
            field=models.CharField(max_length=255, null=True, verbose_name='A-企業名'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_company_num',
            field=models.IntegerField(null=True, verbose_name='A-社数'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_expected_per',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='A-今期予想PER'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_extended_next',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='A-売上高の伸び率-来期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_extended_now',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='A-売上高の伸び率-今期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_industry_sales',
            field=models.CharField(max_length=255, null=True, verbose_name='A-売上高業界平均'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_invest',
            field=models.IntegerField(null=True, verbose_name='A-投資CF'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_market_cap',
            field=models.CharField(max_length=255, null=True, verbose_name='A-時価総額'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_memo',
            field=models.TextField(null=True, verbose_name='A-メモ'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_negative_comment_one',
            field=models.IntegerField(null=True, verbose_name='A-ネガティブコメント数-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_negative_comment_two',
            field=models.IntegerField(null=True, verbose_name='A-ネガティブコメント数-2'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_pbr',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='A-PBR'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_positive_comment_one',
            field=models.IntegerField(null=True, verbose_name='A-ポジティブコメント数-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_positive_comment_two',
            field=models.IntegerField(null=True, verbose_name='A-ポジティブコメント数-2'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_positive_four',
            field=models.CharField(max_length=255, null=True, verbose_name='A-定性評価-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_positive_one',
            field=models.CharField(max_length=255, null=True, verbose_name='A-定性評価-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_positive_three',
            field=models.CharField(max_length=255, null=True, verbose_name='A-定性評価-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_positive_two',
            field=models.CharField(max_length=255, null=True, verbose_name='A-定性評価-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_profit_category',
            field=models.CharField(max_length=255, null=True, verbose_name='A-33業種分類'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_profit_next',
            field=models.CharField(max_length=255, null=True, verbose_name='A-営業利益-来期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_profit_now',
            field=models.CharField(max_length=255, null=True, verbose_name='A-営業利益-今期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_profit_previous',
            field=models.CharField(max_length=255, null=True, verbose_name='A-営業利益-前期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_profit_scale',
            field=models.CharField(max_length=255, null=True, verbose_name='A-営業利益業界平均'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_sales',
            field=models.IntegerField(null=True, verbose_name='A-営業CF'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_sales_next',
            field=models.CharField(max_length=255, null=True, verbose_name='A-売上高-来期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_sales_now',
            field=models.CharField(max_length=255, null=True, verbose_name='A-売上高-今期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_sales_previous',
            field=models.CharField(max_length=255, null=True, verbose_name='A-売上高-前期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_share_num',
            field=models.CharField(max_length=255, null=True, verbose_name='A-発行済株'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_stock_price',
            field=models.CharField(max_length=255, null=True, verbose_name='A-株価'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_trust_val',
            field=models.CharField(max_length=255, null=True, verbose_name='A-信用買残'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='a_yield_percent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='A-配当利回り'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_brand_code',
            field=models.CharField(max_length=255, null=True, verbose_name='B-銘柄コード'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_capital_adequacy_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='B-自己資本比率'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_company_name',
            field=models.CharField(max_length=255, null=True, verbose_name='B-企業名'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_company_num',
            field=models.IntegerField(null=True, verbose_name='B-社数'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_expected_per',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='B-今期予想PER'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_extended_next',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='B-売上高の伸び率-来期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_extended_now',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='B-売上高の伸び率-今期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_industry_sales',
            field=models.CharField(max_length=255, null=True, verbose_name='B-売上高業界平均'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_invest',
            field=models.IntegerField(null=True, verbose_name='B-投資CF'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_market_cap',
            field=models.CharField(max_length=255, null=True, verbose_name='B-時価総額'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_memo',
            field=models.TextField(null=True, verbose_name='B-メモ'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_negative_comment_one',
            field=models.IntegerField(null=True, verbose_name='B-ネガティブコメント数-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_negative_comment_two',
            field=models.IntegerField(null=True, verbose_name='B-ネガティブコメント数-2'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_pbr',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='B-PBR'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_positive_comment_one',
            field=models.IntegerField(null=True, verbose_name='B-ポジティブコメント数-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_positive_comment_two',
            field=models.IntegerField(null=True, verbose_name='B-ポジティブコメント数-2'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_positive_four',
            field=models.CharField(max_length=255, null=True, verbose_name='B-定性評価-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_positive_one',
            field=models.CharField(max_length=255, null=True, verbose_name='B-定性評価-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_positive_three',
            field=models.CharField(max_length=255, null=True, verbose_name='B-定性評価-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_positive_two',
            field=models.CharField(max_length=255, null=True, verbose_name='B-定性評価-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_profit_category',
            field=models.CharField(max_length=255, null=True, verbose_name='B-33業種分類'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_profit_next',
            field=models.CharField(max_length=255, null=True, verbose_name='B-営業利益-来期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_profit_now',
            field=models.CharField(max_length=255, null=True, verbose_name='B-営業利益-今期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_profit_previous',
            field=models.CharField(max_length=255, null=True, verbose_name='B-営業利益-前期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_profit_scale',
            field=models.CharField(max_length=255, null=True, verbose_name='B-営業利益業界平均'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_sales',
            field=models.IntegerField(null=True, verbose_name='B-営業CF'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_sales_next',
            field=models.CharField(max_length=255, null=True, verbose_name='B-売上高-来期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_sales_now',
            field=models.CharField(max_length=255, null=True, verbose_name='B-売上高-今期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_sales_previous',
            field=models.CharField(max_length=255, null=True, verbose_name='B-売上高-前期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_share_num',
            field=models.CharField(max_length=255, null=True, verbose_name='B-発行済株'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_stock_price',
            field=models.CharField(max_length=255, null=True, verbose_name='B-株価'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_trust_val',
            field=models.CharField(max_length=255, null=True, verbose_name='B-信用買残'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='b_yield_percent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='B-配当利回り'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_brand_code',
            field=models.CharField(max_length=255, null=True, verbose_name='C-銘柄コード'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_capital_adequacy_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='C-自己資本比率'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_company_name',
            field=models.CharField(max_length=255, null=True, verbose_name='C-企業名'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_company_num',
            field=models.IntegerField(null=True, verbose_name='C-社数'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_expected_per',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='C-今期予想PER'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_extended_next',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='C-売上高の伸び率-来期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_extended_now',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='C-売上高の伸び率-今期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_industry_sales',
            field=models.CharField(max_length=255, null=True, verbose_name='C-売上高業界平均'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_invest',
            field=models.IntegerField(null=True, verbose_name='C-投資CF'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_market_cap',
            field=models.CharField(max_length=255, null=True, verbose_name='C-時価総額'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_memo',
            field=models.TextField(null=True, verbose_name='C-メモ'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_negative_comment_one',
            field=models.IntegerField(null=True, verbose_name='C-ネガティブコメント数-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_negative_comment_two',
            field=models.IntegerField(null=True, verbose_name='C-ネガティブコメント数-2'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_pbr',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='C-PBR'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_positive_comment_one',
            field=models.IntegerField(null=True, verbose_name='C-ポジティブコメント数-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_positive_comment_two',
            field=models.IntegerField(null=True, verbose_name='C-ポジティブコメント数-2'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_positive_four',
            field=models.CharField(max_length=255, null=True, verbose_name='C-定性評価-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_positive_one',
            field=models.CharField(max_length=255, null=True, verbose_name='C-定性評価-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_positive_three',
            field=models.CharField(max_length=255, null=True, verbose_name='C-定性評価-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_positive_two',
            field=models.CharField(max_length=255, null=True, verbose_name='C-定性評価-1'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_profit_category',
            field=models.CharField(max_length=255, null=True, verbose_name='C-33業種分類'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_profit_next',
            field=models.CharField(max_length=255, null=True, verbose_name='C-営業利益-来期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_profit_now',
            field=models.CharField(max_length=255, null=True, verbose_name='C-営業利益-今期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_profit_previous',
            field=models.CharField(max_length=255, null=True, verbose_name='C-営業利益-前期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_profit_scale',
            field=models.CharField(max_length=255, null=True, verbose_name='C-営業利益業界平均'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_sales',
            field=models.IntegerField(null=True, verbose_name='C-営業CF'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_sales_next',
            field=models.CharField(max_length=255, null=True, verbose_name='C-売上高-来期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_sales_now',
            field=models.CharField(max_length=255, null=True, verbose_name='C-売上高-今期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_sales_previous',
            field=models.CharField(max_length=255, null=True, verbose_name='C-売上高-前期'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_share_num',
            field=models.CharField(max_length=255, null=True, verbose_name='C-発行済株'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_stock_price',
            field=models.CharField(max_length=255, null=True, verbose_name='C-株価'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_trust_val',
            field=models.CharField(max_length=255, null=True, verbose_name='C-信用買残'),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='c_yield_percent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='C-配当利回り'),
        ),
    ]
