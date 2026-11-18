[app]
title = TradeScanner
package.name = tradescanner
package.domain = org.trade
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf
version = 1.0
requirements = python3,kivy==2.3.1,requests,urllib3,certifi,openssl,cryptography
orientation = portrait
fullscreen = 0

# قبول التراخيص وصلاحيات الإنترنت
android.accept_sdk_license = True
android.permissions = INTERNET

# إعدادات النظام
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1

