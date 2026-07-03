# Mobil PID Kontrol Merkezi

Bu proje, PyCharm kullanılarak geliştirilmiş bir mobil uygulamanın (Android/iOS) başlangıç iskeletidir.

## Proje İçeriği
- `main.py`: Kivy kütüphanesi ile yazılmış ana arayüz ve simülasyon kodları.
- `bluetooth_kontrol.py`: İleri aşamada uygulamayı gerçek bir donanımla konuşturmak için hazırlanan taslak sınıf.
- `buildozer.spec`: Projeyi Android cihazlar için yüklenebilir .apk dosyasına çevirecek olan konfigürasyon dosyası. (Gerekli Bluetooth izinleri eklenmiştir).

## Nasıl Çalıştırılır?
1. Bu klasörü PyCharm'da açın.
2. Terminali açıp `pip install kivy` yazarak kütüphaneyi kurun.
3. `main.py` dosyasına sağ tıklayıp "Run 'main'" diyerek uygulamayı bilgisayarınızda test edin.
