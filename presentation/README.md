Presentación: convertir Markdown a PPTX/PDF

Este directorio contiene `STREAMACCOUNTS_presentation.md`, que incluye las 4 diapositivas y notas del orador.

Opciones para obtener una presentación (.pptx / .pdf):

1) Usar Pandoc (recomendado para convertir a PDF/PowerPoint)
- Requisitos: `pandoc` instalado y (opcional) `wkhtmltopdf` para HTML -> PDF o `libreoffice` para otras conversiones.

Comando para instalar pandoc (Windows, choco):
```pwsh
choco install pandoc
```

Convertir a PowerPoint (.pptx):
```pwsh
pandoc presentation/STREAMACCOUNTS_presentation.md -o presentation/StreamAccounts.pptx
```

Convertir a PDF:
```pwsh
pandoc presentation/STREAMACCOUNTS_presentation.md -o presentation/StreamAccounts.pdf
```

2) Crear la presentación manualmente en PowerPoint/Google Slides
- Abre el archivo Markdown, copia el contenido y pega cada sección en una diapositiva.
- Inserta las capturas en `presentation/screenshots/` si las agregas.

3) Usar reveal.js (para presentación web)
- Puedes convertir el Markdown a HTML usando `reveal-md` o `pandoc` con plantilla reveal.js.

Notas:
- Coloca las capturas de pantalla en `presentation/screenshots/` con los nombres indicados en el Markdown.
- Rellena los campos de portada (`Integrantes`) en `STREAMACCOUNTS_presentation.md` antes de convertir.

Si quieres, puedo:
- Generar automáticamente un archivo `.pptx` (si me confirmas que instale/ejecute `pandoc` aquí — necesito permisos para instalar), o
- Crear una carpeta `presentation/screenshots/` con placeholders (archivos PNG en blanco) que luego sustituyas con las capturas reales.
