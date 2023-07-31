# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Estate',
    # 'sequence': 15,
    # 'summary': 'Track leads and close opportunities',
    # 'description': "",
    # 'website': 'https://www.odoo.com/page/crm',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',

        # 'demo': [
        #     'data/crm_team_demo.xml',
        #     'data/mail_activity_demo.xml',
        #     'data/crm_lead_demo.xml',
    ],
    # 'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    'auto_install': False
}
