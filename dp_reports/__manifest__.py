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
        'base'
    ],
    'data': [
        'data/paperformat.xml',
        'reports/report_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'auto_install': False,
}
