from odoo import models, fields, api


class DanhGiaNCC(models.Model):
    _name = 'danh.gia.ncc'
    _description = 'Đánh giá nhà cung cấp'

    ma_phieu = fields.Char(string="Mã phiếu", required=True,
                           default="DGNCC0001")  # Auto increment logic có thể được thêm vào sau
    ten_ncc = fields.Char(string="Tên nhà cung cấp", required=True)
    email = fields.Char(string="Email", required=True)
    dien_thoai = fields.Integer(string="Điện thoại")
    nganh_kd = fields.Char(string="Ngành kinh doanh")
    ky_dg = fields.Date(string="Kỳ đánh giá")
    ngay_dg = fields.Date(string="Ngày đánh giá")
    quan_ly = fields.Many2one('res.users', string="Quản lý")
    trang_thai = fields.Selection([
        ('draft', 'Nhập'),
        ('submitted', 'Chờ xác nhận'),
        ('confirmed', 'Đã xác nhận'),
        ('refused', 'Từ chối'),
        ('cancelled', 'Hủy')
    ], string="Trạng thái", default="draft", readonly=True)

    # One2many relationship với bảng ct.danh_gia_ncc
    ct_danh_gia_ncc = fields.One2many('ct.danh.gia.ncc', 'danh_gia_ncc_id', string="Báo cáo đánh giá")
    cta_danh_gia_ncc = fields.One2many('ct.danh.gia.ncc', 'danh_gia_ncc_id', string="Chi tiết đánh giá")
    # Tổng điểm cuối cùng và kết quả đánh giá


    def action_submit(self):
        self.write({'trang_thai': 'submitted'})

    def action_confirm(self):
        self.write({'trang_thai': 'confirmed'})

    def action_refuse(self):
        self.write({'trang_thai': 'refused'})


    def action_cancel(self):
        self.write({'trang_thai': 'cancelled'})
