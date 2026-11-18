[app]
title = TradeScanner
package.name = tradescanner
package.domain = org.trade
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf
version = 1.0

# تحديد إصدار بايثون المستقر 3.11 بدلاً من 3.14
requirements = python3,kivy==2.3.1,requests,urllib3,certifi,openssl,numpy,pillow

orientation = portrait
fullscreen = 0

android.accept_sdk_license = True
android.permissions = INTERNET, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1

# مهم جداً: استخدام الفرع المستقر وليس develop
p4a.branch = master
