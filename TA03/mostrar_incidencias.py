    #Importar las funcionalidades (ET, json y prettytable)
import xml.etree.ElementTree as ET
import json
from prettytable import PrettyTable

def mostrar_incidencias(xml_file, json_file):
    # Parsear el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Crear una tabla
    tabla = PrettyTable()
    tabla.field_names = ["Email", "Nombre y Apellidos", "Fecha de Incidencia", "Tipo", "Equipo Afectado", "Área", "Descripción", "Nivel de Urgencia", "Acciones Previas"]

    incidencias_list = []

    # Extraer datos de la incidencia
    for incidencia in root.findall('Incidencia'):
        email = incidencia.find('InfoClient/Email').text
        nombre_apellidos = incidencia.find('InfoClient/NombreyApellidos').text
        fecha_incidencia = incidencia.find('InfoIncidencia/Fecha/fechaincidencia').text
        tipo = incidencia.find('InfoIncidencia/Detalles/Tipo').text
        equipo_afectado = incidencia.find('InfoIncidencia/Detalles/EquipoAfectado').text
        area = incidencia.find('InfoIncidencia/Detalles/Área').text
        descripcion = incidencia.find('InfoIncidencia/Detalles/DescripciónProblema').text
        nivel_urgencia = incidencia.find('InfoIncidencia/NivelUrgéncia').text
        acciones_previas = incidencia.find('InfoIncidencia/AccionesPrevias').text

        # Agregar una fila a la tabla
        tabla.add_row([email, nombre_apellidos, fecha_incidencia, tipo, equipo_afectado, area, descripcion, nivel_urgencia, acciones_previas])

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

    # Mostrar la tabla
    print(tabla)

    # Almacenar las incidencias en un archivo JSON
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(incidencias_list, f, ensure_ascii=False, indent=4)

# Ejecutar la función
if __name__ == "__main__":
    mostrar_incidencias('/home/daniel.lopez.7e8/TA03/Solicitud_de_Asistencia_Técnica (respostes).xml', 'incidencias.json')
