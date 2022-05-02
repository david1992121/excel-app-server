from email.policy import default
import json
from attr import field
from django.test import TestCase
from django.urls import reverse
from account.models import User

from work.models import Industry, Ratio, Sheet

class RatioModelTest(TestCase):
    def setUp(self):
        self.basic = Ratio.objects.create(
            m_avg_per=1.00, m_cur_growth=1.00, m_next_growth=1.00,
            m_ratio = 1.00, p_avg_per = 1.00, p_cur_growth = 1.00, p_next_growth = 1.00, p_ratio = 1.00,
            is_active = True
        )

    def test_all_decimal_fields(self):
        fields = [
            { "name": "m_avg_per", "verbose": "市場平均PER" },
            { "name": "m_cur_growth", "verbose": "今期営業増益率" },
            { "name": "m_next_growth", "verbose": "来期営業増益率" },
            { "name": "m_ratio", "verbose": "東証１部平均PEG" },
            { "name": "p_avg_per", "verbose": "マザーズ単純平均PER" },
            { "name": "p_cur_growth", "verbose": "今期営業増益率" },
            { "name": "p_next_growth", "verbose": "来期営業増益率" },
            { "name": "p_ratio", "verbose": "新興PEG" }
        ]
        for field_item in fields:
            self.check_decimal_field(field_item["name"], field_item["verbose"])

    def check_decimal_field(self, field_name, verbose_name):
        meta_data = self.basic._meta.get_field(field_name)
        self.assertEqual(meta_data.verbose_name, verbose_name)
        self.assertEqual(meta_data.null, False)
        self.assertEqual(meta_data.blank, False)
        self.assertEqual(meta_data.max_digits, 7)
        self.assertEqual(meta_data.decimal_places, 2)
        self.assertEqual(self.basic.m_avg_per, 1.00)

    def test_is_active(self):
        meta_data = self.basic._meta.get_field('is_active')
        self.assertEqual(meta_data.verbose_name, '有効')
        self.assertEqual(meta_data.default, True)

    def test_created_at(self):
        meta_data = self.basic._meta.get_field('created_at')
        self.assertEqual(meta_data.verbose_name, '作成日時')
        self.assertEqual(meta_data.auto_now_add, True)
        self.assertEqual(meta_data.auto_now, False)

    def test_updated_at(self):
        meta_data = self.basic._meta.get_field('updated_at')
        self.assertEqual(meta_data.verbose_name, '更新日時')
        self.assertEqual(meta_data.auto_now_add, False)
        self.assertEqual(meta_data.auto_now, True)

class IndustryModelTest(TestCase):
    def setUp(self):
        self.industry = Industry.objects.create(
            name = 'IT',
            company_num = 10,
            sales_sum = "100000000",
            profit_sum = "10000000",
            extended_now = 1.3,
            extended_next = 1.7,
            order = "1"
        )

    def test_name(self):
        meta_data = self.industry._meta.get_field('name')
        self.assertEqual(meta_data.verbose_name, '33業種')
        self.assertEqual(meta_data.max_length, 190)
        self.assertEqual(meta_data.null, False)
        self.assertEqual(meta_data.blank, False)
        self.industry.name = "IT"

    def test_company_num(self):
        meta_data = self.industry._meta.get_field('company_num')
        self.assertEqual(meta_data.verbose_name, '社数')
        self.assertEqual(meta_data.default, 0)
        self.industry.company_num = 10

    def test_sales_sum(self):
        meta_data = self.industry._meta.get_field('sales_sum')
        self.assertEqual(meta_data.verbose_name, '業界の売上高の合計')
        self.assertEqual(meta_data.max_length, 50)
        self.assertEqual(meta_data.null, True)
        self.assertEqual(meta_data.blank, True)
        self.industry.sales_sum = "100000000"

    def test_profit_sum(self):
        meta_data = self.industry._meta.get_field('profit_sum')
        self.assertEqual(meta_data.verbose_name, '業界の営業利益の合計')
        self.assertEqual(meta_data.max_length, 50)
        self.assertEqual(meta_data.null, True)
        self.assertEqual(meta_data.blank, True)
        self.industry.profit_sum = "10000000"

    def test_extended_now(self):
        meta_data = self.industry._meta.get_field('extended_now')
        self.assertEqual(meta_data.verbose_name, '売上高の伸び率業界平均（今期）%')
        self.assertEqual(meta_data.null, True)
        self.assertEqual(meta_data.max_digits, 5)
        self.assertEqual(meta_data.decimal_places, 1)
        self.industry.extended_now = 1.3

    def test_extended_next(self):
        meta_data = self.industry._meta.get_field('extended_next')
        self.assertEqual(meta_data.verbose_name, '売上高の伸び率業界平均（来期）%')
        self.assertEqual(meta_data.null, True)
        self.assertEqual(meta_data.max_digits, 5)
        self.assertEqual(meta_data.decimal_places, 1)
        self.industry.extended_next = 1.7
    
    def test_order(self):
        meta_data = self.industry._meta.get_field('order')
        self.assertEqual(meta_data.verbose_name, '順序')
        self.assertEqual(meta_data.default, "")
        self.assertEqual(meta_data.max_length, 50)
        self.assertEqual(meta_data.null, True)
        self.assertEqual(meta_data.blank, True)
        self.industry.order = "1"

class TestSheetModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@gmail.com", username="test-user")
        self.sheet = Sheet.objects.create(
            title="sheet-1",
            user=self.user,
            stock_year=2022,
            stock_month=11,
            stock_day=1,
            finished_month = 12,
            finished_day = 1
        )

    def test_char_fields(self):
        fields  = [
            { "field": "a_brand_code", "verbose": "A-銘柄コード" },
            { "field": "a_company_name", "verbose": "A-企業名" },
            { "field": "a_stock_price", "verbose": "A-株価" },
            { "field": "a_market_cap", "verbose": "A-時価総額" },
            { "field": "a_share_num", "verbose": "A-発行済株" },
            { "field": "a_positive_one", "verbose": "A-定性評価-1" },
            { "field": "a_positive_two", "verbose": "A-定性評価-1" },
            { "field": "a_positive_three", "verbose": "A-定性評価-1" },
            { "field": "a_positive_four", "verbose": "A-定性評価-1" },
            { "field": "a_sales_previous", "verbose": "A-売上高-前期" },
            { "field": "a_sales_now", "verbose": "A-売上高-今期" },
            { "field": "a_sales_next", "verbose": "A-売上高-来期" },
            { "field": "a_profit_previous", "verbose": "A-営業利益-前期" },
            { "field": "a_profit_now", "verbose": "A-営業利益-今期" },
            { "field": "a_profit_next", "verbose": "A-営業利益-来期" },
            { "field": "a_trust_val", "verbose": "A-信用買残" },
            { "field": "b_brand_code", "verbose": "B-銘柄コード" },
            { "field": "b_company_name", "verbose": "B-企業名" },
            { "field": "b_stock_price", "verbose": "B-株価" },
            { "field": "b_market_cap", "verbose": "B-時価総額" },
            { "field": "b_share_num", "verbose": "B-発行済株" },
            { "field": "b_positive_one", "verbose": "B-定性評価-1" },
            { "field": "b_positive_two", "verbose": "B-定性評価-1" },
            { "field": "b_positive_three", "verbose": "B-定性評価-1" },
            { "field": "b_positive_four", "verbose": "B-定性評価-1" },
            { "field": "b_sales_previous", "verbose": "B-売上高-前期" },
            { "field": "b_sales_now", "verbose": "B-売上高-今期" },
            { "field": "b_sales_next", "verbose": "B-売上高-来期" },
            { "field": "b_profit_previous", "verbose": "B-営業利益-前期" },
            { "field": "b_profit_now", "verbose": "B-営業利益-今期" },
            { "field": "b_profit_next", "verbose": "B-営業利益-来期" },
            { "field": "b_trust_val", "verbose": "B-信用買残" },
            { "field": "c_brand_code", "verbose": "C-銘柄コード" },
            { "field": "c_company_name", "verbose": "C-企業名" },
            { "field": "c_stock_price", "verbose": "C-株価" },
            { "field": "c_market_cap", "verbose": "C-時価総額" },
            { "field": "c_share_num", "verbose": "C-発行済株" },
            { "field": "c_positive_one", "verbose": "C-定性評価-1" },
            { "field": "c_positive_two", "verbose": "C-定性評価-1" },
            { "field": "c_positive_three", "verbose": "C-定性評価-1" },
            { "field": "c_positive_four", "verbose": "C-定性評価-1" },
            { "field": "c_sales_previous", "verbose": "C-売上高-前期" },
            { "field": "c_sales_now", "verbose": "C-売上高-今期" },
            { "field": "c_sales_next", "verbose": "C-売上高-来期" },
            { "field": "c_profit_previous", "verbose": "C-営業利益-前期" },
            { "field": "c_profit_now", "verbose": "C-営業利益-今期" },
            { "field": "c_profit_next", "verbose": "C-営業利益-来期" },
            { "field": "c_trust_val", "verbose": "C-信用買残" }
        ]
        for field_item in fields:
            self.check_char_field(field_item["field"], field_item["verbose"])

    def test_integer_fields(self):
        fields = [
            { "field": "a_positive_comment_one", "verbose": "A-ポジティブコメント数-1", "is_null": True },
            { "field": "a_negative_comment_one", "verbose": "A-ネガティブコメント数-1", "is_null": True },
            { "field": "a_positive_comment_two", "verbose": "A-ポジティブコメント数-2", "is_null": True },
            { "field": "a_negative_comment_two", "verbose": "A-ネガティブコメント数-2", "is_null": True },
            { "field": "a_shareholder_rank", "verbose": "A-株主順位", "is_null": False },
            { "field": "a_sales", "verbose": "A-営業CF", "is_null": True },
            { "field": "a_invest", "verbose": "A-投資CF", "is_null": True },
            { "field": "a_profit_updated", "verbose": "A-最高純益を更新", "is_null": False},
            { "field": "a_sales_comment_now", "verbose": "A-今期稼ぐ力", "is_null": False},
            { "field": "a_sales_comment_next", "verbose": "A-来期稼ぐ力", "is_null": False},
            { "field": "a_comment_chart", "verbose": "A-チャート", "is_null": False},
            { "field": "a_comment_ma", "verbose": "A-移動平均線", "is_null": False},
            { "field": "a_comment_compare", "verbose": "A-チャート-移動平均線", "is_null": False},
            { "field": "a_per_comment", "verbose": "A-PER-判定", "is_null": False},
            { "field": "a_peg_comment", "verbose": "A-PEG-判定", "is_null": False},
            { "field": "a_psr_comment", "verbose": "A-PSR-判定", "is_null": False},
            { "field": "b_positive_comment_one", "verbose": "B-ポジティブコメント数-1", "is_null": True },
            { "field": "b_negative_comment_one", "verbose": "B-ネガティブコメント数-1", "is_null": True },
            { "field": "b_positive_comment_two", "verbose": "B-ポジティブコメント数-2", "is_null": True },
            { "field": "b_negative_comment_two", "verbose": "B-ネガティブコメント数-2", "is_null": True },
            { "field": "b_shareholder_rank", "verbose": "B-株主順位", "is_null": False },
            { "field": "b_sales", "verbose": "B-営業CF", "is_null": True },
            { "field": "b_invest", "verbose": "B-投資CF", "is_null": True },
            { "field": "b_profit_updated", "verbose": "B-最高純益を更新", "is_null": False},
            { "field": "b_sales_comment_now", "verbose": "B-今期稼ぐ力", "is_null": False},
            { "field": "b_sales_comment_next", "verbose": "B-来期稼ぐ力", "is_null": False},
            { "field": "b_comment_chart", "verbose": "B-チャート", "is_null": False},
            { "field": "b_comment_ma", "verbose": "B-移動平均線", "is_null": False},
            { "field": "b_comment_compare", "verbose": "B-チャート-移動平均線", "is_null": False},
            { "field": "b_per_comment", "verbose": "B-PER-判定", "is_null": False},
            { "field": "b_peg_comment", "verbose": "B-PEG-判定", "is_null": False},
            { "field": "b_psr_comment", "verbose": "B-PSR-判定", "is_null": False},
            { "field": "c_positive_comment_one", "verbose": "C-ポジティブコメント数-1", "is_null": True },
            { "field": "c_negative_comment_one", "verbose": "C-ネガティブコメント数-1", "is_null": True },
            { "field": "c_positive_comment_two", "verbose": "C-ポジティブコメント数-2", "is_null": True },
            { "field": "c_negative_comment_two", "verbose": "C-ネガティブコメント数-2", "is_null": True },
            { "field": "c_shareholder_rank", "verbose": "C-株主順位", "is_null": False },
            { "field": "c_sales", "verbose": "C-営業CF", "is_null": True },
            { "field": "c_invest", "verbose": "C-投資CF", "is_null": True },
            { "field": "c_profit_updated", "verbose": "C-最高純益を更新", "is_null": False},
            { "field": "c_sales_comment_now", "verbose": "C-今期稼ぐ力", "is_null": False},
            { "field": "c_sales_comment_next", "verbose": "C-来期稼ぐ力", "is_null": False},
            { "field": "c_comment_chart", "verbose": "C-チャート", "is_null": False},
            { "field": "c_comment_ma", "verbose": "C-移動平均線", "is_null": False},
            { "field": "c_comment_compare", "verbose": "C-チャート-移動平均線", "is_null": False},
            { "field": "c_per_comment", "verbose": "C-PER-判定", "is_null": False},
            { "field": "c_peg_comment", "verbose": "C-PEG-判定", "is_null": False},
            { "field": "c_psr_comment", "verbose": "C-PSR-判定", "is_null": False},
        ]
        for field_item in fields:
            if field_item["is_null"]:
                self.check_integer_field(field_item["field"], field_item["verbose"], True)
            else:
                self.check_integer_field(field_item["field"], field_item["verbose"], False, -1)

    def test_decimal_fields(self):
        fields = [
            { "field": "a_capital_adequacy_ratio", "verbose": "A-自己資本比率", "max_digits": 5, "decimal": 1 },
            { "field": "a_pbr", "verbose": "A-PBR", "max_digits": 8, "decimal": 2 },
            { "field": "a_yield_percent", "verbose": "A-配当利回り", "max_digits": 5, "decimal": 2 },
            { "field": "a_expected_per", "verbose": "A-今期予想PER", "max_digits": 5, "decimal": 2 },
            { "field": "b_capital_adequacy_ratio", "verbose": "B-自己資本比率", "max_digits": 5, "decimal": 1 },
            { "field": "b_pbr", "verbose": "B-PBR", "max_digits": 8, "decimal": 2 },
            { "field": "b_yield_percent", "verbose": "B-配当利回り", "max_digits": 5, "decimal": 2 },
            { "field": "b_expected_per", "verbose": "B-今期予想PER", "max_digits": 5, "decimal": 2 },
            { "field": "c_capital_adequacy_ratio", "verbose": "C-自己資本比率", "max_digits": 5, "decimal": 1 },
            { "field": "c_pbr", "verbose": "C-PBR", "max_digits": 8, "decimal": 2 },
            { "field": "c_yield_percent", "verbose": "C-配当利回り", "max_digits": 5, "decimal": 2 },
            { "field": "c_expected_per", "verbose": "C-今期予想PER", "max_digits": 5, "decimal": 2 }
        ]
        for field_item in fields:
            self.check_decimal_field(
                field_item["field"],
                field_item["verbose"],
                field_item["max_digits"],
                field_item["decimal"],
            )

    def check_char_field(self, field_name, verbose_name):
        meta_data = self.sheet._meta.get_field(field_name)
        self.assertEqual(meta_data.verbose_name, verbose_name)
        self.assertEqual(meta_data.max_length, 255)
        self.assertEqual(meta_data.null, True)
        self.assertEqual(meta_data.blank, True)
        self.assertEqual(getattr(self.sheet, field_name), None)

    def check_integer_field(self, field_name, verbose_name, is_null=True, default_value=-1):
        meta_data = self.sheet._meta.get_field(field_name)
        self.assertEqual(meta_data.verbose_name, verbose_name)
        if is_null:
            self.assertEqual(meta_data.null, True)
            self.assertEqual(getattr(self.sheet, field_name), None)
        else:
            self.assertEqual(meta_data.default, default_value)
            self.assertEqual(getattr(self.sheet, field_name), default_value)
    
    def check_decimal_field(self, field_name, verbose_name, max_digits = 5, decimal_places = 2):
        meta_data = self.sheet._meta.get_field(field_name)
        self.assertEqual(meta_data.verbose_name, verbose_name)
        self.assertEqual(meta_data.null, True)
        self.assertEqual(meta_data.max_digits, max_digits)
        self.assertEqual(meta_data.decimal_places, decimal_places)

    def test_created_at(self):
        meta_data = self.sheet._meta.get_field('created_at')
        self.assertEqual(meta_data.verbose_name, '作成日時')
        self.assertEqual(meta_data.auto_now_add, True)
        self.assertEqual(meta_data.auto_now, False)

    def test_updated_at(self):
        meta_data = self.sheet._meta.get_field('updated_at')
        self.assertEqual(meta_data.verbose_name, '更新日時')
        self.assertEqual(meta_data.auto_now_add, False)
        self.assertEqual(meta_data.auto_now, True)

class TestView(TestCase):
    def setUp(self):        
        self.create_basic()
        self.create_industry()
        self.user = User.objects.create(email="test@gmail.com", username="test-user")
        self.user.set_password('password')
        self.user.save()
        self.token = self.get_token(self.user)
        self.sheet = Sheet.objects.create(
            title="sheet-1",
            user=self.user,
            stock_year=2022,
            stock_month=11,
            stock_day=1,
            finished_month = 12,
            finished_day = 1
        )

    def create_industry(self):
        self.industry = Industry.objects.create(
            name = 'IT',
            company_num = 10,
            sales_sum = "100000000",
            profit_sum = "10000000",
            extended_now = 1.3,
            extended_next = 1.7,
            order = "1"
        )

    def create_basic(self):
        self.basic = Ratio.objects.create(
            m_avg_per=1.00, m_cur_growth=1.00, m_next_growth=1.00,
            m_ratio = 1.00, p_avg_per = 1.00, p_cur_growth = 1.00, p_next_growth = 1.00, p_ratio = 1.00,
            is_active = True
        )

    def get_token(self, user):
        response = self.client.post(reverse('api_token_auth'), {
            'username': user.email,
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)
        login_resp = json.loads(response.content)
        return login_resp['token']

    def test_ratios_list(self):
        auth_header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.client.get(reverse('ratios_list'), **auth_header)
        self.assertEqual(response.status_code, 200)
        ratios_info = json.loads(response.content)
        self.assertLessEqual(1, len(ratios_info))
    
    def test_industries_list(self):
        auth_header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.client.get(reverse('industries_list'), **auth_header)
        self.assertEqual(response.status_code, 200)
        industries = json.loads(response.content)
        self.assertLessEqual(1, len(industries))

    def test_check_sheet_title(self):
        auth_header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.client.get(reverse('sheets_title_check'), {'id': self.sheet.id, 'title': self.sheet.title}, **auth_header)
        self.assertEqual(response.status_code, 200)
        res = json.loads(response.content)
        self.assertTrue(res)

    def test_sheet_list(self):
        auth_header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.client.get(reverse('sheets_view'), **auth_header)
        self.assertEqual(response.status_code, 200)
        sheets = json.loads(response.content)
        self.assertLessEqual(1, len(sheets))

    def test_sheet_create(self):
        auth_header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.client.post(reverse('sheets_view'), {
            "title": "new",
            "user_id": self.user.id,
            "stock_year": 2024,
            "stock_month": 1,
            "stock_day": 1,
            "finished_month": 12,
            "finished_day": 1,
            "a_profit_category_id": 0,
            "b_profit_category_id": 0,
            "c_profit_category_id": 0,
        }, **auth_header)
        self.assertEqual(response.status_code, 201)
        res = json.loads(response.content)
        self.assertLess(self.sheet.id, res["id"])
    
    def test_sheet_retrieve(self):
        auth_header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.client.get(
            reverse('sheets_detail_view', kwargs = { 'pk': self.sheet.id }), **auth_header)
        self.assertEqual(response.status_code, 200)
                
    def test_sheet_delete(self):
        auth_header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.client.delete(
            reverse('sheets_detail_view', kwargs = { 'pk': self.sheet.id }), **auth_header)
        self.assertEqual(response.status_code, 204)

        response = self.client.get(
            reverse('sheets_detail_view', kwargs = { 'pk': self.sheet.id }), **auth_header)
        self.assertEqual(response.status_code, 404)