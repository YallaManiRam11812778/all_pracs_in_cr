# pyzk_test.py
from zk import ZK, const
# zk = ZK('182.156.77.203', port=8003, timeout=30)
zk = ZK("172.150.1.17", port=4370, timeout=30)
try:
    print('Connecting to device ...')
    conn = zk.connect()
    print('Disabling device ...')
    conn.disable_device()
    print('Firmware Version: : {}'.format(conn.get_firmware_version()))
    # print '--- Get User ---'
    users = conn.get_users()
    for user in users:
        privilege = 'User'
        if user.privilege == const.USER_ADMIN:
            privilege = 'Admin'

        print ('- UID #{}'.format(user.uid))
        print ('  Name       : {}'.format(user.name))
        print ('  Privilege  : {}'.format(privilege))
        print ('  Password   : {}'.format(user.password))
        print ('  Group ID   : {}'.format(user.group_id))
        print ('  User  ID   : {}'.format(user.user_id))

    print("Voice Test ...")
    conn.test_voice()
    print('Enabling device ...')
    conn.enable_device()
except Exception as e:
    print("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()