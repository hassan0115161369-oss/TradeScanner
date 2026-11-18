[app]
title = TradeScanner
package.name = tradescanner
package.domain = org.trade
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf
version = 1.0

# تحديد إصدارات البايثون بدقة (hostpython3 و python3) لمنع التعارض
requirements = hostpython3==3.11.5,python3==3.11.5,kivy==2.3.1,requests,urllib3,certifi,openssl,numpy==1.24.2

orientation = portrait
fullscreen = 0

# إعدادات أندرويد
android.accept_sdk_license = True
android.permissions = INTERNET, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1

# استخدام الفرع الرئيسي المستقر لـ p4a
p4a.branch = master
