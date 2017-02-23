path = $(shell ls | grep $*)

rsheet = $(path)/sheet
rsolution = $(path)/solution
rslides = $(path)/slides

sheet = $(path)/BPP-Sheet$(path)
solution = $(path)/BPP-Solution$(path)
slides = $(path)/BPP-$(path).pdf


%: slides% sheet% solution% zip%
	@echo 'Done.'

zip%:
	@if [ -f $(rsheet).list ]; then \
		awk '{print "$(path)/" $$0} END {print "$(sheet).pdf"}' $(rsheet).list | zip -@ $(sheet).zip \
		; \
	fi; \
	if [ -f $(rsolution).list ]; then \
		awk '{print "$(path)/" $$0} END {print "$(solution).pdf"}' $(rsolution).list | zip -@ $(solution).zip \
		; \
	fi

slides%:
	@if [ -f $(rslides).md ]; then \
		pandoc \
			-t beamer \
			-o $(slides).pdf \
			$(path)/slides.md \
		; \
	fi

sheet%:
	@if [ -f $(rsheet).md ]; then \
		pandoc \
			-o $(sheet).pdf \
			$(path)/sheet.md \
		; \
	fi

solution%:
	@if [ -f $(rsolution).md ]; then \
		pandoc \
			-o $(solution).pdf \
			$(path)/solution.md \
		; \
	fi

clean:
	@rm -rf ./*/*.pdf ./*/*.zip
