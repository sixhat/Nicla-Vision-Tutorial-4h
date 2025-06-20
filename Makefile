all: zip slide

zip:
	echo "Zipping Code"
	zip -r9 dist/nicla-vision-code.zip code

slide:
	echo "Making Slides"
	cd slides && make -f Makefile