# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosConfig(models.Model):
    _inherit = 'pos.config'
    
    order_count = fields.Integer(compute="_compute_order_count")
    
    # @api.depends('order_count')
    def _compute_order_count(self):
        for record in self: 
            record['order_count'] = self.env['report.pos.order'].search_count([('config_id', '=', record.id)])

    


