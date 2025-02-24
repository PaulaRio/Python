# -*- coding: utf-8 -*-
{
    'name': "libreria",

    'summary': "modulo para gestionar una biblioteca",

    'description': """
Long description of module's purpose
    """,

    'author': "Ruben SF",
    'website': "https://www.iescomercio.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views_categoria.xml',
        'views/views_libro.xml',
        'views/views_menu.xml',
        'reports/report_libro.xml',
        'reports/ir_actions_report.xml',
        'data/data.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
    'application': True,
}

