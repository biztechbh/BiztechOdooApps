
# -*- coding: utf-8 -*-
{
    'name': 'Preview Purchase History',
    'version': '16.0',
    'summary': "Preview Purchase History",
    'sequence': 16,
    'description': """It shows purchase history of product in purchase line""",
    'category': 'purchase',
    'author': 'Biztech Computer',
    'maintainer': 'Biztech Computer',
    'website': 'https://biztechbh.biz',
    'depends': ['account', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/purchase_line_wiz.xml',
        'view/purchase_custom.xml'
    ],

    'demo': [],
    'license': 'AGPL-3',
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
