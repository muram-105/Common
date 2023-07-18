# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ReSequenceWizard(models.TransientModel):
    _inherit = 'account.resequence.wizard'
    _description = 'Remake the sequence of Journal Entries.'


    def resequence(self):
        return super(ReSequenceWizard, self.with_context(pass_validation=True)).resequence()