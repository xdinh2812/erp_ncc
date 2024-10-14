from odoo import models, fields, api

class CtDanhGiaNCC(models.Model):
    _name = 'ct.danh.gia.ncc'
    _description = 'Chi tiết đánh giá nhà cung cấp'

    danh_gia_ncc_id = fields.Many2one('danh.gia.ncc', string="Đánh giá nhà cung cấp", required=True, ondelete='cascade')
    tieu_chi_dg = fields.Many2one('tieu.chi.dg', string="Tiêu chí đánh giá", required=True)
    da_duoc_dg = fields.Boolean(string="Đã được đánh giá", default=False)
    diem_dg = fields.Selection([
        ('0', '0'),
        ('1', '1 sao'),
        ('2', '2 sao'),
        ('3', '3 sao'),
        ('4', '4 sao'),
        ('5', '5 sao')
    ], string="Điểm đánh giá",widget='priority', default='1')
    tong_diem_cuoi_cung = fields.Float(string="Tổng điểm cuối cùng", readonly=True, compute='_compute_tong_diem')
    kq_danh_gia = fields.Selection( [
        ('0', '0'),
        ('1', '1 sao'),
        ('2', '2 sao'),
        ('3', '3 sao'),
        ('4', '4 sao'),
        ('5', '5 sao')
    ], string="Kết quả đánh giá", default='1', readonly=True, compute='_compute_ket_qua_danh_gia')

    thong_tin_phan_hoi = fields.Text(string="Thông tin phản hồi")


