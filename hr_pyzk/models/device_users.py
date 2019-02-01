
from odoo import models, fields, api, exceptions, _
from addons.hr_pyzk.controllers import controller as c
from zk import ZK, const

class DeviceUsers(models.Model):
    _name = 'device.users'
    _order = "device_user_id"


    device_user_id = fields.Integer('Device User ID')
    device_uid = fields.Integer('Device UID') # uid in the device. Important to delete user in the future
    name = fields.Char('Device User Name')
    employee_id = fields.Many2one('hr.employee', 'Related employee')
    device_id = fields.Many2one('devices', 'Fingerprint Device')

    _sql_constraints = [
        ('employee_id_uniq', 'unique (employee_id)',
         'It is not possible to relate an employee with a pyzk user '
         'more than once!'),
    ]

    _sql_constraints = [
        ('device_user_id_uniq', 'unique (device_user_id)',
         'It is not possible to create more than one user '
         'with the same device_user_id'),
    ]

    @api.multi
    def create_user(self, device):
        """
                Function uses to get attendances
                """
        ip_address = self.device_id.ip_address
        port = self.device_id.port
        device_password = self.device_id.device_password
        user_id = str(self.device_user_id)

        with c.ConnectToDevice(ip_address, port, device_password) as conn:

            device_users = conn.get_users()
            device_user_ids = [int(x.user_id) for x in device_users]
            if self.device_user_id not in device_user_ids:
                conn.set_user(uid=self.device_user_id, name=self.name, privilege=const.USER_DEFAULT, user_id=user_id)
                self.device_uid = self.device_user_id
                return {
                    "type": "ir.actions.act_window",
                    "res_model": "device.users",
                    "views": [[False, "form"]],
                    "res_id": self.id,
                    "target": "main",
                    "context": {'show_message1': True},
                }

            else:
                return {
                    "type": "ir.actions.act_window",
                    "res_model": "device.users",
                    "views": [[False, "form"]],
                    "res_id": self.id,
                    "target": "main",
                    "context": {'show_message2': True},
                }

    @api.multi
    def edit_user(self, device):
        """
                Function uses to get attendances
                """
        ip_address = self.device_id.ip_address
        port = self.device_id.port
        device_password = self.device_id.device_password

        if self.device_id.id is False:
            raise exceptions.Warning("Fingerprint device is not selected")



        with c.ConnectToDevice(ip_address, port, device_password) as conn:

            try:
                conn.set_user(uid=self.device_user_id, name=self.name, privilege=const.USER_DEFAULT,
                              user_id=str(self.device_user_id))
                return {
                    "type": "ir.actions.act_window",
                    "res_model": "device.users",
                    "views": [[False, "form"]],
                    "res_id": self.id,
                    "target": "main",
                    "context": {'show_message3': True},
                }

            except Exception as e:
                raise exceptions.Warning("User does not exist in the device")
            # else:
            #     return {
            #         "type": "ir.actions.act_window",
            #         "res_model": "device.users",
            #         "views": [[False, "form"]],
            #         "res_id": self.id,
            #         "target": "main",
            #         "context": {'show_message4': True},
            #     }
