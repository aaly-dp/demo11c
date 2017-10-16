# -*- coding: utf-8 -*-

# noinspection PyStatementEffect
{
    'name': 'datepol Report-Anpassungen',
    'category': 'Custom',
    'version': '1.0',
    'summary': """Individuelle Report Anpassungen""",
    'description': """Individuelle Report Anpassungen""",
    'author': 'datenpol gmbh',
    'website': 'http://www.datenpol.at/',
    'depends': [
        'dp_reports',
        'purchase'
    ],
    'data': [
        'reports/purchase.xml',
        'reports/purchasequotation.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'auto_install': False,
}
