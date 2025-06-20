all: slides pdf

slides:
	echo "Preparing slides"
	marp --pdf --html --allow-local-files "Nicla Vision Introdução.md"
	marp --html --allow-local-files "Nicla Vision Introdução.md"
	mv "Nicla Vision Introdução.pdf" "nicla-vision-slides.pdf"
	mv "Nicla Vision Introdução.html" "nicla-vision-slides.html"

pdf:
	echo "Preparing full A4 PDF"
	,md2pdf.sh "Nicla Vision Introdução.md"
	mv "Nicla Vision Introdução.pdf" "nicla-vision-a4paper.pdf"