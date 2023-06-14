# -*- coding:utf-8 -*-
from odoo import _, api, fields, models, tools


class PosOrder(models.Model):
    _inherit = "pos.order"
    
    config_id = fields.Many2one(
        'pos.config', string='Point of Sale',related='session_id.config_id',store=True) 