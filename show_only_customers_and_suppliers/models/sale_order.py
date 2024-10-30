# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    show_only_customers = fields.Boolean(
        string="Show Only Customers", 
        default=lambda self: self.env['ir.config_parameter'].sudo().get_param('show_only_customers_and_suppliers.show_only_customers')
    )
    tag_to_show_id = fields.Many2many(
        comodel_name='res.partner.category',
        string="Filter by",
        related='company_id.tag_to_show_id',
        readonly=False
    )

    @api.model
    def default_get(self, fields_list):
        res = super(SaleOrder, self).default_get(fields_list)
        if res.get('show_only_customers'):
            tags = self.env['res.partner.category'].browse(res.get('tag_to_show_id'))
            res['partner_id'] = self.env['res.partner'].search([('category_id', 'in', tags.ids)]).ids
        return res
