# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2018 Odoo IT now <http://www.odooitnow.com/>
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Website Pre Loader',
    'category': 'Website',
    'summary': 'Website Pre Loader',

    'version': '0.1',
    'description': """
Website Pre Loader
==================
This module allows Pre Loader when page takes time to load in the website.
        """,

    'author': 'Odoo IT now',
    'website': 'http://www.odooitnow.com/',
    'license': 'AGPL-3',

    'depends': [
        'web','daeris_saas'
        ],
    'data': [
        'views/website_preloader_templates.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'website_loader_oin/static/src/css/website_preloader.css',
        ],
    },
    'images': ['images/OdooITnow_screenshot.png'],
    'price': 0.0,
    'currency': 'EUR',
    'installable': True,
    'application': False
}
