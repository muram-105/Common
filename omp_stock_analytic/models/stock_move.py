# -*- coding:utf-8 -*-
from odoo import _, api, fields, models, tools

class StockMove(models.Model):
    _name = "stock.move"
    _inherit = ["stock.move", "analytic.mixin"]

    def _prepare_account_move_line(
        self, qty, cost, credit_account_id, debit_account_id, svl_id, description
    ):
        self.ensure_one()
        res = super(StockMove, self)._prepare_account_move_line(
            qty, cost, credit_account_id, debit_account_id, svl_id, description
        )
       
       
        # if not self.analytic_distribution:
        #     return res
        for line in res:
            analytic_account = self.picking_id.picking_type_id.analytic_account_id.id
            if (
                line[2]["account_id"]
                != self.product_id.categ_id.property_stock_valuation_account_id.id
            ):
                line[2]['analytic_distribution'] = {}
                line[2]['analytic_distribution'][analytic_account] = analytic_account

              
        return res
