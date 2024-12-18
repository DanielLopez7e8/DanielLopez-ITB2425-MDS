import xml.etree.ElementTree as ET
import json
from colorama import Fore, init

# Inicializar colorama
init(autoreset=True)

def ajustar_texto(texto, max_length):
    """Recorta el texto si excede max_length, añadiendo '...' al final."""
    if len(texto) > max_length:
        return texto[:max_length - 3] + '...'  # 3 caracteres para '...'
    return texto

def mostrar_incidencias(xml_file, json_file):
    # Parsear el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Encabezados de la tabla
    headers = [
        "Email",
        "Nombre y Apellidos",
        "Fecha de Incidencia",
        "Tipo",
        "Equipo Afectado",
        "Área",
        "Descripción",
        "Nivel de Urgencia",
        "Acciones Previas"
    ]

    # Definir el ancho de cada columna
    col_widths = [60, 60, 40, 30, 50, 30, 100, 40, 40]

    # Imprimir encabezados
    header_row = "".join(f"{Fore.CYAN}{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
    print(header_row)
    print("=" * sum(col_widths))  # Línea divisoria

    incidencias_list = []

    # Extraer datos de la incidencia
    for incidencia in root.findall('Incidencia'):
        email = incidencia.find('InfoClient/Email').text or "N/A"
        nombre_apellidos = incidencia.find('InfoClient/NombreyApellidos').text or "N/A"
        fecha_incidencia = incidencia.find('InfoIncidencia/Fecha/fechaincidencia').text or "N/A"
        tipo = incidencia.find('InfoIncidencia/Detalles/Tipo').text or "N/A"
        equipo_afectado = incidencia.find('InfoIncidencia/Detalles/EquipoAfectado').text or "N/A"
        area = incidencia.find('InfoIncidencia/Detalles/Área').text or "N/A"
        descripcion = incidencia.find('InfoIncidencia/Detalles/DescripciónProblema').text or "N/A"
        nivel_urgencia = incidencia.find('InfoIncidencia/NivelUrgéncia').text or "N/A"
        acciones_previas = incidencia.find('InfoIncidencia/AccionesPrevias').text or "N/A"

        # Definir color para el nivel de urgencia
        if nivel_urgencia == "Muy Urgente":
            nivel_color = Fore.RED
        elif nivel_urgencia == "Urgente":
            nivel_color = Fore.YELLOW
        else:
            nivel_color = Fore.GREEN

        # Imprimir los datos de cada incidencia, ajustando el texto
        data_row = "".join(f"{Fore.WHITE}{ajustar_texto(data, col_widths[i]):<{col_widths[i]}}" for i, data in enumerate([
            email, nombre_apellidos, fecha_incidencia, tipo, equipo_afectado,
            area, descripcion, acciones_previas
        ]))
        
        print(data_row + nivel_color + f"{nivel_urgencia:<{col_widths[-1]}}")

        # Agregar la incidencia a la lista
        incidencias_list.append({
            "Email": email,
            "Nombre y Apellidos": nombre_apellidos,
            "Fecha de Incidencia": fecha_incidencia,
            "Tipo": tipo,
            "Equipo Afectado": equipo_afectado,
            "Área": area,
            "Descripción": descripcion,
            "Nivel de Urgencia": nivel_urgencia,
            "Acciones Previas": acciones_previas
        })

    # Almacenar las incidencias en un archivo JSON
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(incidencias_list, f, ensure_ascii=False, indent=4)

# Ejecutar la función
if __name__ == "__main__":
    mostrar_incidencias('/home/daniel.lopez.7e8/DanielLopez-ITB2425-MDS/TA03/Solicitud_de_Asistencia_Técnica (respostes).xml', 'incidencias.json')


