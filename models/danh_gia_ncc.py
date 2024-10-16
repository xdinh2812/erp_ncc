from odoo import models, fields, api
from . import ct_danh_gia_ncc


class DanhGiaNCC(models.Model):
    _name = 'danh.gia.ncc'
    _description = 'Đánh giá nhà cung cấp'
    _rec_name = 'ma_phieu'

    ma_phieu = fields.Char(string="Mã phiếu", readonly=True)  # Auto increment logic có thể được thêm vào sau
    ten_ncc = fields.Many2one('thong.tin.ncc', string='Thông tin NCC')
    email = fields.Char(string="Email", required=True)
    dien_thoai = fields.Integer(string="Điện thoại")
    nganh_kd = fields.Char(string="Ngành kinh doanh")
    ky_dg = fields.Date(string="Kỳ đánh giá")
    ngay_dg = fields.Date(string="Ngày đánh giá")
    quan_ly = fields.Many2one('res.users', string="Quản lý")
    trang_thai = fields.Selection([
        ('draft', 'Nháp'),
        ('submitted', 'Chờ xác nhận'),
        ('confirmed', 'Đã xác nhận'),
        ('refused', 'Từ chối'),
        ('cancelled', 'Hủy')
    ], string="Trạng thái", default="draft", readonly=True)

    # One2many relationship với bảng ct.danh_gia_ncc
    ct_danh_gia_ncc = fields.One2many('ct.danh.gia.ncc', 'danh_gia_ncc_id')
    # Tổng điểm cuối cùng và kết quả đánh giá

    tong_diem_cuoi_cung = fields.Float(string="Tổng điểm cuối cùng", compute='_compute_tong_diem', readonly=True)
    kq_danh_gia = fields.Selection([
        ('0', '0 sao'),
        ('1', '1 sao'),
        ('2', '2 sao'),
        ('3', '3 sao'),
        ('4', '4 sao'),
        ('5', '5 sao')
    ], string="Kết quả đánh giá", default='1',compute='_compute_ket_qua_danh_gia', readonly=True)


    @api.depends('ct_danh_gia_ncc.diem_dg')
    def _compute_tong_diem(self):
        for record in self:
            total = 0
            count = 0
            for line in record.ct_danh_gia_ncc:
                if line.da_duoc_dg:  # Chỉ tính nếu đã được đánh giá
                    total += int(line.diem_dg or 0)  # Chuyển đổi chuỗi thành số
                    count += 1
            record.tong_diem_cuoi_cung = total / count if count > 0 else 0
            if record.ten_ncc:
                record.ten_ncc.danh_gia_cuoi_cung = record.kq_danh_gia

    @api.depends('ct_danh_gia_ncc.tong_diem_cuoi_cung')
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

    @api.model
    def create(self, vals):
        if 'ma_phieu' not in vals:
            existing_numbers = [
                int(record.ma_phieu[6:]) for record in self.search([])
                if record.ma_phieu.startswith('DGNCC')
            ]
            next_number = 1
            while next_number in existing_numbers:
                next_number += 1
            vals['ma_phieu'] = f'DGNCC{next_number:04}'

        res = super(DanhGiaNCC, self).create(vals)
        tieuchidanhgia = self.env['tieu.chi.dg'].search([])

        # Tạo chi tiết đánh giá cho từng tiêu chí
        for tieuchi in tieuchidanhgia:
            self.env['ct.danh.gia.ncc'].create({
                'danh_gia_ncc_id': res.id,  # Gán vào bản ghi đánh giá vừa tạo
                'tieu_chi_dg': tieuchi.id,
                'da_duoc_dg': False,
                'diem_dg': None,  # Để None hoặc giá trị mặc định nếu có
            })
        return res




    def action_submit(self):
        self.write({'trang_thai': 'submitted'})

    def action_confirm(self):
        self.write({'trang_thai': 'confirmed'})

    def action_refuse(self):
        self.write({'trang_thai': 'refused'})


    def action_cancel(self):
        self.write({'trang_thai': 'cancelled'})



