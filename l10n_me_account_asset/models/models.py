# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class AccountAsset(models.Model):
    _inherit = "account.asset"
    
    name = fields.Char(string='Asset Name', compute='_compute_name', store=True, required=True, translate=True)

class AccountChartTemplate(models.Model):
    _inherit = "account.chart.template"
    
    def load_account_assets(self,company):
        env = self.env
        asset_model = env["account.asset"]
        translation_object = env["ir.translation"]
        er_journal = env["account.journal"].search([('type','=','general'),('code','=','ER'),('company_id','=',company.id)],limit=1)
        sale_journal = env["account.journal"].search([('type','=','sale'),('code','=','INV'),('company_id','=',company.id)])
        purchase_journal = env["account.journal"].search([('type','=','purchase'),('code','=','BILL'),('company_id','=',company.id)])
        rent_account = env.ref("l10n_me.%s_account_account_template_56"%(company.id), False)
        prepaid_rent_account = env.ref("l10n_me.%s_account_account_template_12"%(company.id), False)
        internet_account = env.ref("l10n_me.%s_account_account_template_71"%(company.id), False)
        prepaid_internet_account = env.ref("l10n_me.%s_account_account_template_11"%(company.id), False)
        translation_values = []
        if prepaid_rent_account and rent_account:
            asset_1 = asset_model.create({
                "name":"1Y - Rent",
                "method_period":'1',
                "method_number":12,
                "journal_id":er_journal.id,
                "asset_type":'expense',
                "account_depreciation_id":prepaid_rent_account.id,
                "account_depreciation_expense_id":rent_account.id,
                "state":"model"
                })
            
            translation_values.append({
                'name':'account.asset,name',
                'type':'model',
                'lang':'ar_001',
                'src':"1Y - Rent",
                'value':"عام واحد - ايجارات",
                'res_id':asset_1.id
                
                })
        
        if prepaid_internet_account and internet_account:
            asset_2 = asset_model.create({
                "name":"1Y - Internet",
                "method_period":'1',
                "method_number":12,
                "journal_id":er_journal.id,
                "asset_type":'expense',
                "account_depreciation_id":prepaid_internet_account.id,
                "account_depreciation_expense_id":internet_account.id,
                "state":"model"
                })
            translation_values.append({
                'name':'account.asset,name',
                'type':'model',
                'lang':'ar_001',
                'src':"1Y - Internet",
                'value':"عام واحد - انترنت",
                'res_id':asset_2.id
                
                })
        if prepaid_rent_account and rent_account:
            asset_3 = asset_model.create({
                "name":"6M - Rent",
                "method_period":'1',
                "method_number":6,
                "journal_id":er_journal.id,
                "asset_type":'expense',
                "account_depreciation_id":prepaid_rent_account.id,
                "account_depreciation_expense_id":rent_account.id,
                "state":"model"
                })
            translation_values.append({
                'name':'account.asset,name',
                'type':'model',
                'lang':'ar_001',
                'src':"6M - Rent",
                'value':"ستة اشهر - ايجارات",
                'res_id':asset_3.id
                
                })
        
        if prepaid_internet_account and internet_account:
            asset_4 = asset_model.create({
                "name":"6M - Internet",
                "method_period":'1',
                "method_number":6,
                "journal_id":er_journal.id,
                "asset_type":'expense',
                "account_depreciation_id":prepaid_internet_account.id,
                "account_depreciation_expense_id":internet_account.id,
                "state":"model"
                })
            
            translation_values.append({
                'name':'account.asset,name',
                'type':'model',
                'lang':'ar_001',
                'src':"6M - Internet",
                'value':"ستة اشهر - انترنت",
                'res_id':asset_4.id
                
                })
        
        if prepaid_rent_account and rent_account:
            asset_5 = asset_model.create({
                "name":"3M - Rent",
                "method_period":'1',
                "method_number":3,
                "journal_id":er_journal.id,
                "asset_type":'expense',
                "account_depreciation_id":prepaid_rent_account.id,
                "account_depreciation_expense_id":rent_account.id,
                "state":"model"
                })
            translation_values.append({
                'name':'account.asset,name',
                'type':'model',
                'lang':'ar_001',
                'src':"3M - Rent",
                'value':"ثلاثة اشهر - ايجارات",
                'res_id':asset_5.id
                
                })
        
        if prepaid_internet_account and internet_account:
            asset_6 = asset_model.create({
                "name":"3M - Interne",
                "method_period":'1',
                "method_number":3,
                "journal_id":er_journal.id,
                "asset_type":'expense',
                "account_depreciation_id":prepaid_internet_account.id,
                "account_depreciation_expense_id":internet_account.id,
                "state":"model"
                })
            translation_values.append({
                'name':'account.asset,name',
                'type':'model',
                'lang':'ar_001',
                'src':"3M - Interne",
                'value':"ثلاثة اشهر - انترنت",
                'res_id':asset_6.id
                
                })
        
        fa_journal = self.env["account.journal"].search([('company_id','=',company.id),('code','=',"FA")],limit=1)
        if not fa_journal:
            fa_journal = env["account.journal"].create({
                "name":"Fixed Assets",
                "code":"FA",
                "type":"general",
                'show_on_dashboard':False,
                "company_id":company.id,
                })
            translation_values.append({
                'res_id':fa_journal.id,
                'src':fa_journal.name,
                'value':"الأصول الثابتة",
                'name':'account.journal,name',  
                'lang':'ar_001',
                'type':'model'
                })
        
        tools_and_eq_acc = env.ref("l10n_me.%s_account_account_template_25"%(company.id), False)
        tools_and_eq_dep_acc = env.ref("l10n_me.%s_account_account_template_26"%(company.id), False)
        tools_and_eq_exp_acc = env.ref("l10n_me.%s_account_account_template_82"%(company.id), False)
        if tools_and_eq_acc and tools_and_eq_dep_acc and tools_and_eq_exp_acc:
            tools_and_eq = asset_model.create({
                "name":_("Tools and Equipments"),
                "asset_type":"purchase",
                "state":"model",
                "method":"linear",
                "method_number":60,
                "method_period":"1",
                "journal_id":fa_journal.id,
                "account_asset_id":tools_and_eq_acc.id,
                "account_depreciation_id":tools_and_eq_dep_acc.id,
                "account_depreciation_expense_id":tools_and_eq_exp_acc.id,
                "company_id":company.id
                })
            
            translation_values.append({
                'name':'account.asset,name',
                'type':'model',
                'lang':'ar_001',
                'src':"ثلاثة اشهر - انترنت",
                'value':"عدد و معدات",
                'res_id':tools_and_eq.id
                
                })
        
        
            tools_and_eq_acc.create_asset = "draft"
            tools_and_eq_acc.multiple_assets_per_line = False
            tools_and_eq_acc.asset_model = tools_and_eq.id  
            tools_and_eq_acc.allowed_journal_ids = [(6,0,[sale_journal.id,purchase_journal.id,fa_journal.id])]
            tools_and_eq_dep_acc.allowed_journal_ids = [(6,0,[fa_journal.id])]
        
        elect_acc = env.ref("l10n_me.%s_account_account_template_98"%(company.id), False)
        elect_dep_acc = env.ref("l10n_me.%s_account_account_template_97"%(company.id), False)
        elect_exp_acc = env.ref("l10n_me.%s_account_account_template_99"%(company.id), False)
        
        if  elect_acc and elect_dep_acc and elect_exp_acc:
            elect = asset_model.create({
                "name":_("Electricity Devices"),
                "asset_type":"purchase",
                "state":"model",
                "method":"linear",
                 "method_number":36,
                 "method_period":"1",
                "journal_id":fa_journal.id,
                "account_asset_id":elect_acc.id,
                "account_depreciation_id":elect_dep_acc.id,
                "account_depreciation_expense_id":elect_exp_acc.id,
                 "company_id":company.id
                })
            
            translation_values.append({
                'name':'account.asset,name',
                'type':'model',
                'lang':'ar_001',
                'src':"ثلاثة اشهر - انترنت",
                'value':"اجهزة الكترونية",
                'res_id':elect.id
                
                })
            elect_acc.create_asset = "draft"
            elect_acc.multiple_assets_per_line = False
            elect_acc.asset_model = elect.id  
            elect_acc.allowed_journal_ids = [(6,0,[sale_journal.id,purchase_journal.id,fa_journal.id])]
            elect_dep_acc.allowed_journal_ids = [(6,0,[fa_journal.id])]
        
        furniture_acc = env.ref("l10n_me.%s_account_account_template_15"%(company.id), False)
        furniture_dep_acc = env.ref("l10n_me.%s_account_account_template_16"%(company.id), False)
        furniture_exp_acc = env.ref("l10n_me.%s_account_account_template_78"%(company.id), False)
        
        if furniture_acc and furniture_dep_acc and furniture_exp_acc:
            furniture = asset_model.create({
                "name":_("Furniture"),
                "asset_type":"purchase",
                "state":"model",
                "method":"linear",
                 "method_number":60,
                 "method_period":"1",
                "journal_id":fa_journal.id,
                "account_asset_id":furniture_acc.id,
                "account_depreciation_id":furniture_dep_acc.id,
                "account_depreciation_expense_id":furniture_exp_acc.id,
                 "company_id":company.id
                })
            
            translation_values.append({
                'name':'account.asset,name',
                'type':'model',
                'lang':'ar_001',
                'src':"Furniture",
                'value':"اثاث",
                'res_id':furniture.id
                
                })
        
            furniture_acc.create_asset = "draft"
            furniture_acc.multiple_assets_per_line = False
            furniture_acc.asset_model = furniture.id  
            furniture_acc.allowed_journal_ids = [(6,0,[sale_journal.id,purchase_journal.id,fa_journal.id])]
            furniture_dep_acc.allowed_journal_ids = [(6,0,[fa_journal.id])]
        
        
        decoration_acc = env.ref("l10n_me.%s_account_account_template_21"%(company.id), False)
        decoration_dep_acc = env.ref("l10n_me.%s_account_account_template_22"%(company.id), False)
        decoration_exp_acc = env.ref("l10n_me.%s_account_account_template_81"%(company.id), False)
        
        if decoration_acc and decoration_dep_acc and decoration_exp_acc:
            decoration = asset_model.create({
                "name":_("Decorations"),
                "asset_type":"purchase",
                "state":"model",
                "method":"linear",
                 "method_number":120,
                 "method_period":"1",
                "journal_id":fa_journal.id,
                "account_asset_id":decoration_acc.id,
                "account_depreciation_id":decoration_dep_acc.id,
                "account_depreciation_expense_id":decoration_exp_acc.id,
                 "company_id":company.id
                })
            
            translation_values.append({
                'name':'account.asset,name',
                'type':'model',
                'lang':'ar_001',
                'src':"Decorations",
                'value':"الديكورات",
                'res_id':decoration.id
                
                })
        
            decoration_acc.create_asset = "draft"
            decoration_acc.multiple_assets_per_line = False
            decoration_acc.asset_model = decoration.id  
            decoration_acc.allowed_journal_ids = [(6,0,[sale_journal.id,purchase_journal.id,fa_journal.id])]
            decoration_dep_acc.allowed_journal_ids = [(6,0,[fa_journal.id])]

        computers_acc = env.ref("l10n_me.%s_account_account_template_17"%(company.id), False)
        computers_dep_acc = env.ref("l10n_me.%s_account_account_template_18"%(company.id), False)
        computers_exp_acc = env.ref("l10n_me.%s_account_account_template_79"%(company.id), False)
        
        if computers_acc and computers_dep_acc and computers_exp_acc:
            computer = asset_model.create({
                "name":_("Computers"),
                "asset_type":"purchase",
                "state":"model",
                "method":"linear",
                 "method_number":34,
                 "method_period":"1",
                "journal_id":fa_journal.id,
                "account_asset_id":computers_acc.id,
                "account_depreciation_id":computers_dep_acc.id,
                "account_depreciation_expense_id":computers_exp_acc.id,
                 "company_id":company.id
                })
            
            translation_values.append({
                'name':'account.asset,name',
                'type':'model',
                'lang':'ar_001',
                'src':"Computers",
                'value':"الحاسبات",
                'res_id':computer.id
                })
        
        
            computers_acc.create_asset = "draft"
            computers_acc.multiple_assets_per_line = True
            computers_acc.asset_model = computer.id  
            computers_acc.allowed_journal_ids = [(6,0,[sale_journal.id,purchase_journal.id,fa_journal.id])]
            computers_dep_acc.allowed_journal_ids = [(6,0,[fa_journal.id])]
        
        car_acc = env.ref("l10n_me.%s_account_account_template_23"%(company.id), False)
        car_dep_acc = env.ref("l10n_me.%s_account_account_template_24"%(company.id), False)
        car_exp_acc = env.ref("l10n_me.%s_account_account_template_77"%(company.id), False)
        
        if car_acc and car_dep_acc and car_exp_acc:
            car = asset_model.create({
                "name":_("Cars"),
                "asset_type":"purchase",
                "state":"model",
                "method":"linear",
                 "method_number":60,
                 "method_period":"1",
                "journal_id":fa_journal.id,
                "account_asset_id":car_acc.id,
                "account_depreciation_id":car_dep_acc.id,
                "account_depreciation_expense_id":car_exp_acc.id,
                 "company_id":company.id
                })
            
            translation_values.append({
                'name':'account.asset,name',
                'type':'model',
                'lang':'ar_001',
                'src':"Cars",
                'value':"السيارات",
                'res_id':car.id
                })
        
            car_acc.create_asset = "draft"
            car_acc.multiple_assets_per_line = False
            car_acc.asset_model = car.id  
            car_acc.allowed_journal_ids = [(6,0,[sale_journal.id,purchase_journal.id,fa_journal.id])]
            car_dep_acc.allowed_journal_ids = [(6,0,[fa_journal.id])]
            car_exp_acc.allowed_journal_ids = [(6,0,[fa_journal.id])]
        
        conditions_acc = env.ref("l10n_me.%s_account_account_template_19"%(company.id), False)
        conditions_dep_acc = env.ref("l10n_me.%s_account_account_template_20"%(company.id), False)
        conditions_exp_acc = env.ref("l10n_me.%s_account_account_template_80"%(company.id), False)
        
        if conditions_acc and conditions_dep_acc and conditions_exp_acc:
            conditions = asset_model.create({
                "name":_("Air Conditions"),
                "asset_type":"purchase",
                "state":"model",
                "method":"linear",
                 "method_number":24,
                 "method_period":"1",
                "journal_id":fa_journal.id,
                "account_asset_id":conditions_acc.id,
                "account_depreciation_id":conditions_dep_acc.id,
                "account_depreciation_expense_id":conditions_exp_acc.id,
                 "company_id":company.id
                })
            
            translation_values.append({
                'name':'account.asset,name',
                'type':'model',
                'lang':'ar_001',
                'src':"Air Conditions",
                'value':"المكيفات",
                'res_id':conditions.id
                })
        
            conditions_acc.create_asset = "draft"
            conditions_acc.multiple_assets_per_line = False
            conditions_acc.asset_model = conditions.id  
            conditions_acc.allowed_journal_ids = [(6,0,[sale_journal.id,purchase_journal.id,fa_journal.id])]
            conditions_dep_acc.allowed_journal_ids = [(6,0,[fa_journal.id])]
        
        acc_sys_acc = env.ref("l10n_me.%s_account_account_template_27"%(company.id), False)
        acc_sys_dep_acc = env.ref("l10n_me.%s_account_account_template_28"%(company.id), False)
        acc_sys_exp_acc = env.ref("l10n_me.%s_account_account_template_83"%(company.id), False)
        
        if acc_sys_acc and acc_sys_dep_acc and acc_sys_exp_acc:
            acc_sys = asset_model.create({
                "name":_("Accounting Systems"),
                "asset_type":"purchase",
                "state":"model",
                "method":"linear",
                 "method_number":24,
                 "method_period":"1",
                "journal_id":fa_journal.id,
                "account_asset_id":acc_sys_acc.id,
                "account_depreciation_id":acc_sys_dep_acc.id,
                "account_depreciation_expense_id":acc_sys_exp_acc.id,
                 "company_id":company.id
                })
            
            translation_values.append({
                'name':'account.asset,name',
                'type':'model',
                'lang':'ar_001',
                'src':"Accounting Systems",
                'value':"نظام المحاسبة",
                'res_id':acc_sys.id
                })
            translation_object.create(translation_values)
            acc_sys_acc.create_asset = "draft"
            acc_sys_acc.multiple_assets_per_line = False
            acc_sys_acc.asset_model = acc_sys.id  
            acc_sys_acc.allowed_journal_ids = [(6,0,[sale_journal.id,purchase_journal.id,fa_journal.id])]
            acc_sys_dep_acc.allowed_journal_ids = [(6,0,[fa_journal.id])]
        
        prepaid_rent = env.ref("l10n_me.%s_account_account_template_12"%(company.id), False)
        if prepaid_rent:
            prepaid_rent.create_asset = "draft"
        
        prepaid_net = env.ref("l10n_me.%s_account_account_template_11"%(company.id), False)
        if prepaid_net:
            prepaid_net.create_asset = "draft"
        
        prepaid_main = env.ref("l10n_me.%s_account_account_template_10"%(company.id), False)
        if prepaid_main:
            prepaid_main.create_asset = "draft"
        
        prepaid_h_ins = env.ref("l10n_me.%s_account_account_template_13"%(company.id), False)
        if prepaid_h_ins:
            prepaid_h_ins.create_asset = "draft"
    
    def _load(self, sale_tax_rate, purchase_tax_rate, company):
        res = super(AccountChartTemplate, self)._load( sale_tax_rate, purchase_tax_rate, company)
        if self.parent_id.id == self.env.ref("l10n_me.l10nme_chart_template").id or self.id == self.env.ref("l10n_me.l10nme_chart_template").id:
            self.load_account_assets(company)
        return res
        
        
        