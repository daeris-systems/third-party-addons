# Copyright 2018-2021 datenpol gmbh (<https://www.datenpol.at/>)
# License OPL-1 or later (https://www.odoo.com/documentation/15.0/legal/licenses.html).

# noinspection PyStatementEffect
{
    'name': """DP EU-GDPR""",
    'summary': """General Data Protection Regulation""",
    'description': """DSGVO, EU-DSGVO, GDPR, EU-GDPR, General Data Protection Regulation, Dateschutzgrundverordnung, Datenschutz-Grundverordnung, RGPD, Règlement général sur la protection des données, Right of Access, Right to rectification, Right to erasure, Right to restriction of processing, Right to data portability, Right to object""",
    'category': 'Extra Tools',
    'version': '15.0.1.0.0',
    'license': 'OPL-1',
    'author': 'datenpol gmbh',
    'support': 'office@datenpol.at',
    'website': 'https://www.datenpol.at/',
    'depends': [
        'base',
        'mail_bot',
    ],
    'data': [
        'data/sequence.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/eu_gdpr_log_views.xml',
        'wizards/eu_gdpr.xml',
    ],
    'images': ['static/description/Banner.jpg'],
    'assets': {
        'web.assets_backend': [
            'dp_eu_gdpr/static/src/css/style.css',
        ]
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
