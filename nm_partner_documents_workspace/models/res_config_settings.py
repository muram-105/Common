# -*- coding:utf-8-*-
from odoo import _, api, fields, models, tools


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    partner_workspace_id = fields.Many2one('documents.folder',string='Customer Workspace',
    config_parameter='nm_reception_treatment_unit.partner_workspace_id',
    )


