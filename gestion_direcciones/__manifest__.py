# -*- coding: utf-8 -*-
{
'name': "gestiondirecciones",

    'summary': """
        Módulo para el control de ips""",

    'description': """
        EL presente módulo .
    """,

    'author': "David",
    

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
      
        'views/menusyacciones.xml',
        'views/cita_gestionhospital.xml',
        'views/doctor_gestionhospital.xml',
        'views/especialidad_gestionhospital.xml',
        'views/paciente_gestionhospital.xml',
        'views/registroclinico_gestionhospital.xml',
        'views/sala_gestionhospital.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
