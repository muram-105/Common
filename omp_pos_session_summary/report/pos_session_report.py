# -*- coding:utf-8 -*-
from odoo import models, fields, api, _


class PosSessionReport(models.AbstractModel):
    _name = 'report.omp_pos_session_summary.session_summary_template'

    @api.model
    def _get_report_values(self, docids, data=None):
        session = self.env['pos.session'].browse(docids)

        total_sales_amount = session.total_payments_amount
        po_payment = self.env['pos.payment'].search([('session_id', '=', session.id)])
        payment_method = po_payment.mapped('payment_method_id')
        summary_by_payment_method = []
        for rec in payment_method:
            summary_by_payment_method.append({
                'payment_method': rec.name,
                # 'amount': sum(r.amount for r in po_payment if r.payment_method_id.name == rec.name)
                'amount': round(sum(r.amount for r in po_payment if r.payment_method_id.name == rec.name), 2)

            })

        return {
            'doc_ids': docids,
            'docs': session,
            'session': session.name,
            'responsible': session.config_id.name,
            'open_by': session.user_id.name,
            'opening_date': session.start_at,
            'opening_balance': session.cash_register_balance_start,
            'closing_balance': session.cash_register_balance_end_real,
            'closing_date': session.stop_at,
            'total_sales_amount': total_sales_amount,
            'summary_by_payment_method': summary_by_payment_method
        }
