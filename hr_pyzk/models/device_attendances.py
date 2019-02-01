from datetime import datetime

from odoo import models, fields, api, exceptions, _


class DeviceAttendances(models.Model):
    _name = "device.attendances"
    _description = "Device Attendances"
    #_order = "pyzk_datetime"
    _order = "device_datetime desc"

    @api.one
    @api.depends('device_id')
    def _compute_get_employee_id(self):
        if self.device_user_id.employee_id:
            self.employee_id = self.device_user_id.employee_id

    device_user_id = fields.Many2one('device.users','Device ID')
    employee_id = fields.Many2one('hr.employee', 'Related employee', compute=_compute_get_employee_id, store=True )
    device_datetime = fields.Datetime(string="Device Datetime")
    device_punch = fields.Selection([(0, 'Check In'), (1, 'Check Out')], string='Device Punch')
    attendance_state = fields.Selection([(0, 'Not Logged'), (1, 'Logged')], string='Status', default = 0)
    #validity = fields.Selection([(0, 'Valid'), (1, 'Invalid')], string='Validity', default=0)
    device_id = fields.Many2one('devices', 'fingerprint Device')
