import os, json
from odoo import api, SUPERUSER_ID

def _populate_res_bank(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    path_to_json =  os.path.dirname(__file__)+'/data/SWIFT_codes/'
    country_code = ''
    banks = []
    for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
        with open(path_to_json + file_name) as json_file:
            data = json.load(json_file)
            country_code = data.get('country_code', '')
            country = env['res.country'].search([('code', '=', country_code)], limit=1)
            country_id = country.id if country.exists() else None
            bank_list = data.get('list', [])
            for bank in bank_list:
                name = bank.get('bank')
                branch = bank.get('branch')
                if branch:
                    name += ' '  + branch
                new_bank = {
                    'name': name,
                    'bic': bank.get('swift_code'),
                    'city': bank.get('city'),
                    'country': country_id,
                }
                banks.append(new_bank)
    env['res.bank'].create(banks)