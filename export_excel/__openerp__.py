# -*- coding: utf-8 -*-
{
    'name': 'Export a Excel',
    'version': '1',
    'category': 'Web',
    'description': """
WEB EXPORT VIEW
===============

Modulo que exporta a Excel las vista en tree
""",
    'author': 'Grupo Innova',
    'website': 'http://www.innovahn.com',
    'depends': [
        'web',
    ],
    'data': [
        'view/web_export_view.xml',
    ],
    'qweb': [
        'static/src/xml/web_export_view_template.xml',
    ],
    'installable': True,
    'auto_install': False,
}
