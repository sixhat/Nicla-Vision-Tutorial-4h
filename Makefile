all: clean zip slide gith

clean:
	echo "Delete previous Zips"
	rm -f dist/*.zip

zip:
	echo "Zipping Code"
	zip -r9 dist/nicla-vision-code.zip code

slide:
	echo "Making Slides"
	cd slides && make -f Makefile

gith:
	git commit -a -m "new build"
