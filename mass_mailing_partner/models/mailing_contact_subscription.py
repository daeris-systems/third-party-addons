# Copyright 2018 Tecnativa - Ernesto Tejeda
# Copyright 2020 Tecnativa - Manuel Calero
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, models
from odoo.exceptions import ValidationError


class MailingContactSubscription(models.Model):
    _inherit = "mailing.contact.subscription"

    @api.constrains("contact_id", "list_id")
    def _check_contact_id_partner_id_list_id(self):
        for rel in self:
            if rel.contact_id.partner_id:
                contacts = rel.list_id.contact_ids - rel.contact_id
                if rel.contact_id.partner_id in contacts.mapped("partner_id"):
                    raise ValidationError(
                        _("A partner cannot be multiple times in the same list")
                    )

    @api.model
    #Si la lista dispone de la marca de creación del contacto, procedemos a crearlo
    def create(self, vals):
        record = self.new(vals)
        if record.list_id.partner_mandatory and not record.contact_id.partner_id:
            m_partner = self.env["res.partner"]
            partner_vals = {'name': record.contact_id.display_name,'email': record.contact_id.email_normalized ,'category_id': record.list_id.partner_category}
            record.contact_id.partner_id = m_partner.sudo().create(partner_vals)
        return super().create(vals)
