# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def get_default_show_only_suppliers(self):
        ICP = self.env['ir.config_parameter'].sudo()
        show_only_suppliers = ICP.get_param('show_only_customers_and_suppliers.show_only_suppliers')
        return show_only_suppliers
    
    show_only_suppliers = fields.Boolean(string="show only suppliers", default=get_default_show_only_suppliers)
    tag_to_show_id = fields.Many2many(
        comodel_name='res.partner.category',
        string="filter by",
        related='company_id.to_show_id_po',
        readonly=False
    )
    
    @api.onchange('show_only_suppliers')
    def filter_by_suppliers(self):
        for rec in self:
            if rec.show_only_suppliers:
                return {'domain': {'partner_id': [('category_id', 'in', rec.tag_to_show_id.ids)]}}
            else:
                return {'domain': {'partner_id': []}}