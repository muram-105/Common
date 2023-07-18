# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, models


class AccountChartTemplate(models.Model):
    _inherit = 'account.chart.template'

    def process_coa_translations(self):
        res = super(AccountChartTemplate, self).process_coa_translations()
        installed_langs = dict(self.env['res.lang'].get_installed())
        company_obj = self.env['res.company']
        if self.id == self.env.ref("l10n_me.l10nme_chart_template").id:
            for chart_template_id in self:
                langs = []
                if chart_template_id.spoken_languages:
                    for lang in chart_template_id.spoken_languages.split(';'):
                        if lang not in installed_langs:
                            # the language is not installed, so we don't need to load its translations
                            continue
                        else:
                            langs.append(lang)
                    if langs:
                        company_ids = company_obj.search([])
                        for company in company_ids:
                            chart_template_id._process_accounts_reconcile_translations(company.id, langs, 'name')
        return True

    def _process_accounts_reconcile_translations(self, company_id, langs, field):
        r_in_ids , r_out_ids = self._get_template_from_model(company_id, 'account.reconcile.model')
        return self.process_translations(langs, field, r_in_ids, r_out_ids)


