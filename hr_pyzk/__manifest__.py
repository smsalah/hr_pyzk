# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'PYZK Attendances',
    'version': '1.0.0.0',
    'category': 'Human Resources',
    'sequence': 100,
    'summary': 'Employee Attendance using pyzk ',
    'description': """
This Module fetches attendance from zk machines and add them in the attendance
==============================================================================

It works on zkteco machines using pyzk library( version 1.9)
       """,
    'website': 'https://github.com/smsalah/hr_pyzk',
	'author': 'Sheikh M. Salahuddin <smsalah@gmail.com>',
    'license': 'AGPL-3',
    'depends': ['hr', 'hr_attendance'],
    'data': [
        'security/pyzk_security.xml',
        'security/ir.model.access.csv',
        'views/device_users_view.xml',
        'views/devices_view.xml',
        'views/device_attendances_view.xml',
        'views/combined_attendances_view.xml',
        'wizard/user_wizard.xml',
        'wizard/delete_attendance_wizard_view.xml'
     ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
