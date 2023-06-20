# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.tools import format_amount

class ProductProduct(models.Model):
    _inherit = 'product.product'


    
    color_id= fields.Char("Color ID",)
    material = fields.Char("Material ID",)
    no_of_pieces = fields.Integer("Number of Pieces",)



class ProductTemplate(models.Model):
    _inherit = "product.template"

    color_id= fields.Char("Color ID",)
    material = fields.Char("Material ID",)
    no_of_pieces = fields.Integer("Number of Pieces",)
