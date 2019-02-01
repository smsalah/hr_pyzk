# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime

from odoo import models, fields, api, exceptions, _


class CombinedAttendances(models.Model):
    _name = "combined.attendances"
    _description = "combined.attendances"
    _order = "device_date desc"

    # @api.one
    # def _compute_get_employee_id(self):
    #     if self.pyzk_employee_id.employee_id:
    #         self.employee_id = self.pyzk_employee_id.employee_id
    #
    # @api.one
    # def _compute_get_name(self):
    #     if self.pyzk_employee_id:
    #         self.name = self.pyzk_employee_id.name

    @api.one
    @api.depends('device_user_id')
    def _compute_get_employee_id(self):
        if self.device_user_id.employee_id:
            self.employee_id = self.device_user_id.employee_id

    device_user_id = fields.Many2one('device.users', 'Device User ID')
    employee_id = fields.Many2one('hr.employee', 'Related employee', compute=_compute_get_employee_id, store=True )
    device_date = fields.Date(string="Date")
    device_clockin = fields.Datetime(string="Clock In")
    device_clockout = fields.Datetime(string="Clock Out")
    state = fields.Selection([('Not Transferred', 'Not Transferred'),
                              ('Invalid', 'Invalid'), ('Transferred','Transferred')],
                             string='Status',default='Not Transferred')

