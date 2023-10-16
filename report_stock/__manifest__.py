{
    'name':'Reporte de Inventario',
    'author':'Johao Marcos Maldonado Roman',
    'depends':[
        'base',
        'stock',
        'report_xlsx'
    ],
    'data':[
        #Report
        'report/report_stock_picking_xlsx.xml',
        'report/report_stock_picking.xml',
        #wizard
        'wizard/stock.xml'
    ]

}