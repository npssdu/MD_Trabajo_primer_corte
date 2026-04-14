# Configuración avanzada de latexmk (Raíz del proyecto)

# 1. Definir dónde va la "basura" (archivos auxiliares)
$out_dir = 'documento/build';
$aux_dir = 'documento/build';

# 2. Configurar rutas de búsqueda (TEXINPUTS)
# Esto permite usar \input{content/file} desde la raíz sin problemas.
# Se añaden las carpetas de origen y recursos al path de LaTeX.
$ENV{'TEXINPUTS'} = ".:./documento/src:./documento/img:./documento/src/content:" . ($ENV{'TEXINPUTS'} // "");

# 3. Modo PDF (5 = xelatex → necesario para fontspec / fuente Aptos)
$pdf_mode = 5;

# 4. Mover el PDF final a la carpeta /pdf después de compilar
$post_script = 'mkdir -p documento/pdf && cp documento/build/%b.pdf documento/pdf/%b.pdf';
