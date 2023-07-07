# -*- coding:utf-8  -*-
from odoo import _, api, fields, models, tools

class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'
    
    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account')

    
    