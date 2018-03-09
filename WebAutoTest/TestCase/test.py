from selenium import webdriver
import unittest
from Page_Base import Page
from xmlrpc import client


dbname = 'odoo-staging'
usr = 'admin'
pwd = 'admin'
# oe_ip = 'odoo-staging.ehsy.com'
oe_ip = 'localhost:8069'

vals = {'ks_no': 'KS2018030763'}

sock_common = client.ServerProxy('http://' + oe_ip + '/xmlrpc/common')
uid = sock_common.login(dbname, usr, pwd)
sock = client.ServerProxy('http://' + oe_ip + '/xmlrpc/object')
result = sock.execute(dbname, uid, pwd, 'used.by.tester', 'so_invoice', vals)
print(result)
