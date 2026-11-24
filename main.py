
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from interfaz_ui import Ui_Form


class MiFormulario(QWidget):

    def __init__(self):
        super().__init__()

        # Cargar la interfaz visual
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Conectar el botón Enviar
        self.ui.btnEnviar.clicked.connect(self.guardar_datos)

    def guardar_datos(self):

        # Obtener los datos de cada campo
        nombre = self.ui.txtNombre.text().strip()
        apellido = self.ui.txtApellido.text().strip()
        matricula = self.ui.txtMatricula.text().strip()
        telefono = self.ui.txtTelefono.text().strip()

        # Validar que los campos no estén vacíos
        if not nombre or not apellido or not matricula or not telefono:
            QMessageBox.warning(
                self,
                "Advertencia",
                "Por favor completa todos los campos."
            )
            return

        # Guardar la información en un archivo de texto
        try:
            with open("datos.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"Nombre: {nombre}\n")
                archivo.write(f"Apellido: {apellido}\n")
                archivo.write(f"Matrícula: {matricula}\n")
                archivo.write(f"Teléfono: {telefono}\n")
                archivo.write("-" * 30 + "\n")

        except OSError as error:
            QMessageBox.critical(
                self,
                "Error",
                f"No se pudieron guardar los datos:\n{error}"
            )
            return

        # Mostrar mensaje de éxito
        QMessageBox.information(
            self,
            "Éxito",
            "Los datos se guardaron correctamente en datos.txt"
        )

        # Limpiar los campos
        self.ui.txtNombre.clear()
        self.ui.txtApellido.clear()
        self.ui.txtMatricula.clear()
        self.ui.txtTelefono.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiFormulario()
    ventana.show()
    sys.exit(app.exec())
