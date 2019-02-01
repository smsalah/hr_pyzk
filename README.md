# <span style="color: #339966;">**Introduction**</span>  

This repository contains an odoo module for attendance. it brings attendance from  
zkteco machines and transfer them to hr attendance.  

## <span style="color: #339966;">Here is how it workds</span>

<span style="color: #339966;"> </span>

> <span style="color: #ff0000;">**Important!**</span>
> 
> <span style="color: #ff0000;"> </span>
> 
> <span style="color: #ff0000;">Install pyzk library first. the library is included in the module directory hr_pyzk/pyzk-master. you can also get it from the following link . You can also get it from  [here](https://github.com/fananimi/pyzk). To install the library go to pyzk_master folder and run python setup.py.</span>
> 
> <span style="color: #ff0000;">Please Visit the image folder in the main folder of the module (hr_pyzk/images) to view different processes.</span>

1.  <span style="color: #000000;">Make sure you copy the module in addons folder of odoo. After the installation of the module make sure to make the user member of **"Device/Manager" Security group.**</span>
2.  <span style="color: #000000;">Create attendance devices. Please make sure password is defined on the machine.I think default password is nothing but I am not sure.If device status is defined Inactive the users and attendances will not be imported from it.</span>
3.  <span style="color: #000000;">After defining the device import device users using "User/Attendance Wizard".</span>
4.  <span style="color: #000000;">Define related odoo employees for device users. If Odoo employees are not defined the attendance will not be transferred.</span>
5.  <span style="color: #000000;">Import attendance from the device using "User/Attendance Wizard". Their are separate records for clock ins and clockouts for all users from all devices.</span>
6.  <span style="color: #000000;">Combine attendance using "User/Attendance Wizard". combining means relevant clocin and clock outs will be joined for each user. the logic work as follows.  
    The system makes pairs between subsequent Clock in /clock out. If a user forget clocking out the system will look for the next clock out and ignore a repeating clock in even if it is legal.</span>
7.  <span style="color: #000000;">Transfer attendance to HR Attendance using "User/Attendance Wizard".</span>
8.  <span style="color: #000000;">Delete Attendance from selected device. Be carefull.</span>
9.  <span style="color: #000000;">You can create fingerprint user by clicking create user and than click "Create Fingerprint User".</span>
10.  You can Edit existing users by clicking "Edit/Update Existing fingperint User" button in the user form view.

## <span style="color: #339966;">Compatible Devices</span>

<span style="color: #339966;"> </span>

*   Firmware Version : Ver 6.21 Nov 19 2008 Platform : ZEM500 DeviceName : U580
*   Firmware Version : Ver 6.60 Apr 9 2010 Platform : ZEM510_TFT DeviceName : T4-C
*   Firmware Version : Ver 6.60 Dec 1 2010 Platform : ZEM510_TFT DeviceName : T4-C
*   Firmware Version : Ver 6.60 Mar 18 2011 Platform : ZEM600_TFT DeviceName : iClock260
*   Platform : ZEM560_TFT Firmware Version : Ver 6.60 Feb 4 2012 DeviceName :
*   Firmware Version : Ver 6.60 Oct 29 2012 Platform : ZEM800_TFT DeviceName : iFace402/ID
*   Firmware Version : Ver 6.60 Mar 18 2013 Platform : ZEM560 DeviceName : MA300
*   Firmware Version : Ver 6.60 Dec 27 2014 Platform : ZEM600_TFT DeviceName : iFace800/ID
*   Firmware Version : Ver 6.60 Nov 6 2017 (remote tested with correct results) Platform : ZMM220_TFT DeviceName : (unknown device) (broken info but at least the important data was read)
*   Firmware Version : Ver 6.60 Jun 9 2017 Platform : JZ4725_TFT DeviceName : K20 (latest checked correctly!)
*   Firmware Version : Ver 6.60 Aug 23 2014 Platform : ZEM600_TFT DeviceName : VF680 (face device only, but we read the user and attendance list!)
