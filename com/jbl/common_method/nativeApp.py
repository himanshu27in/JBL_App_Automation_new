'''
Created on Oct 25, 2017

@author: hkumar04
'''
import os

class SonyXperiaNativeApp(object):
    '''
    All functions defined in this class belong to native app of Sony Xperia XZ(F8332)
    '''

    @staticmethod
    def launch_bt_setting_page(self):
        self.driver.implicitly_wait(10000)
        # adb command for sony xperia
        os.system("adb shell am start -n com.android.settings/.bluetooth.BluetoothSettings")
        #adb command for LG G5
        #os.system("adb shell am start -n com.lge.bluetoothsetting/.LGBluetoothSettingActivity")