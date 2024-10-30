# -*- coding: utf-8 -*-
{
    'name': "Show and filter only customers and suppliers",
    'summary': """show only customers and suppliers in sales and purchases""",
    'description': """
        - you can filter sales only by customers
        - you can filter only suppliers in purchases
        - In Sales > Clients you can make only clients appear
        - In Purchase > Suppliers you can make only supplier appear
        """,
    'author': "WitLinkGT, Alexander E.P",
    'price': 19.00,
    'currency': "USD",
    'website': "",
    "images": [#'static/description/banner.png',
               #'static/description/icon.png',
               #'static/description/thumbnail.png'
               ],
    "license": 'OPL-1',
    'category': 'Contacts',
    'version': '3.5',
    'depends': ['base',
                'sale_management',
                'contacts',
                'purchase',
                'account',],
    'data': [
        'views/settings.xml',
        'views/settings_sale.xml',
        'views/sale_action.xml',
        'views/purchase_action.xml',
        'views/sale_order.xml',
        'views/purchase_order.xml',
    ],
    'demo': [
        # 'demo.xml',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}