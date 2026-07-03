import tkinter as tk
import math
import random


class PIDSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("PID Denge Simülatörü (Kurulumsuz Test)")

        # Fizik Değişkenleri
        self.angle = -30.0
        self.angular_velocity = 0.0
        self.target_angle = 0.0

        self.integral = 0.0
        self.last_error = 0.0
        self.disturbance_timer = 0

        # Arayüz Kurulumu (Siyah Ekran)
        self.canvas = tk.Canvas(root, width=400, height=300, bg="#101820")
        self.canvas.pack(pady=10)

        # Kontrol Paneli (Sliderlar)
        controls = tk.Frame(root)
        controls.pack(fill="x", padx=20, pady=5)

        tk.Label(controls, text="Kp (Oransal):", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="e")
        self.kp_slider = tk.Scale(controls, from_=0, to=5, resolution=0.05, orient="horizontal", length=200)
        self.kp_slider.set(1.5)
        self.kp_slider.grid(row=0, column=1)

        tk.Label(controls, text="Ki (İntegral):", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="e")
        self.ki_slider = tk.Scale(controls, from_=0, to=1, resolution=0.01, orient="horizontal", length=200)
        self.ki_slider.set(0.05)
        self.ki_slider.grid(row=1, column=1)

        tk.Label(controls, text="Kd (Türevsel):", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="e")
        self.kd_slider = tk.Scale(controls, from_=0, to=2, resolution=0.02, orient="horizontal", length=200)
        self.kd_slider.set(0.4)
        self.kd_slider.grid(row=2, column=1)

        # Oyunu Başlat
        self.update_simulation()

    def update_simulation(self):
        dt = 1.0 / 60.0

        # Sliderlardan anlık değerleri al
        Kp = self.kp_slider.get()
        Ki = self.ki_slider.get()
        Kd = self.kd_slider.get()

        # Rastgele Rüzgar Etkisi (Kolun dengesini bozan şey)
        self.disturbance_timer += dt
        if self.disturbance_timer > 2.5:
            self.angular_velocity += random.uniform(-15.0, 15.0)
            self.disturbance_timer = 0

        # PID Hesaplaması (Düzeltme algoritması)
        error = self.target_angle - self.angle
        self.integral += error * dt
        self.integral = max(min(self.integral, 50), -50)
        derivative = (error - self.last_error) / dt

        output = (Kp * error) + (Ki * self.integral) + (Kd * derivative)
        self.last_error = error

        # Fizik ve Yerçekimi
        gravity_effect = -9.81 * math.sin(math.radians(self.angle)) * 0.1
        angular_acceleration = output + gravity_effect

        self.angular_velocity += angular_acceleration * dt
        self.angular_velocity *= 0.98  # Sürtünme yavaşlaması
        self.angle += self.angular_velocity * dt

        # Dönme Sınırları
        if self.angle > 90:
            self.angle, self.angular_velocity = 90, 0
        elif self.angle < -90:
            self.angle, self.angular_velocity = -90, 0

        # Ekrana Çizdirme
        self.canvas.delete("all")
        cx, cy = 200, 150

        # Hedef Denge Çizgisi (Yeşil)
        self.canvas.create_line(50, cy, 350, cy, fill="#27ae60", dash=(4, 4))

        # Pervane Kolunu Hesapla
        rad = math.radians(self.angle)
        arm_length = 100
        x_end = cx + arm_length * math.cos(rad)
        y_end = cy + arm_length * math.sin(rad)
        x_start = cx - arm_length * math.cos(rad)
        y_start = cy - arm_length * math.sin(rad)

        # Pervane Kolunu Çiz
        self.canvas.create_line(x_start, y_start, x_end, y_end, fill="#bdc3c7", width=4)

        # Kırmızı Merkez Noktası
        self.canvas.create_oval(cx - 5, cy - 5, cx + 5, cy + 5, fill="#e74c3c")

        # Uçlardaki Mavi Motorlar
        self.canvas.create_oval(x_end - 10, y_end - 10, x_end + 10, y_end + 10, fill="#3498db")
        self.canvas.create_oval(x_start - 10, y_start - 10, x_start + 10, y_start + 10, fill="#3498db")

        # 60 FPS Hızında tekrarla
        self.root.after(16, self.update_simulation)


if __name__ == "__main__":
    root = tk.Tk()
    app = PIDSimulator(root)
    root.mainloop()