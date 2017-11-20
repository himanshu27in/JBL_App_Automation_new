'''
Created on Nov 15, 2017

@author: hkumar04


This file is created o store all different types of log coming in logmon tool
'''


a2dp_playing_log = ['AVRCP_PASS_THROUGH_ID_PLAY','A2DP_Playing','AUDIO_PLAYBACK']
a2dp_paused_log = ['AVRCP_PASS_THROUGH_ID_PAUSE','PAUSED']
aa_off_log = ['SMART','FeatureValue: 0']
aa_low_log = ['SMART','FeatureValue: 1']
aa_high_log = ['SMART','FeatureValue: 3']
volume_up_log = ['SysEventData: 3','Headphone_Volume']
volume_low_log = ['SysEventData: 4','Headphone_Volume']
max_volume_up_log = ['SysEventData: 3','SyncedVolumeIndex: 16','Headphone_Volume','PowerOn_Tone']
min_volume_down_log = ['SysEventData: 4','SyncedVolumeIndex: 0','Headphone_Volume']