import win32serviceutil
import win32service
import win32event
import time
import os
from datetime import datetime

class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = "MyPythonService"
    _svc_display_name_ = "My Python Service"
    _svc_description_ = "This service runs a specific Python script at a specified time."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.running = False
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        while self.running:
            self.check_time_and_run_script()
            time.sleep(60)  # Check every minute

    def check_time_and_run_script(self):
        # Especifica la hora en la que quieres ejecutar el script
        target_hour = 1  # Ejemplo: 14 para las 2:00 PM
        target_minute = 54

        now = datetime.now()
        if now.hour == target_hour and now.minute == target_minute:
            self.run_script()

    def run_script(self):
        # Ruta del script Python a ejecutar
        script_path = r"C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/23.4.-POO GUI Multiples Pantallas PyQt5.py"
        os.system(f"python {script_path}")

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(MyService)