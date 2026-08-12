import os
import sys
import subprocess
import re
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QSpinBox, QComboBox, QTextEdit, QGroupBox, QMessageBox)
from PySide6.QtCore import QTimer

CREATE_NO_WINDOW = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0

def get_bin_path(filename):
    if getattr(sys, 'frozen', False):
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "bin", "scrcpy", filename)

class AdbManager:
    def __init__(self, adb_path):
        self.adb_path = adb_path

    def get_devices_info(self):
        cmd = [self.adb_path, "devices", "-l"]
        try:
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                timeout=5,
                creationflags=CREATE_NO_WINDOW
            )
        except Exception:
            return []

        devices = []
        for line in result.stdout.splitlines()[1:]:
            line = line.strip()
            if not line or line.startswith("*"):
                continue

            parts = line.split()
            if len(parts) < 2:
                continue

            serial = parts[0]
            status = parts[1]
            is_wifi = ":" in serial

            model = "Unknown"
            model_match = re.search(r'model:(\S+)', line)
            if model_match:
                model = model_match.group(1)

            devices.append({
                "serial": serial,
                "model": model,
                "status": status,
                "connection_type": "Wi-Fi" if is_wifi else "USB"
            })
        return devices

    def restart_in_usb_mode(self, serial):
        cmd = [self.adb_path, "-s", serial, "usb"]
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True,
            creationflags=CREATE_NO_WINDOW
        )
        return result.returncode == 0, result.stdout + result.stderr

    def pair_device(self, ip_port, code):
        cmd = [self.adb_path, "pair", ip_port, str(code)]
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True,
            creationflags=CREATE_NO_WINDOW
        )
        success = "Successfully paired" in result.stdout or result.returncode == 0
        return success, result.stdout + result.stderr

    def connect_device(self, ip_port):
        cmd = [self.adb_path, "connect", ip_port]
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True,
            creationflags=CREATE_NO_WINDOW
        )
        success = "connected to" in result.stdout.lower()
        return success, result.stdout + result.stderr

class DexController:
    def __init__(self, scrcpy_path):
        self.scrcpy_path = scrcpy_path
        self.process = None

    def start_dex(self, width=1920, height=1080, dpi=240, bitrate="8M", fps=60, serial=None):
        display_param = f"--new-display={width}x{height}/{dpi}"
        cmd = [
            self.scrcpy_path,
            display_param,
            "-b", bitrate,
            "--max-fps", str(fps),
            "--video-codec=h265",
            "--shortcut-mod=rctrl",
            "--stay-awake",
            "--keyboard=uhid"
        ]
        if serial:
            cmd.extend(["-s", serial])
        self.process = subprocess.Popen(
            cmd,
            creationflags=CREATE_NO_WINDOW
        )
        return self.process

    def stop_dex(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process = None

class DexApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Galaxy A Dex")
        self.setGeometry(100, 100, 520, 660)
        
        adb_path = get_bin_path("adb.exe")
        scrcpy_path = get_bin_path("scrcpy.exe")

        self.adb = AdbManager(adb_path=adb_path)
        self.dex = DexController(scrcpy_path=scrcpy_path)
        self.known_serials = set()

        layout = QVBoxLayout()

        usb_group = QGroupBox("USB ADB Status")
        usb_layout = QVBoxLayout()
        
        device_select_layout = QHBoxLayout()
        device_select_layout.addWidget(QLabel("Connected Device:"))
        self.combo_devices = QComboBox()
        device_select_layout.addWidget(self.combo_devices)
        
        btn_refresh = QPushButton("Refresh")
        btn_refresh.clicked.connect(self.update_device_list)
        device_select_layout.addWidget(btn_refresh)
        usb_layout.addLayout(device_select_layout)
        
        btn_usb_mode = QPushButton("Switch to USB Mode (adb usb)")
        btn_usb_mode.clicked.connect(self.handle_switch_usb)
        usb_layout.addWidget(btn_usb_mode)
        
        usb_group.setLayout(usb_layout)
        layout.addWidget(usb_group)

        wifi_group = QGroupBox("Wireless ADB Connection")
        wifi_layout = QVBoxLayout()
        
        pair_layout = QHBoxLayout()
        self.input_pair_ip = QLineEdit()
        self.input_pair_ip.setPlaceholderText("IP:Port (for pairing)")
        self.input_pair_code = QLineEdit()
        self.input_pair_code.setPlaceholderText("Pairing Code")
        btn_pair = QPushButton("Pair")
        btn_pair.clicked.connect(self.handle_pair)
        pair_layout.addWidget(self.input_pair_ip)
        pair_layout.addWidget(self.input_pair_code)
        pair_layout.addWidget(btn_pair)
        wifi_layout.addLayout(pair_layout)

        conn_layout = QHBoxLayout()
        self.input_conn_ip = QLineEdit()
        self.input_conn_ip.setPlaceholderText("IP:Port (for connection :5555)")
        btn_conn = QPushButton("Connect")
        btn_conn.clicked.connect(self.handle_connect)
        conn_layout.addWidget(self.input_conn_ip)
        conn_layout.addWidget(btn_conn)
        wifi_layout.addLayout(conn_layout)
        
        wifi_group.setLayout(wifi_layout)
        layout.addWidget(wifi_group)

        dex_group = QGroupBox("DeX Virtual Display Settings")
        dex_layout = QVBoxLayout()
        
        res_layout = QHBoxLayout()
        res_layout.addWidget(QLabel("Width:"))
        self.spin_width = QSpinBox()
        self.spin_width.setRange(800, 3840)
        self.spin_width.setValue(1920)
        res_layout.addWidget(self.spin_width)

        res_layout.addWidget(QLabel("Height:"))
        self.spin_height = QSpinBox()
        self.spin_height.setRange(600, 2160)
        self.spin_height.setValue(1080)
        res_layout.addWidget(self.spin_height)

        res_layout.addWidget(QLabel("DPI:"))
        self.spin_dpi = QSpinBox()
        self.spin_dpi.setRange(120, 480)
        self.spin_dpi.setValue(240)
        res_layout.addWidget(self.spin_dpi)
        dex_layout.addLayout(res_layout)

        self.btn_toggle_dex = QPushButton("Start DeX")
        self.btn_toggle_dex.clicked.connect(self.handle_toggle_dex)
        dex_layout.addWidget(self.btn_toggle_dex)
        
        dex_group.setLayout(dex_layout)
        layout.addWidget(dex_group)

        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        layout.addWidget(self.log_area)

        footer_layout = QHBoxLayout()
        btn_license = QPushButton("License Info")
        btn_license.clicked.connect(self.show_license_dialog)
        footer_layout.addStretch()
        footer_layout.addWidget(btn_license)
        layout.addLayout(footer_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.monitor_timer = QTimer(self)
        self.monitor_timer.setInterval(3000)
        self.monitor_timer.timeout.connect(self.update_device_list)
        self.monitor_timer.start()

        self.update_device_list()

    def show_license_dialog(self):
        license_text = (
            "Galaxy DeX & ADB Controller\n\n"
            "[Application License]\n"
            "MIT License\n\n"
            "[Third-Party Open Source Licenses]\n"
            "・scrcpy (Apache License 2.0)\n"
            "   Copyright (C) 2018 Genymobile\n"
            "   Copyright (C) 2018-2026 Romain Vimont\n"

            "  https://github.com/Genymobile/scrcpy\n\n"
            "・Android Debug Bridge (ADB) (Apache License 2.0)\n"
            "  Copyright (C) The Android Open Source Project\n\n"
            "・PySide6 / Qt6 (LGPL v3)\n"
            "  Copyright (C) The Qt Company Ltd."
        )
        QMessageBox.about(self, "License Information", license_text)

    def log(self, text):
        self.log_area.append(text)

    def get_selected_device(self):
        return self.combo_devices.currentData()

    def update_device_list(self):
        devices = self.adb.get_devices_info()
        current_serials = {d["serial"] for d in devices}
        
        self.combo_devices.clear()
        if not devices:
            self.combo_devices.addItem("No devices detected")
        else:
            for dev in devices:
                status_str = f" [{dev['status'].upper()}]" if dev['status'] != "device" else ""
                label = f"[{dev['connection_type']}] {dev['model']} ({dev['serial']}){status_str}"
                self.combo_devices.addItem(label, userData=dev)

        new_devices = current_serials - self.known_serials
        for dev in devices:
            if dev["serial"] in new_devices:
                if dev["status"] == "unauthorized":
                    self.log(f"⚠️ Device detected but unauthorized: {dev['serial']}")
                    self.log("👉 Please tap 'Allow USB debugging' on your device screen.")
                elif dev["status"] == "device":
                    self.log(f"✅ Connected: {dev['model']} ({dev['serial']})")
                else:
                    self.log(f"⚠️ Connection status [{dev['status']}]: {dev['serial']}")

        removed_devices = self.known_serials - current_serials
        for serial in removed_devices:
            self.log(f"❌ Disconnected: {serial}")

        self.known_serials = current_serials

    def handle_switch_usb(self):
        dev = self.get_selected_device()
        if not dev or "serial" not in dev:
            self.log("No device selected.")
            return
        success, msg = self.adb.restart_in_usb_mode(dev["serial"])
        self.log(f"Switch to USB mode: {msg.strip()}")

    def handle_pair(self):
        ip_port = self.input_pair_ip.text()
        code = self.input_pair_code.text()
        if not ip_port or not code:
            self.log("Please enter IP:Port and pairing code.")
            return
        success, msg = self.adb.pair_device(ip_port, code)
        self.log(f"Pairing result: {msg.strip()}")
        self.update_device_list()

    def handle_connect(self):
        ip_port = self.input_conn_ip.text()
        if not ip_port:
            self.log("Please enter IP:Port.")
            return
        success, msg = self.adb.connect_device(ip_port)
        self.log(f"Connection result: {msg.strip()}")
        self.update_device_list()

    def handle_toggle_dex(self):
        if self.dex.process is None or self.dex.process.poll() is not None:
            dev = self.get_selected_device()
            if not dev or "serial" not in dev:
                self.log("Error: Please select a valid device.")
                return
            
            if dev["status"] != "device":
                self.log(f"Error: Device is not ready ({dev['status']})")
                return

            w = self.spin_width.value()
            h = self.spin_height.value()
            dpi = self.spin_dpi.value()
            
            self.dex.start_dex(width=w, height=h, dpi=dpi, serial=dev["serial"])
            self.log(f"DeX started [{dev['serial']}]: {w}x{h} / {dpi}DPI")
            self.btn_toggle_dex.setText("Stop DeX")
        else:
            self.dex.stop_dex()
            self.log("DeX stopped")
            self.btn_toggle_dex.setText("Start DeX")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = DexApp()
    win.show()
    sys.exit(app.exec())