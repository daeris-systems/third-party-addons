{
    'name': "Bank Autocomplete",
    'version': '1.0.0',
    'summary': 'Auto-complete bank data. SWIFT / BIC code, full name, branch, country and city. The dataset covers all the countries. The list contains more than 100 thousand banks. Quick search and completion.',
    'depends': ['base'],
    'author': "Sébastien Mottet",
    'license': "OPL-1",
    'category': 'Accounting',
    'description': """
        More than 100k pre-encoded banks.
    """,
    'images': ['static/description/banner.png'],
    'support': 'sebastien.mottet96@gmail.com',
    'installable': True,
    'post_init_hook': '_populate_res_bank',
}
