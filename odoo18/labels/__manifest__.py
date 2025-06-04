{
    'name': 'Transfer Label Generator',
    'version': '1.0',
    'summary': 'Custom label printing for transfer operations',
    'description': 'Generates barcode labels for products during transfer, only if checkbox is enabled on product form.',
    'category': 'Inventory',
    'author': 'Mohammed Al-Nakheby',
    'website': 'https://github.com/romance007',
    'depends': ['stock'],
        'data': [
        'views/product_template_views.xml',
        'reports/report_reception_report_label.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
 
