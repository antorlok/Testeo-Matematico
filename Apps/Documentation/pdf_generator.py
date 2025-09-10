import os
from jinja2 import Environment, FileSystemLoader
import pdfkit

def generate_pdf():
    # Configuración de Jinja2 para cargar la plantilla HTML
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))
    template = env.get_template("documentation_template.html")

    # Diccionario con los datos para la plantilla
    context = {
        "firstIterationErrors": 12,
        "secondIterationErrors": 15,
        "thirdIterationErrors": 10,
        "fourthIterationErrors": 14,
        "fifthIterationErrors": 15,
        "summatoryErrorsResult": 66,
        "avarageErrorsResults": 13.2,
        "firstDifference": -1.2,
        "secondDifference": 1.8,
        "thirdDifference": -3.2,
        "fourthDifference": 0.8,
        "fifthDifference": 1.8,
        "firstDifferenceSquare": 1.44,
        "secondDifferenceSquare": 3.24,
        "thirdDifferenceSquare": 10.24,
        "fourthDifferenceSquare": 0.64,
        "fifthDifferenceSquare": 3.24,
        "variance": 3.76,
        "desviacion": 1.94,
        # Ruta absoluta de la imagen final, compatible con wkhtmltopdf y sin espacios
        "imagen_final": "file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "cap.png")).replace("\\", "/"),
    }

    # Renderizar la plantilla con los datos
    html_out = template.render(context)

    # Guardar el HTML temporalmente
    temp_html_path = os.path.join(os.path.dirname(__file__), "temp_documentation.html")
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_out)


    # Configuración de pdfkit (wkhtmltopdf)
    options = {
        'enable-local-file-access': None  # Permite acceso a archivos locales para imágenes
    }
    # Buscar wkhtmltopdf primero en una ruta local, luego en variable de entorno, luego usar default
    local_wkhtmltopdf = os.path.join(os.path.dirname(__file__), 'wkhtmltopdf', 'bin' ,'wkhtmltopdf.exe')
    default_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'

    if os.path.isfile(local_wkhtmltopdf):
        wkhtmltopdf_path = local_wkhtmltopdf
    elif os.path.isfile(default_wkhtmltopdf):
        wkhtmltopdf_path = default_wkhtmltopdf
    else:
        raise FileNotFoundError(
            'No se encontró el ejecutable wkhtmltopdf.\n'
            'Coloca wkhtmltopdf.exe en "Apps/Documentation/wkhtmltopdf/", o define la variable de entorno WKHTMLTOPDF_PATH, '
            'o instala wkhtmltopdf en "C:/Program Files/wkhtmltopdf/bin/".'
        )
    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

    # Generar PDF a partir del HTML
    pdf_output_path = os.path.join(os.path.dirname(__file__), "documentation1.pdf")
    pdfkit.from_file(temp_html_path, pdf_output_path, options=options, configuration=config)

    # Eliminar archivo HTML temporal
    os.remove(temp_html_path)

    print(f"PDF generado correctamente en: {pdf_output_path}")

if __name__ == "__main__":
    generate_pdf()
