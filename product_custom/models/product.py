# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.tools import format_amount

class ProductProduct(models.Model):
    _inherit = 'product.product'


    dry_clean = fields.Boolean("Dry Cleaning",default=False)
    machine_wash = fields.Boolean("Machine Washing", default=False)
    hand_wash = fields.Boolean("Hand Washing", default=False)
    iron = fields.Boolean("Ironing", default=False)
    instruction = fields.Text("Care Instructions")
    warning = fields.Text("Warnings")
    color_id= fields.Char("Color ID",)
    size_id = fields.Char("Size ID",)
    material_id = fields.Char("Material ID",)
    design_id = fields.Char("Design ID",)
    theme_id = fields.Char("Theme ID",)



class ProductTemplate(models.Model):
    _inherit = "product.template"

    dry_clean = fields.Boolean("Dry Cleaning",default=False)
    machine_wash = fields.Boolean("Machine Washing", default=False)
    hand_wash = fields.Boolean("Hand Washing", default=False)
    iron = fields.Boolean("Ironing", default=False)
    instruction = fields.Text("Care Instructions")
    warning = fields.Text("Warnings")
    color_id= fields.Char("Color ID",)
    size_id = fields.Char("Size ID",)
    material_id = fields.Char("Material ID",)
    design_id = fields.Char("Design ID",)
    theme_id = fields.Char("Theme ID",)
