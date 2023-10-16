#-*- encoding:utf-8 -*-
from odoo import models,api,fields
import logging


class WizardReportStock(models.TransientModel):
    _name = "wizard.report.stock"
    _description = "Wizard para Reporte Inventario"

    TYPE_STATE_STOCK = [
        ('draft','Borrador'),
        ('done', 'Realizado'),
        ('cancel', 'Cancelado')
    ]
    date_from = fields.Date(string="Fecha Desde",required=True)
    date_to = fields.Date(string="Fecha Hasta",required=True)
    state_stock = fields.Selection(string="Estado",selection=TYPE_STATE_STOCK)

    def btn_report_xlsx(self):
        data={
            'date_from':self.date_from,
            'date_to':self.date_to,
            'state_stock':self.state_stock
        }

        return self.env.ref('report_stock.stock_picking_report').report_action(self,data=data)