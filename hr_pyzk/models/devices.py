from odoo import models, fields, api, exceptions, _

from addons.hr_pyzk.controllers import controller as c



class Devices(models.Model):


    _name = 'devices'

    name = fields.Char(string='Device Name')
    ip_address = fields.Char(string='Ip address')
    port = fields.Integer(string='Port', default = 4370)
    sequence = fields.Integer(string='Sequence')
    device_password = fields.Char(string='Device Password')
    state = fields.Selection([(0, 'Active'), (1, 'Inactive')], string='Status', default=1)
    difference = fields.Float(string='Time Difference with UTC',
                              help = "Please enter the time difference betwneen local and UTC times in hours", default=0)

    def test_connection(self):
        with c.ConnectToDevice(self.ip_address, self.port, self.device_password) as conn:
            if conn:
                return {
                    "type": "ir.actions.act_window",
                    "res_model": "devices",
                    "views": [[False, "form"]],
                    "res_id": self.id,
                    "target": "main",
                    "context": {'show_message1': True},
                }

