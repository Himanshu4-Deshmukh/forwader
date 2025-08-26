# Write buildozer.spec with source.dir
buildozer_spec = """
[app]
title = OTP Interceptor
package.name = otpinterceptor
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,scapy,pyserial
orientation = portrait
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,READ_PHONE_STATE,RECEIVE_SMS,SEND_SMS

[buildozer]y
log_level = 2
warn_on_root = 1
"""
with open('buildozer.spec', 'w') as f:
    f.write(buildozer_spec)