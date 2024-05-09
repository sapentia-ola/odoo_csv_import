# -*- coding: utf-8 -*-
from odoo_csv_tools.lib import mapper
from odoo_csv_tools.lib.transform import Processor

# Custom import
from datetime import datetime   # used to change the format of datetime fields

processor = Processor('data-bank.csv', delimiter=';')

res_partner_mapping = {    
    'id': mapper.m2o_map('my_import_res_bank', mapper.concat('_', 'name')),
    'name': mapper.val('name'),
    'active': mapper.val('active'),
    }

processor.process(res_partner_mapping, 'res.bank.csv', {'model': 'res.bank', 'context': "{'tracking_disable': True}", 'worker': 2, 'batch_size': 20})
processor.write_to_file("res_bank.sh", python_exe='', path='')