{
    'name': 'NCC_Database',
    'version': '1.0',
    'summary': 'Summery',
    'description': 'Description',
    'category': 'Category',
    'author': 'Dino',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [

        'security/ir.model.access.csv',
        'views/tieu_chi_view.xml',
        'views/danh_gia_ncc_view.xml',
        'views/thong_tin_ncc_view.xml',
        'views/ncc_menu.xml',
        'data/data.xml',

             ],

    # 'assets': {'web.assets_backend': [
    #     'static/src/css/style.css',
    #     ],
    # },
    'installable': True,
    'application': True,
    'auto_install': False,

}
