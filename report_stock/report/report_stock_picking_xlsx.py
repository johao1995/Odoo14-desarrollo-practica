# -*- coding:utf-8 -*-
from odoo import models,api
from datetime import datetime

import logging
_logger = logging.getLogger(__name__)

class ReportStock(models.AbstractModel):
    _name = "report.report_stock.stock_picking_report_xlsx"
    _inherit = "report.report_xlsx.abstract"


    def generate_xlsx_report(self,workbook,data,partners):

        date_from = data.get('date_from',False)
        date_to = data.get('date_to',False)
        state_stock = data.get('state_stock',False)

        sheet = workbook.add_worksheet("Reporte")
        format_header = workbook.add_format({
            'align':'vcenter',
            'bold':True,
            'border':True
        })
        format_body = workbook.add_format({
            'align':'vcenter',
            'border':True
        })
        sheet.write(1,1,"Referencia",format_header)
        sheet.write(1,2,"Contacto", format_header)
        sheet.write(1,3,"Fecha", format_header)
        sheet.write(1,4,"Documento Origen", format_header)
        sheet.write(1,5,"Estado", format_header)

        query_stock = """
            SELECT stock.name AS name_stock,
            partner.name AS name_partner,
            stock.scheduled_date,
            stock.origin,
            state AS state_stock
            FROM stock_picking stock INNER JOIN res_partner partner 
            ON stock.partner_id = partner.id
            WHERE stock.state = %s
        """
        self.env.cr.execute(query_stock,(state_stock,))
        result_stock = self.env.cr.dictfetchall()
        row = 2
        for stock in result_stock:
            #Hallando Estado
            sheet.write(row,1,stock['name_stock'],format_body)
            sheet.write(row,2,stock['name_partner'], format_body)
            sheet.write(row,3,stock['scheduled_date'].strftime('%m/%d/%Y %H:%M:%S'), format_body)
            sheet.write(row,4,stock['origin'], format_body)
            sheet.write(row,5,stock['state_stock'], format_body)

            row+=1
