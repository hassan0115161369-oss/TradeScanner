[app]
title = TradeScanner
package.name = tradescanner
package.domain = org.trade
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf
version = 1.0
requirements = python3,kivy==2.3.1,cython==0.29.33,requests,urllib3
orientation = portrait
fullscreen = 0

# قبول تراخيص اندرويد تلقائياً (مهم جداً لمنع فشل البناء)
android.accept_sdk_license = True

# إضافة صلاحية الإنترنت (ضرورية جداً لتطبيق تداول) مع صلاحية التخزين
android.permissions = INTERNET, READ_EXTERNAL_STORAGE

# تحديث إصدار أندرويد ليكون متوافقاً مع الخوادم الحديثة
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
