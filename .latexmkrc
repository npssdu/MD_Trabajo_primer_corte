# Configuración de latexmk (Ubicado en la raíz del proyecto)
$out_dir = 'documento/build';
$pdf_mode = 1;

$post_script = 'mkdir -p documento/pdf && cp documento/build/%b.pdf documento/pdf/Reporte.pdf';

