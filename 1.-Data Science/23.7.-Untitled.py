import sys
import os
import time
import threading
from datetime import datetime
from PyQt5 import QtWidgets
import win32serviceutil
import win32service
import win32event
import servicemanager

# Clase para el servicio de Windows
class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = "MyPythonService"
    _svc_display_name_ = "My Python Service"
    _svc_description_ = "This service runs a specific executable at a specified time."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.running = False
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        while self.running:
            self.check_time_and_run_gui()
            time.sleep(60)  # Check every minute

    def check_time_and_run_gui(self):
        target_hour = 14  # Ejemplo: 14 para las 2:00 PM
        target_minute = 0

        now = datetime.now()
        servicemanager.LogInfoMsg(f"Checking time: {now.hour}:{now.minute}")
        if now.hour == target_hour and now.minute == target_minute:
            servicemanager.LogInfoMsg("Launching GUI")
            self.run_gui()

    def run_gui(self):
        # Ejecutar la GUI en un nuevo hilo
        threading.Thread(target=run_gui).start()

# Clase para la GUI
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Mi Aplicación GUI')
        self.setGeometry(100, 100, 800, 600)
        # Aquí puedes añadir los elementos de la GUI

def run_service():
    win32serviceutil.HandleCommandLine(MyService)

def run_gui():
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in ('install', 'update', 'remove', 'start', 'stop'):
        run_service()
    else:
        # Ejecutar el servicio en un hilo
        service_thread = threading.Thread(target=run_service)
        service_thread.start()