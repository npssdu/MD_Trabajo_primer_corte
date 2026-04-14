import json
import base64
import os

notebook_path = '/home/limonada/Documents/Projects/Uni Projects/mineria de datos/MD_Trabajo_primer_corte/MD_Trabajo_Primer_Corte.ipynb'
output_dir = '/home/limonada/Documents/Projects/Uni Projects/mineria de datos/MD_Trabajo_primer_corte/documento/img/graphs'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

count = 0
for cell in nb['cells']:
    if 'outputs' in cell:
        for output in cell['outputs']:
            if 'data' in output and 'image/png' in output['data']:
                png_data = output['data']['image/png']
                count += 1
                file_path = os.path.join(output_dir, f'grafica_{count}.png')
                with open(file_path, 'wb') as f_out:
                    f_out.write(base64.b64decode(png_data))
                print(f'Saved grafica_{count}.png')

print(f'Total {count} graphs saved.')
