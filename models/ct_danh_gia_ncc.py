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
    tong_diem_cuoi_cung = fields.Float(string="Tổng điểm cuối cùng", readonly=True)
    kq_danh_gia = fields.Selection( [
        ('0', '0'),
        ('1', '1 sao'),
        ('2', '2 sao'),
        ('3', '3 sao'),
        ('4', '4 sao'),
        ('5', '5 sao')
    ], string="Kết quả đánh giá", default='1', readonly=True)

    thong_tin_phan_hoi = fields.Text(string="Thông tin phản hồi")

    # def button_tinh_tong_diem(self):
    #     total = 0
    #     count = 0
    #     for record in self:
    #         if record.da_duoc_dg:
    #             total += int(record.diem_dg)
    #             count += 1
    #     self.tong_diem_cuoi_cung = total / count if count > 0 else 0
    #
    #     # Tính kết quả đánh giá dựa trên tổng điểm cuối cùng
    #     if self.tong_diem_cuoi_cung >= 4.5:
    #         self.kq_danh_gia = '5'
    #     elif self.tong_diem_cuoi_cung >= 3.5:
    #         self.kq_danh_gia = '4'
    #     elif self.tong_diem_cuoi_cung >= 2.5:
    #         self.kq_danh_gia = '3'
    #     elif self.tong_diem_cuoi_cung >= 1.5:
    #         self.kq_danh_gia = '2'
    #     else:
    #         self.kq_danh_gia = '1'
