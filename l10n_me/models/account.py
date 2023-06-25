# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class AccountAccount(models.Model):
    _inherit = 'account.account'
    
    @api.onchange('account_type')
    def _onchange_account_type(self):
        super(AccountAccount, self)._onchange_account_type()
        if self.internal_group == 'income':
            self.tax_ids = False
        elif self.internal_group == 'expense':
            self.tax_ids = False

class AccountJournal(models.Model):
    _inherit = "account.journal"
    
    invoice_reference_type = fields.Selection(selection_add=[('origin', 'Based on Source Document'),
                                                             ('sale', 'Based on Sale Order #.')], ondelete={'origin': 'set default','sale': 'set default'})
    
    @api.model
    def _fill_missing_values(self, vals):
        acc_template_ref = self.env.context.get('acc_template_ref')
        company_chart = self.company_id.chart_template_id
        if self.env.context.get('from_act') :
            if vals['type'] == 'cash':
                vals['default_account_id'] = vals.get('default_account_id',acc_template_ref.get(self.env.ref('l10n_me.account_account_cash'))).id
            if vals['type'] == 'bank':
                vals['default_account_id'] = vals.get('default_account_id',acc_template_ref.get(self.env.ref('l10n_me.account_account_template_bank_1'))).id
        return super(AccountJournal, self)._fill_missing_values(vals)
    
class AccountChartTemplate(models.Model):
    _inherit = "account.chart.template"
    
    @api.model
    def _create_cash_discount_loss_account(self, company, code_digits):
        acc = self.env['account.account'].create({
            'name': _("Cash Discount Loss"),
            'code': 51000032,
            'account_type': 'expense',
            'company_id': company.id,
        })
        acc._update_field_translations('name', {'ar_001': 'خسارة الخصم النقدي'})
        return acc

    @api.model
    def _create_cash_discount_gain_account(self, company, code_digits):
        acc = self.env['account.account'].create({
            'name': _("Cash Discount Gain"),
            'code': 42000004,
            'account_type': 'income_other',
            'company_id': company.id,
        })
        acc._update_field_translations('name', {'ar_001': 'كسب الخصم النقدي'})
        return acc
    
    def generate_account_reconcile_model(self, tax_template_ref, acc_template_ref, company):
        return super(AccountChartTemplate, self.with_context(sequence=8)).generate_account_reconcile_model(tax_template_ref, acc_template_ref, company)
        
    def _prepare_all_journals(self, acc_template_ref, company, journals_dict=None):
        me_chart =  self.env.ref("l10n_me.l10nme_chart_template")
        if self.id == me_chart.id or self.parent_id.id == me_chart.id:
            journals = [{'name': _('Revenue Recognition'), 'type': 'general', 'code': _('RR'), 'favorite': False, 'color': 11, 'sequence': 11},
                         {'name': _('Expense Recognition'), 'type': 'general', 'code': _('ER'), 'favorite': False, 'color': 11, 'sequence': 11},
                         {'name': _('Tax'), 'type': 'general', 'code': _('Tax'), 'favorite': False, 'color': 11, 'sequence': 11},
                         {'name': _('Reconciliation Entries'), 'type': 'general', 'code': _('RECE'), 'favorite': False, 'color': 11, 'sequence': 11}
                         ]
            if journals_dict != None:
                journals_dict.extend(journals)
            else:
                journals_dict = journals
            journals_data = super(AccountChartTemplate, self)._prepare_all_journals(acc_template_ref, company, journals_dict)
            for journal in journals_data:
                if journal['code'] == "CABA" and journal['type'] == "general":
                    journal ["active"] = False
        else :
            journals_data = super(AccountChartTemplate, self)._prepare_all_journals(acc_template_ref, company, journals_dict)
        return journals_data
    

    def _create_bank_journals(self, company, acc_template_ref):
        from_act = False
        me_chart =  self.env.ref("l10n_me.l10nme_chart_template")
        if self.id == me_chart.id or self.parent_id.id == me_chart.id:
            from_act = True
        journals = super(AccountChartTemplate, self.with_context(acc_template_ref=acc_template_ref ,from_act=from_act))._create_bank_journals(company, acc_template_ref)
        me_chart =  self.env.ref("l10n_me.l10nme_chart_template")
        if self.id == me_chart.id or self.parent_id.id == me_chart.id:
            suspense_account = self.env.ref("l10n_me.%s_account_account_template_105"%(company.id))
            cash_journal = journals.filtered(lambda x:x.type == "cash")
            cash_journal.write({"suspense_account_id":suspense_account.id})
            cash_basis_taxes = journals.filtered(lambda x:x.type == "general" and x.code == "CABA")
            cash_basis_taxes.write({"active":False})
            env = self.env
            vals = []
            for journal in journals:
                if journal.name and journal.name == "Bank":
                    journal.payment_sequence = False
                    journal._update_field_translations('name', {'ar_001': 'البنك'})
                elif journal.name and journal.name == "Cash":
                    journal._update_field_translations('name', {'ar_001': 'نقد'})
                    journal.payment_sequence = False
        return journals
    
    def _load_company_accounts(self, account_ref, company):
        res =  super(AccountChartTemplate, self)._load_company_accounts(account_ref, company)
        if hasattr(company, 'account_tax_periodicity'):
            company.account_tax_periodicity = "2_months"
        if not company.account_journal_payment_debit_account_id and (company.chart_template_id.parent_id and company.chart_template_id.parent_id == self.env.ref('l10n_me.l10nme_chart_template')):
            company.account_journal_payment_debit_account_id = self.env.ref("l10n_me.%s_account_account_template_90"%(company.id)).id 
        if not company.account_journal_payment_credit_account_id and (company.chart_template_id.parent_id and company.chart_template_id.parent_id == self.env.ref('l10n_me.l10nme_chart_template')):
            company.account_journal_payment_credit_account_id = self.env.ref("l10n_me.%s_account_account_template_92"%(company.id)).id 
        return res
    
    
    def _load(self, company):
        res = super(AccountChartTemplate, self)._load(company)
        me_chart =  self.env.ref("l10n_me.l10nme_chart_template")
        
        if self.id == me_chart.id or self.parent_id.id == me_chart.id:
            journal = self.env["account.journal"]
            bank_journal = journal.search([('type','=','bank'),('code','=',"BNK1"),('company_id','=',company.id)],limit=1)
            cash_journal = journal.search([('type','=','cash'),('code','=','CSH1'),('company_id','=',company.id)],limit=1)
            rece_journal = journal.search([('type','=','general'),('code','=','RECE'),('company_id','=',company.id)],limit=1)
            vb_journal = journal.search([('type','=','purchase'),('code','=','BILL'),('company_id','=',company.id)],limit=1)
            inv_journal = journal.search([('type','=','sale'),('code','=','INV'),('company_id','=',company.id)],limit=1)
            exr_journal = journal.search([('type','=','general'),('code','=','ER'),('company_id','=',company.id)],limit=1)
            rr_journal = journal.search([('type','=','general'),('code','=','RR'),('company_id','=',company.id)],limit=1)
            tax_journal = journal.search([('type','=','general'),('code','=','Tax'),('company_id','=',company.id)],limit=1)
            exch = journal.search([('type','=','general'),('code','=','EXCH'),('company_id','=',company.id)],limit=1)
            
            internet_exp_account = self.env.ref("l10n_me.%s_account_account_template_11"%(company.id)).id
            rent_exp_account = self.env.ref("l10n_me.%s_account_account_template_12"%(company.id)).id
            
            if cash_journal:
                for in_line in cash_journal.inbound_payment_method_line_ids:
                    if self.env.ref('account.account_payment_method_manual_in', False) and self.env.ref('account.account_payment_method_manual_in').id == in_line.payment_method_id.id:
                        in_line.payment_account_id = cash_journal.default_account_id.id
                
                for out_line in cash_journal.outbound_payment_method_line_ids:
                    if self.env.ref('account.account_payment_method_manual_out', False) and self.env.ref('account.account_payment_method_manual_out').id == out_line.payment_method_id.id:
                        out_line.payment_account_id = cash_journal.default_account_id.id 
            
            if tax_journal and company._fields.get('account_tax_periodicity_journal_id', False):
                company.account_tax_periodicity_journal_id = tax_journal.id 
                
            categ = False
            try:
                categ = self.env.ref("product.cat_expense")
            except:
                categ = self.env["product.category"].search([],limit=1)
            imd_obj = self.env['ir.model.data']
            common_vals = {
                    "type":"service",
                    "categ_id":categ.id,
                    "default_code":"Prepaid",
                    "purchase_ok":True,
                    "supplier_taxes_id":False,
                    "sale_ok":False,
                    "company_id": False
                    }
            
            internt_prod = self.env.ref('l10n_me.internet_product', False)
            rent_prod = self.env.ref('l10n_me.office_rent_product', False)
            
            if internet_exp_account and not internt_prod:
                common_vals["name"] = "Internet"
                common_vals["property_account_expense_id"] = internet_exp_account
                common_vals["taxes_id"] = [(6, 0, [])]
                p1 = self.env["product.template"].create(common_vals)
                p1.property_account_income_id  = False
                ii = imd_obj.create({'module': 'l10n_me',
                                'name': 'internet_product',
                                'model': 'product.template',
                                'res_id': p1.id,
                                'noupdate': True})
            else:
                internt_prod.with_company(company.id).property_account_expense_id = internet_exp_account
                internt_prod.with_company(company.id).property_account_income_id = False
                
            if rent_exp_account and not rent_prod:
                common_vals["name"] = "Office Rent"
                common_vals["property_account_expense_id"] = rent_exp_account
                common_vals["taxes_id"] = [(6, 0, [])]
                p2 = self.env["product.template"].create(common_vals)
                p2.property_account_income_id  = False
                imd_obj.create({'module': 'l10n_me',
                                'name': 'office_rent_product',
                                'model': 'product.template',
                                'res_id': p2.id,
                                'noupdate': True})
            else:
                rent_prod.with_company(company.id).property_account_expense_id = rent_exp_account
                rent_prod.with_company(company.id).property_account_income_id = False
            
            cheques_book_ref = "l10n_me.%s_cheques_book_template"%(company.id)
            cheques_book = self.env.ref(cheques_book_ref)
            allowed_discount_ref = "l10n_me.%s_allowed_discount_template"%(company.id)
            allowed_discount = self.env.ref(allowed_discount_ref) 
            write_off_ref = "l10n_me.%s_write_off_template"%(company.id)
            earned_disc_ref = "l10n_me.%s_earned_discount_template"%(company.id)
            earned_disc = self.env.ref(earned_disc_ref)
            if bank_journal:
                cheques_book.match_journal_ids = [(4,bank_journal.id)]
                allowed_discount.match_journal_ids = [(4,bank_journal.id)]
                earned_disc.match_journal_ids = [(4,bank_journal.id)]
            if cash_journal:
                allowed_discount.match_journal_ids = [(4,cash_journal.id)]
                earned_disc.match_journal_ids = [(4,cash_journal.id)]
                
                cash_account = self.env.ref("l10n_me.%s_account_account_cash"%(company.id), False)
                if cash_account:
                    cash_account.allowed_journal_ids = [(6,0,[cash_journal.id])]
    
            if rece_journal:
                allowed_discount.line_ids.write({'journal_id':rece_journal.id})
                earned_disc.line_ids.write({'journal_id':rece_journal.id})
            
            outstanding_rec = self.env.ref("l10n_me.%s_account_account_template_90"%(company.id), False)
            if outstanding_rec:
                outstanding_rec.allowed_journal_ids = [(6, 0, [bank_journal.id,exch.id])]
            outstanding_pay = self.env.ref("l10n_me.%s_account_account_template_92"%(company.id), False)
            if outstanding_pay:
                outstanding_pay.allowed_journal_ids = [(6, 0, [bank_journal.id,exch.id])] 
            acc_payable = self.env.ref("l10n_me.%s_account_account_template_30"%(company.id), False)
            if acc_payable:
                acc_payable.allowed_journal_ids = [(6, 0, [bank_journal.id,exch.id,cash_journal.id,vb_journal.id])] 
            acc_receivable = self.env.ref("l10n_me.%s_account_account_template_6"%(company.id), False)
            if acc_receivable:
                acc_receivable.allowed_journal_ids = [(6, 0, [bank_journal.id,exch.id,cash_journal.id,inv_journal.id])] 
            exp_acc = self.env.ref("l10n_me.%s_account_account_template_10"%(company.id), False)
            if exp_acc:
                exp_acc.allowed_journal_ids = [(6, 0, [exr_journal.id,vb_journal.id])]
            pexp_acc = self.env.ref("l10n_me.%s_account_account_template_11"%(company.id), False)
            if pexp_acc:
                pexp_acc.allowed_journal_ids = [(6, 0, [exr_journal.id,vb_journal.id])]
            pexpr_acc =self.env.ref("l10n_me.%s_account_account_template_12"%(company.id), False)
            if pexpr_acc:
                pexpr_acc.allowed_journal_ids = [(6, 0, [exr_journal.id,vb_journal.id])]
            pexph_acc =self.env.ref("l10n_me.%s_account_account_template_13"%(company.id), False)
            if pexph_acc:
                pexph_acc.allowed_journal_ids = [(6, 0, [exr_journal.id,vb_journal.id])]
            une12_acc =self.env.ref("l10n_me.%s_account_account_template_36"%(company.id), False)
            if une12_acc:
                une12_acc.allowed_journal_ids = [(6, 0, [inv_journal.id,rr_journal.id])]
            une6_acc =self.env.ref("l10n_me.%s_account_account_template_111"%(company.id), False)
            if une6_acc:
                une6_acc.allowed_journal_ids = [(6, 0, [inv_journal.id,rr_journal.id])]
            une3_acc =self.env.ref("l10n_me.%s_account_account_template_112"%(company.id), False)
            if une3_acc:
                une3_acc.allowed_journal_ids = [(6, 0, [inv_journal.id,rr_journal.id])]
            une2_acc =self.env.ref("l10n_me.%s_account_account_template_113"%(company.id), False)
            if une2_acc:
                une2_acc.allowed_journal_ids = [(6, 0, [inv_journal.id,rr_journal.id])]
            une1_acc =self.env.ref("l10n_me.%s_account_account_template_114"%(company.id), False)
            if une1_acc:
                une1_acc.allowed_journal_ids = [(6, 0, [inv_journal.id,rr_journal.id])]
            furn_acc =self.env.ref("l10n_me.%s_account_account_template_15"%(company.id), False)
            if furn_acc:
                furn_acc.allowed_journal_ids = [(6, 0, [inv_journal.id,vb_journal.id])]
                
            #Non Trade Accounts
            acc1 =self.env.ref("l10n_me.%s_account_account_template_115"%(company.id), False)
            if acc1:
                acc1.non_trade = True
                
            acc2 =self.env.ref("l10n_me.%s_account_account_template_33"%(company.id), False)
            if acc2:
                acc2.non_trade = True
                
        return res
    
    
    def generate_journals(self, acc_template_ref, company, journals_dict=None):
        res = super(AccountChartTemplate, self).generate_journals(acc_template_ref, company, journals_dict)
        env = self.env
        vals = []
        me_chart =  self.env.ref("l10n_me.l10nme_chart_template")
        if self.id == me_chart.id or self.parent_id.id == me_chart.id:
            journals = env["account.journal"].search([('company_id','=',company.id)])
            for journal in journals:
                if journal.name and journal.name == "Customer Invoices":
                    journal._update_field_translations('name', {'ar_001': 'فواتير العميل'})
                elif journal.name and journal.name == "Vendor Bills":
                    journal._update_field_translations('name', {'ar_001': 'فواتير الموردون'})
                elif journal.name and journal.name == "Miscellaneous Operations":
                    journal._update_field_translations('name', {'ar_001': 'عمليات متنوعة'})
                elif journal.name and journal.name == "Exchange Difference":
                    journal._update_field_translations('name', {'ar_001': 'فرق سعر الصرف'})
                elif journal.name and journal.name == "Bank":
                    journal._update_field_translations('name', {'ar_001': 'البنك'})
                elif journal.name and journal.name == "Cash":
                    journal._update_field_translations('name', {'ar_001': 'نقد'})
                elif journal.name and journal.name == "Fixed Assets":
                    journal._update_field_translations('name', {'ar_001': 'الأصول الثابتة'})
                elif journal.name and journal.name == "Expense Recognition":
                    journal._update_field_translations('name', {'ar_001': 'الاعتراف بالمصروفات'})
                elif journal.name and journal.name == "Revenue Recognition":
                    journal._update_field_translations('name', {'ar_001': 'تحقق الإيرادات'})
                elif journal.name and journal.name == "Stock":
                    journal._update_field_translations('name', {'ar_001': 'مخزون'})
                elif journal.name and journal.name == "Tax":
                    journal._update_field_translations('name', {'ar_001': 'ضريبة'})
            return journals
        return res

    
class AccountReconcileModel(models.Model):
    _inherit = 'account.reconcile.model'
    
    @api.model_create_multi
    def create(self, vals):
        model = super(AccountReconcileModel, self).create(vals)
        seq =  self._context.get("sequence")
        if seq:
            model.sequence = seq
        return model
    
class AM(models.Model):
    _inherit = "account.move"
    
    def _get_invoice_computed_reference(self):
        self.ensure_one()
        if self.journal_id.invoice_reference_type == 'origin':
            return self.invoice_origin
        elif self.journal_id.invoice_reference_type == 'sale':
            if self.env.ref('sale.model_sale_order', False):
                so = self.env['sale.order'].search([('invoice_ids','in',[self.id])], limit=1)
                if so:
                    ref = self.payment_reference or ''
                    if ref:
                        return so.name+'-'+ref
                    else:
                        return so.name
            return ''
        return super(AM, self)._get_invoice_computed_reference()
    
    def _get_starting_sequence(self):
        self.ensure_one()
        is_payment = self.payment_id or self._context.get('is_payment')
        if self.journal_id.type == "general":
            starting_sequence = "%s/%04d/%02d/0000" % (self.journal_id.code, self.date.year, self.date.month)
        else:
            starting_sequence = "%s/%04d/0000" % (self.journal_id.code, self.date.year)
        if self.journal_id.refund_sequence and self.move_type in ('out_refund', 'in_refund'):
            starting_sequence = "R" + starting_sequence
            
        if self.journal_id.payment_sequence and is_payment:
            starting_sequence = "P" + starting_sequence
        return starting_sequence

    @api.ondelete(at_uninstall=False)
    def _unlink_forbid_parts_of_chain(self):
        """ Moves with a sequence number can only be deleted if they are the last element of a chain of sequence.
        If they are not, deleting them would create a gap. If the user really wants to do this, he still can
        explicitly empty the 'name' field of the move; but we discourage that practice.
        """
        if not self._context.get('force_delete') and not self.filtered(lambda move: move.name != '/')._is_end_of_seq_chain():
            raise UserError(_(
                "You cannot delete this entry, as it has already consumed a sequence number and is not the last one in the chain. You should probably revert it instead."
            ))
    
    # @api.constrains('name')
    # def _check_name(self):
    #     for rec in self:
    #         moves = self.search([('company_id','=',rec.journal_id.company_id.id),('name','=',rec.name),('id','!=',rec.id),('state','=','posted')],limit=1)
    #         pass_validation = self._context.get('pass_validation', False)
    #         if moves and not pass_validation:
    #             raise ValidationError(_("Name should be unique per company."))
    
class AccountReconcileTemplate(models.Model):
    _inherit = 'account.reconcile.model.template'

    name = fields.Char(string='Button Label', required=True, translate=True)

    
class AccountReconcile(models.Model):
    _inherit = 'account.reconcile.model'

    name = fields.Char(string='Name', required=True, translate=True)


