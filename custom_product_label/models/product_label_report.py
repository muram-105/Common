# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict

from odoo import _, models
from odoo.exceptions import UserError


class ReportProductLabel45x45(models.AbstractModel):
    _name = 'report.custom_product_label.report_producttemplate45x45label'
    _description = 'Product Label Report'

    def _get_report_values(self, docids, data):
        # change product ids by actual product object to get access to fields in xml template
        # we needed to pass ids because reports only accepts native python types (int, float, strings, ...)
        if data.get('active_model') == 'product.template':
            Product = self.env['product.template'].with_context(display_default_code=False)
        elif data.get('active_model') == 'product.product':
            Product = self.env['product.product'].with_context(display_default_code=False)
        else:
            raise UserError(_('Product model not defined, Please contact your administrator.'))

        total = 0
        qty_by_product_in = data.get('quantity_by_product')
        # search for products all at once, ordered by name desc since popitem() used in xml to print the labels
        # is LIFO, which results in ordering by product name in the report
        products = Product.search([('id', 'in', [int(p) for p in qty_by_product_in.keys()])], order='name desc')
        quantity_by_product = defaultdict(list)
        for product in products:
            q = qty_by_product_in[str(product.id)]
            quantity_by_product[product].append((product.barcode, q))
            total += q
        if data.get('custom_barcodes'):
            # we expect custom barcodes format as: {product: [(barcode, qty_of_barcode)]}
            for product, barcodes_qtys in data.get('custom_barcodes').items():
                quantity_by_product[Product.browse(int(product))] += (barcodes_qtys)
                total += sum(qty for _, qty in barcodes_qtys)

        layout_wizard = self.env['product.label.layout'].browse(data.get('layout_wizard'))
        if not layout_wizard:
            return {}
        return {
            'quantity': quantity_by_product,
            'print_format':data.get('print_format'),
            'page_numbers': total,
            'price_included': data.get('price_included'),
            'extra_html': layout_wizard.extra_html,
        }

class ReportProductLabel38x25(models.AbstractModel):
    _name = 'report.custom_product_label.report_producttemplate38x25label'
    _description = 'Product Label Report'

    def _get_report_values(self, docids, data):
        # change product ids by actual product object to get access to fields in xml template
        # we needed to pass ids because reports only accepts native python types (int, float, strings, ...)
        if data.get('active_model') == 'product.template':
            Product = self.env['product.template'].with_context(display_default_code=False)
        elif data.get('active_model') == 'product.product':
            Product = self.env['product.product'].with_context(display_default_code=False)
        else:
            raise UserError(_('Product model not defined, Please contact your administrator.'))

        total = 0
        qty_by_product_in = data.get('quantity_by_product')
        # search for products all at once, ordered by name desc since popitem() used in xml to print the labels
        # is LIFO, which results in ordering by product name in the report
        products = Product.search([('id', 'in', [int(p) for p in qty_by_product_in.keys()])], order='name desc')
        quantity_by_product = defaultdict(list)
        for product in products:
            q = qty_by_product_in[str(product.id)]
            quantity_by_product[product].append((product.barcode, q))
            total += q
        if data.get('custom_barcodes'):
            # we expect custom barcodes format as: {product: [(barcode, qty_of_barcode)]}
            for product, barcodes_qtys in data.get('custom_barcodes').items():
                quantity_by_product[Product.browse(int(product))] += (barcodes_qtys)
                total += sum(qty for _, qty in barcodes_qtys)

        layout_wizard = self.env['product.label.layout'].browse(data.get('layout_wizard'))
        if not layout_wizard:
            return {}
        return {
            'quantity': quantity_by_product,
            'print_format':data.get('print_format'),
            'page_numbers': total,
            'price_included': data.get('price_included'),
            'extra_html': layout_wizard.extra_html,
        }