# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class ContractType(models.Model):
    _name = 'hr.contract.type'
    _description = 'Contract contribution group'
    _order = 'sequence, id'

    name = fields.Char(string='Contract contribution group', required=True, help="Contract contribution group")
    sequence = fields.Integer(help="Gives the sequence when displaying a list of Contract contribution group.", default=10)