# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class ResCompanyPo(models.Model):
    _inherit = 'res.company'

    to_show_id_po = fields.Many2many(
        comodel_name='res.partner.category',
        string="filter by",
        relation='company_res_partner_category_rel',
        column1='company_id',
        column2='partner_category_id',
        readonly=False)

class SettingsPo(models.TransientModel):
    _inherit = 'res.config.settings'

    tag_to_show_id_po = fields.Many2many(
        comodel_name='res.partner.category',
        string="filter by",
        related='company_id.to_show_id_po',
        readonly=False
    )
    
    show_only_suppliers = fields.Boolean(string="Filter and show only suppliers in purchase order")

    @api.model
    def set_values(self):
        ICP = self.env['ir.config_parameter'].sudo()
        ICP.set_param('show_only_customers_and_suppliers.show_only_suppliers', self.show_only_suppliers)
        super(SettingsPo, self).set_values()

    @api.model
    def get_values(self):
        ICP = self.env['ir.config_parameter'].sudo()
        res = super(SettingsPo, self).get_values()
        res['show_only_suppliers'] = bool(ICP.get_param('show_only_customers_and_suppliers.show_only_suppliers'))
        return res