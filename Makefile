path = $(shell ls | grep $*)

%: slides% sheet%
	@:

slides%:
	@if [ -f $(path)/slides.md ]; then \
		pandoc \
			-t beamer \
			-o $(path)/BPP$(path).pdf \
			$(path)/slides.md \
		; \
	fi

sheet%:
	@if [ -f $(path)/sheet.md ]; then \
		pandoc \
			-o $(path)/BPP-Sheet$(path).pdf \
			$(path)/sheet.md \
		; \
	fi

clean:
	rm -rf ./*/*.pdf
