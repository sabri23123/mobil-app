[app]
title = PID Kontrol
package.name = pidkontrol
package.domain = org.mobilproje
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,jnius
orientation = portrait
fullscreen = 0
# Bluetooth izinleri donanımla haberleşmek için çok önemli
android.permissions = BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_CONNECT, ACCESS_COARSE_LOCATION
android.archs = arm64-v8a, armeabi-v7a
