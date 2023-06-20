# -*- coding: utf-8 -*-

from odoo import api, models, fields, _

class Documents(models.Model):
    _inherit = 'documents.document'

    partner_workspace_id = fields.Many2one('documents.folder',string='Customer Workspace',
    default=lambda self: self.env['ir.config_parameter'].sudo().get_param('nm_reception_treatment_unit.partner_workspace_id')
    )

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _get_workspace(self):
        params = self.env['ir.config_parameter'].sudo()
        folder = params.get_param('nm_reception_treatment_unit.partner_workspace_id')	

    def action_open_documents(self):
        workspace = self._get_workspace()
        action = self.env['ir.actions.act_window']._for_xml_id('nm_partner_documents_workspace.customer_document_action')
        action['context'] = {
            'search_default_partner_id': self.id,
            'default_partner_id': self.id,
            'searchpanel_default_folder_id': workspace,
        }
        action['domain'] = [('partner_id', '=', self.id)]
        return action