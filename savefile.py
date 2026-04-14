import json
import os
import base64

# Configuración de rutas
notebook_path = 'MD_Trabajo_Primer_Corte.ipynb'
output_dir = 'documento/img/graphs'

# Crear el directorio si no existe
os.makedirs(output_dir, exist_ok=True)

# Leer el notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

graph_count = 0

# Recorrer celdas y salidas
for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        for output in cell.get('outputs', []):
            # Buscar datos de imagen en la salida
            data = output.get('data', {})
            if 'image/png' in data:
                graph_count += 1
                image_data = data['image/png']
                
                # Nombre del archivo (puedes ajustarlo)
                file_name = f'grafica_{graph_count}.png'
                file_path = os.path.join(output_dir, file_name)
                
                # Decodificar y guardar
                with open(file_path, 'wb') as img_file:
                    img_file.write(base64.b64decode(image_data))
                
                print(f'Guardada: {file_path}')

print(f'\nProceso finalizado. Se extrajeron {graph_count} gráficas en {output_dir}')
