import unittest, sys
sys.path.append('../Page')
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from Page_Base import Page
from Page_NormalCart import NormalCart
from Page_Home import Home
from Page_ProductList import ProductList
import pytest, allure

driver = 1
sql = "select a.ORDER_ID from oc.order_info a where a.EXTERNAL_ORDER_NO='PR2018061220261792100'"
sql_result = Page(driver).db_con('production', sql)
SO = sql_result[0]['ORDER_ID']
print(SO)