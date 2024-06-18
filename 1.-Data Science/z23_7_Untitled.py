import win32serviceutil
import win32service
import win32event
import time
import subprocess
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
        print("Service is running...")
        while self.running:
            self.check_time_and_run_script()
            time.sleep(30)  # Check every 30 seconds

    def check_time_and_run_script(self):
        # Especifica la hora en la que quieres ejecutar el script
        target_hour = 2  # Ejemplo: 2 para las 2:00 AM (hora en formato de 24 horas)
        target_minute = 27  # Ejemplo: 18 para los 18 minutos

        now = datetime.now()
        print(f"Current time: {now.hour}:{now.minute}")

        if now.hour == target_hour and now.minute == target_minute:
            print(f"Executing script at {target_hour}:{target_minute}")
            self.run_script()
        else:
            print(f"Waiting for {target_hour}:{target_minute}...")

    def run_script(self):
        # Ruta del script Python a ejecutar
        script_path = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/23.4.-POO GUI Multiples Pantallas PyQt5.py"
        
        try:
            # Ejecutar el script en un proceso separado
            subprocess.Popen(["pythonw", script_path])
            print(f"GUI iniciada: {script_path}")

            # Esperar 30 segundos antes de cerrar el proceso
            time.sleep(30)

            # Terminar el proceso de la GUI después de 30 segundos
            subprocess.Popen(["taskkill", "/f", "/im", "pythonw.exe", "/t"])
            print("GUI cerrada")
        except Exception as e:
            print(f"Error al ejecutar la GUI: {e}")

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(MyService)