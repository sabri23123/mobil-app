# -*- coding: utf-8 -*-
# Bu dosya, bir sonraki aşamada fiziksel donanımlara (Arduino vb.) 
# Bluetooth üzerinden bağlanmak için kullanılacak modülün taslağıdır.

class BluetoothController:
    def __init__(self):
        self.connected = False
        self.device_mac = None
        
    def connect_to_device(self, mac_address):
        '''
        Android API (jnius) veya pyjnius kullanılarak HC-05 / BLE cihazına bağlanma işlemi
        '''
        self.device_mac = mac_address
        self.connected = True
        print(f"[{mac_address}] cihazına başarıyla bağlanıldı.")
        
    def send_pid_values(self, kp, ki, kd):
        '''
        Mobil uygulamadaki slider'lardan gelen veriyi donanıma yollar
        '''
        if self.connected:
            # Protokol örneği: P1.50I0.05D0.40\n
            data_packet = f"P{kp:.2f}I{ki:.2f}D{kd:.2f}\n"
            # TODO: Serial.write() işlemi burada yapılacak
            print(f"Donanıma gönderilen veri paketi: {data_packet}")
        else:
            print("Cihaz bağlı değil!")
