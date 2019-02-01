from zk import ZK, const
from odoo import models, fields, api, exceptions, _

class DeviceUsers():


    def get_users(devices):
        all_users = []
        all_users.clear()
        # device_object = self.env['devices']
        # devices = device_object.search([('state', '=', 0)])
        for device in devices:
            with ConnectToDevice(device.ip_address, device.port, device.device_password) as conn:
                users = conn.get_users()
                all_users.extend(users)
                added = []
                added.clear()
                unique_data = []
                unique_data.clear()
                for user in all_users:
                    if int(user.user_id) not in added:
                        added.append(int(user.user_id))
                        added.sort()
                        unique_data.append(user)
        return unique_data

    def get_attendance(device):
        """
                Function uses to get attendances
                """

        with ConnectToDevice(device.ip_address, device.port, device.device_password) as conn:
            attendances = conn.get_attendance()
            device_attendance = [[x.user_id, x.timestamp, x.punch, device.id] for x in attendances]

        return device_attendance

    def outputresult(user_punches):

        user_clock = []
        user_clock.clear()
        user_attendance = []
        user_attendance.clear()
        initial_number = 1

        for clock in user_punches:
            if clock[2] == initial_number:
                initial_number = clock[2]
                pass
            else:
                user_clock.append(clock)
                initial_number = clock[2]

        if len(user_clock) != 0 and user_clock[-1][2] == 0:
            del (user_clock[-1])

        user_attendance = [[i[0], i[1], j[1]] for i, j in zip(user_clock[::2], user_clock[1::2])]

        return user_attendance
class ConnectToDevice(object):
    """
    Class uses to assure connetion to a device and closing of the same
    It is using to disable the device when it is been reading or busy
    """

    def __init__(self, ip_address, port, device_password):



        try:
            zk = ZK(ip_address, port,timeout = 10, password=device_password)
            conn = zk.connect()

        except Exception as e:
            raise exceptions.Warning(e)

        conn.disable_device()
        self.conn = conn

    def __enter__(self):
        """
        return biometric connection
        """
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        enable device and close connection
        """
        self.conn.enable_device()  # noqa: W0104