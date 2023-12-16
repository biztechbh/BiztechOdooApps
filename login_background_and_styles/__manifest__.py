# -*- encoding: utf-8 -*-
{
    'name': 'Login Background And Styles',
    'summary': 'The new configurable Odoo Web Login Screen',
    'version': '12.0.1.0.0',
    'category': 'website',
    'summary': """
    You can customised login page like add background image or color and change position of login form.
    """,
    'author': 'Biztech Computer',
    'maintainer': 'Biztech Computer',
    'website': 'https://biztechbh.biz',
    'license': 'AGPL-3',
    'depends': ['base', 'base_setup', 'web', 'auth_signup'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/login_image.xml',
        'templates/assets.xml',
        'templates/left_login_template.xml',
        'templates/right_login_template.xml',
        'templates/middle_login_template.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'images': ['static/description/icon.png'],
}

