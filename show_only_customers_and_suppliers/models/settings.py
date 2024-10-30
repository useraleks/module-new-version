# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class ResCompany(models.Model):
    _inherit = 'res.company'

    tag_to_show_id = fields.Many2many(
        comodel_name='res.partner.category',
        string="filter by",
        readonly=False
    )

class Settings(models.TransientModel):
    _inherit = 'res.config.settings'

    show_only_customers = fields.Boolean(string="Filter and show only customers in sales")
    tag_to_show_id = fields.Many2many(
        comodel_name='res.partner.category',
        string="filter by",
        related='company_id.tag_to_show_id',
        readonly=False
    )
    
    @api.model
    def set_values(self):
        ICP = self.env['ir.config_parameter'].sudo()
        ICP.set_param('show_only_customers_and_suppliers.show_only_customers', self.show_only_customers)
        super(Settings, self).set_values()

    @api.model
    def get_values(self):
        ICP = self.env['ir.config_parameter'].sudo()
        res = super(Settings, self).get_values()
        res['show_only_customers'] = bool(ICP.get_param('show_only_customers_and_suppliers.show_only_customers'))
        return res