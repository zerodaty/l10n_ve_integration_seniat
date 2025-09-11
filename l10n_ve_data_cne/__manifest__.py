# -*- coding: utf-8 -*-
{
    'name': "l10n_ve_data_cne",

    'summary': 
        """
        Módulo base que almacena los datos del Registro Civil y la división
        geopolítica de Venezuela para ser consumido por otros módulos.
        """,

    'description': 
        """
        - Crea los modelos para Estados, Municipios, Parroquias, Centros CNE.
        - Crea el modelo principal para el Registro Civil.
        - No contiene vistas de menú, es un módulo técnico de base.
        """,

    'author': "Frany Velasquez",
    'license': 'AGPL-3',
    'website': "https://github.com/zerodaty/l10n_ve_integration_cedula",
    'category': 'Localization',
    'version': '18.0.1.0.0',

    'depends': [
        'base'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
    ],
    
    'installable': True,
    'application': False,
    'auto_install': False,
}

