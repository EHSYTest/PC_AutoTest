import pytest, random, sys
sys.path.append('../Page')
from Page_Base import Page


sql = "SELECT SKU_CODE, promotion_value FROM pc.promotion_sku WHERE promotion_id IN(SELECT id FROM pc.promotion WHERE TYPE='1' AND promotion_type='1' AND `status`='1' and CURRENT_DATE BETWEEN start_date AND end_date ) AND CURRENT_DATE BETWEEN start_date AND end_date"
page = Page('driver')
cr = page.db_con('staging')
cr.execute(sql)
r = cr.fetchall()
result = random.choice(r)
print(r, result)
sku = result['SKU_CODE']
promotion_price = str(result['promotion_value'])
sql = "SELECT market_price FROM pc.price WHERE CURRENT_DATE BETWEEN valid_time_start AND valid_time_end AND sku_code='"+sku+"'"
cr.execute(sql)
r = cr.fetchall()
print(r)
market_price = str(r[0]['market_price'])
print({'sku': sku, 'promotion_price': promotion_price, 'market_price': market_price})