# -*- coding: utf-8 -*-

from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'
    cnae_code = fields.Char(string='Código CNAE',help='Codigo de CNAE al que se acoge la empresa. Se puede averiguar mediante el buscador de actividades de la agencia tributaria española',required=False)
    cnae_name = fields.Char(string='Descripción CNAE',help='Nombre de CNAE al que se acoge la empresa. Se puede averiguar mediante el buscador de actividades de la agencia tributaria española',required=False)
    cnae_coef_it = fields.Float(string='Tarifa CNAE IT',help='Prima incapacidad temporal en base al CNAE',required=False)
    cnae_coef_ims = fields.Float(string='Tarifa CNAE IMS',help='Prima incapacidad permanente, muerte y supervivencia  en base al CNAE',required=False)
    ssnid = fields.Char(string='Nº Seguridad Social', help='Numero de inscripción a la seguridad social',required=False)
