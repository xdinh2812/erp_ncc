from odoo import fields, models, api


class ThongtinNCC(models.Model):
    _name = 'thong.tin.ncc'
    _description = 'Thong tin nha cung cap'
    _rec_name = 'ten_ncc'


    ten_ncc = fields.Char(string='Tên nhà cung cấp')
    loai_hinh = fields.Selection([('ca_nhan', 'Cá nhân'), ('cong_ty', 'Công ty')], string='loại hình', required=True)
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
    ], string="Đánh giá cuối cùng", default='1', readonly=True)
    danh_gia_moi = fields.Char(string='Đánh giá mới')
