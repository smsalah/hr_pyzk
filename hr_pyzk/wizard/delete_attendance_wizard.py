
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################

#from .pyzk_data import PyzkData
from zk import ZK, const
from odoo import api, fields, models, exceptions, _
from addons.hr_pyzk.controllers import controller as c
from zk import ZK, const

class DeleteAttendanceWizard(models.TransientModel):
    _name = 'delete.attendance.wizard'

    device_id = fields.Many2one('devices', 'Fingerprint Device',)


    def delete_attendance(self):

        with c.ConnectToDevice(self.device_id.ip_address, self.device_id.port, self.device_id.device_password) as conn:
            conn.clear_attendance()
            raise exceptions.Warning('Attendances deleted successfully')

