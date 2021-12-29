# -*- coding:utf-8 -*-
from odoo import api, fields, models
class HrContract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Employee Contract'
    struct_id = fields.Many2one('hr.payroll.structure', string='Salary Structure')
    schedule_pay = fields.Selection([
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('semi-annually', 'Semi-annually'),
        ('annually', 'Annually'),
        ('weekly', 'Weekly'),
        ('bi-weekly', 'Bi-weekly'),
        ('bi-monthly', 'Bi-monthly'),
    ], string='Scheduled Pay', index=True, default='monthly', help="Defines the frequency of the wage payment.")
    type_id = fields.Many2one('hr.contract.type', string="Contribution group",required=True, help="Employee Contribution group",default=lambda self: self.env['hr.contract.type'].search([], limit=1))

    resource_calendar_id = fields.Many2one(required=True, help="Employee's working schedule.")
    professional_group = fields.Text(string='profesional group',help='In spain, is mandatory appears profesional group over payroll')
    base_max_cotizacion = fields.Monetary(string='Quote - Maximum basis', required=False, help="Maximum base to perform the BCC base calculation")#digits=(8, 2),
    base_min_cotizacion = fields.Monetary(string='Quote - Minimum basis', required=False, help="Minimum basis to perform the BCC basis calculation")#, digits=(8, 2)
    plus_conv = fields.Monetary(string='Plus agreement', required=False, tracking=True, help="Plus agreement to incorporate in payroll")#, digits=(16, 2)
    antiguedad = fields.Monetary(string='Seniority', required=False, tracking=True, help="Seniority to be included in the payroll")#, digits=(16, 2)
    complemento_salarial = fields.Monetary(string='Salary supplement', required=False, tracking=True, help="Value of the salary supplement to be incorporated in payroll")#, digits=(16, 2)
    contingencias_com = fields.Float(string='Common contingencies',required=False,help="Common contingencies")#, digits=(16, 4)
    desempleo = fields.Float(string='Unemployment',required=False,help="Unemployment")#, digits=(16, 4)
    formacion_prof = fields.Float(string='Professional training',required=False,help="Professional training")#, digits=(16, 4)
    dias_contrato = fields.Float(string='Contract days',required=False,help="Number of days of the contract. If the contract is indefinite, it must be informed with 30 days",default=30)#, digits=(6, 2)
    jornada_laboral = fields.Float(string='% Workday',required=False,help="Percentage of working hours in the case of taking advantage of reduced working hours",default=100)#, digits=(5, 2)
    irpf = fields.Float(string='IRPF',required=False,help="IRPF")#, digits=(16, 4)
    tickets_comida = fields.Monetary(string='Restaurant tickets', required=False, tracking=True, help="Daily ticket value")#, digits=(16, 2)
    seguro_vida = fields.Monetary(string='Life insurance', required=False, tracking=True, help="Monthly life insurance cost")#, digits=(16, 2)
    seguro_medico = fields.Monetary(string='Health insurance', required=False, tracking=True, help="Cost of monthly health insurance")#, digits=(16, 2)
    precio_km = fields.Monetary(string='Price/Km', required=False, tracking=True, help="Cost of the km traveled")#, digits=(16, 2)
    h_extra_dia_laboral = fields.Monetary(string='Extra hour business day', required=False, tracking=True, help="Extra hour price on business day")#, digits=(16, 2)
    h_extra_noche_laboral = fields.Monetary(string='Extra hour business night', required=False, tracking=True, help="Extra hour price on business night")#, digits=(16, 2)
    h_extra_dia_festivo = fields.Monetary(string='Extra hour holiday day', required=False, tracking=True, help="Extra hour price on holiday day")#, digits=(16, 2)
    h_extra_noche_festivo = fields.Monetary(string='Extra hour holiday night', required=False, tracking=True, help="Extra hour price on holiday night")#, digits=(16, 2)
    guardia_dia_laboral = fields.Monetary(string='Dia guardia laboral', required=False, tracking=True, help="Coste de un dia de guardia en laboral")#, digits=(16, 2)
    guardia_dia_festivo = fields.Monetary(string='Dia guardia festivo', required=False, tracking=True, help="Coste de un dia de guardia en festivo")#, digits=(16, 2)
    num_pagas_extras = fields.Float(string='Nº extraordinary payments',required=False,help="Number of extraordinary payments")#, digits=(2,0)
    proratear_pagas = fields.Boolean(string='¿Prorated payments?',required=False,help="Prorate the extra payments on the payroll, month by month")

    def get_all_structures(self):
        structures = self.mapped('struct_id')
        if not structures:
            return []
        return list(set(structures._get_parent_structure().ids))

    def get_attribute(self, code, attribute):
        return self.env['hr.contract.advantage.template'].search([('code', '=', code)], limit=1)[attribute]

    def set_attribute_value(self, code, active):
        for contract in self:
            if active:
                value = self.env['hr.contract.advantage.template'].search([('code', '=', code)], limit=1).default_value
                contract[code] = value
            else:
                contract[code] = 0.0

class HrContractAdvandageTemplate(models.Model):
    _name = 'hr.contract.advantage.template'
    _description = "Employee's Advantage on Contract"

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    lower_bound = fields.Float('Lower Bound', help="Lower bound authorized by the employer for this advantage")
    upper_bound = fields.Float('Upper Bound', help="Upper bound authorized by the employer for this advantage")
    default_value = fields.Float('Default value for this advantage')