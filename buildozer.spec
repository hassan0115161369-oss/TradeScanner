[app]
title = TradeScanner
package.name = tradescanner
package.domain = org.trade
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf
version = 1.0
requirements = python3,kivy==2.3.1,requests,urllib3,certifi,openssl,numpy==1.22.3
orientation = portrait
fullscreen = 0

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

p4a.branch = release-2023.09.16
