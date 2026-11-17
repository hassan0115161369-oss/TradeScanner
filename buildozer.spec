[app]
title = TradeScanner
package.name = tradescanner
package.domain = org.trade
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf
version = 1.0
requirements = python3,kivy==2.3.1,cython==0.29.36
orientation = portrait
fullscreen = 0

android.permissions = READ_EXTERNAL_STORAGE
android.api = 30
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
