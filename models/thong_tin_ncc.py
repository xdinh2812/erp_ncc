from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'thong.tin.ncc'
    _description = 'Thong tin nha cung cap'

    ten_ncc = fields.Char(string='Tên nhà cung cấp')
    dia_chi = fields.Char(string='Địa chỉ', required=True)
    email = fields.Char(string='Email', required=True)
    dien_thoai = fields.Integer(string='Điện thoại')
    website = fields.Char(string='Website')
    tax_id = fields.Char(string='TAX ID')
    tag = fields.Char(string='Tag')
    danh_gia_cuoi_cung = fields.Selection([
        ('0', '0'),
        ('1', '1 sao'),
        ('2', '2 sao'),
        ('3', '3 sao'),
        ('4', '4 sao'),
        ('5', '5 sao')
    ], string="Đánh giá cuối cùng", default='1')
    danh_gia_moi = fields.Char(string='Đánh giá mới')
