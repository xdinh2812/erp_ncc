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
    tong_diem_cuoi_cung = fields.Float(string="Tổng điểm cuối cùng", compute="_compute_tong_diem", readonly=True)
    kq_danh_gia = fields.Selection([
        ('0', '0'),
        ('1', '1 sao'),
        ('2', '2 sao'),
        ('3', '3 sao'),
        ('4', '4 sao'),
        ('5', '5 sao')
    ], string="Kết quả đánh giá", compute="_compute_ket_qua_danh_gia", default='1', readonly=True)

    thong_tin_phan_hoi = fields.Text(string="Thông tin phản hồi")

    @api.depends('diem_dg')
    def _compute_tong_diem(self):
        for record in self:
            total = sum(int(line.diem_dg) for line in record)
            count = len(record)
            record.tong_diem_cuoi_cung = total / count if count > 0 else 0

    @api.depends('tong_diem_cuoi_cung')
    def _compute_ket_qua_danh_gia(self):
        for record in self:
            if record.tong_diem_cuoi_cung >= 4.5:
                record.kq_danh_gia = '5'
            elif record.tong_diem_cuoi_cung >= 3.5:
                record.kq_danh_gia = '4'
            elif record.tong_diem_cuoi_cung >= 2.5:
                record.kq_danh_gia = '3'
            elif record.tong_diem_cuoi_cung >= 1.5:
                record.kq_danh_gia = '2'
            else:
                record.kq_danh_gia = '1'

