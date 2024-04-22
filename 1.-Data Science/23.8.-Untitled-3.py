from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication([])

    # Creamos un botón
    button = QtWidgets.QPushButton("Presionar")

    # Estilo CSS para el botón cuando está presionado
    style = "background-color: red;"
    pressed_style = "background-color: black;"
    button.setStyleSheet(
        f"QPushButton {{ {style} }}"
        f"QPushButton:pressed {{ {pressed_style} }}"
    )

    # Creamos el diseño
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(button)

    # Creamos la ventana
    window = QtWidgets.QWidget()
    window.setLayout(layout)
    window.setWindowTitle("Botón Presionado")
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()