# -*- coding: utf-8 -*-
{
    'name': "l10n_ve_integration_cedula",

    'summary': 
        """
        Autocompleta los datos de contactos (partners) utilizando una API 
        externa a partir de la Cédula de Identidad o RIF.
        """,

    'description': 
        """
        Autocompleta los datos de contactos (partners) utilizando una API
        externa a partir de la Cédula de Identidad o RIF.
        """,

    'author': "Frany Velasquez",
    'license': 'AGPL-3',
    'website': "https://github.com/zerodaty/l10n_ve_integration_cedula",

    'category': 'Localization/Venezuela',
    'version': '18.0.1.0.0',

    'depends': [
        'base',
        'contacts'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    
    'installable': True,
    'application': False,
    'auto_install': False,
}

