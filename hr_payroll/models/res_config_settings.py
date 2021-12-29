# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    module_account_accountant = fields.Boolean(string='Account Accountant')
    #module_l10n_fr_hr_payroll = fields.Boolean(string='French Payroll')
    #module_l10n_be_hr_payroll = fields.Boolean(string='Belgium Payroll')
    #module_l10n_in_hr_payroll = fields.Boolean(string='Indian Payroll')
    generate_payslip = fields.Boolean(help="Automatic generation of payslip batches"
                                           " and payslips using cron job (Monthly)")
    option = fields.Selection([
        ('first', 'Month First'),
        ('specific', 'Specific date'),
        ('end', 'Month End'),
    ], string='Option', default='first', help='Option to select the date to generate payslips')
    generate_day = fields.Integer(string="Day", default=1,
                                  help="payslip generated day in a month")
    @api.model
    def get_values(self):
        """get values from the fields"""
        res = super(ResConfigSettings, self).get_values()
        res.update(
            generate_payslip=self.env['ir.config_parameter'].sudo().get_param('generate_payslip'),
            generate_day=int(self.env['ir.config_parameter'].sudo().get_param('generate_day') or 1),
            option=self.env['ir.config_parameter'].sudo().get_param('option') or 'first'
        )
        return res

    def set_values(self):
        """Set values in the fields"""
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('generate_payslip', self.generate_payslip)
        self.env['ir.config_parameter'].sudo().set_param('generate_day', int(self.generate_day))
        self.env['ir.config_parameter'].sudo().set_param("option", self.option)