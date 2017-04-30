build = ./output
path = $(shell ls | grep $*)
tpl = ./templates

rsheet = $(path)/sheet
rsolution = $(path)/solution
rslides = $(path)/slides

sheet = $(build)/BPP-$(path)-Sheet
solution = $(build)/BPP-$(path)-Solution
slides = $(build)/BPP-$(path)
notes = $(slides)-Notes

dateslides = $(shell [ -f $(path)/dates.txt ] && head -n1 $(path)/dates.txt || date "+%a, %d %b %Y")
datesheet = $(shell echo Deadline: `[ -f $(path)/dates.txt ] && tail -n1 $(path)/dates.txt || date "+%a, %d %b %Y"` 08:00 +0200)


%: builddir% slides% notes% sheet% solution% zip%
	@echo 'Done.'

all: clean outline 01 02 03 04 05
	@

outline: builddir%
	@pandoc \
		--bibliography=$(tpl)/bibliography.bib \
		-o $(build)/BPP-Outline.pdf \
		00_Meta/outline.md \
		$(tpl)/meta.yaml


zip%: builddir% sheet% solution%
	@if [ -f $(rsheet).list ]; then \
		echo Zipping exercises for $(path) ; \
		awk '{print "$(path)/" $$0}' $(rsheet).list | zip -@ $(sheet).zip ; \
		zip -j $(sheet).zip $(sheet).pdf ; \
	fi; \
	if [ -f $(rsolution).list ]; then \
		echo Zipping solutions for $(path) ; \
		awk '{print "$(path)/" $$0}' $(rsolution).list | zip -@ $(solution).zip ; \
		zip -j $(solution).zip $(solution).pdf ; \
	fi; \
	if [ -f $(rslides).list ]; then \
		echo Zipping slides for $(path) ; \
		awk '{print "$(path)/" $$0}' $(rslides).list | zip -@ $(slides).zip ; \
		zip -j $(slides).zip $(slides).pdf ; \
	fi


# Builds the uploadable slides
slides%: builddir%
	@if [ -f $(rslides).md ]; then \
		echo Creating slides for $(path) ; \
		pandoc \
			-t beamer \
			--filter panflute \
			--bibliography=$(tpl)/bibliography.bib \
			--highlight-style tango \
			-o $(slides).pdf \
			--metadata date='$(dateslides)' \
			$(path)/slides.md \
			$(tpl)/meta.yaml \
			$(tpl)/slides.yaml \
		; \
	fi


# Builds the lecture notes in a split slide pdf
notes%: builddir%
	@if [ -f $(rslides).md ]; then \
		echo Creating notes for $(path) ; \
		pandoc \
			-t beamer \
			--filter panflute \
			--bibliography=$(tpl)/bibliography.bib \
			--highlight-style tango \
			-o $(notes).pdf \
			--metadata date='$(dateslides)' \
			$(path)/slides.md \
			$(tpl)/meta.yaml \
			$(tpl)/notes.yaml \
		; \
	fi


# Builds the exercise sheet
sheet%: builddir%
	@if [ -f $(rsheet).md ]; then \
		echo Creating exercises for $(path) ; \
		pandoc \
			--filter panflute \
			--bibliography=$(tpl)/bibliography.bib \
			--highlight-style tango \
			-o $(sheet).pdf \
			--metadata date='$(datesheet)' \
			$(path)/sheet.md \
			$(tpl)/meta.yaml \
			$(tpl)/sheet.yaml \
		; \
	fi


# Builds the solution sheet
solution%: builddir%
	@if [ -f $(rsolution).md ]; then \
		echo Creating solutions for $(path) ; \
		pandoc \
			--filter panflute \
			--bibliography=$(tpl)/bibliography.bib \
			--highlight-style tango \
			-o $(solution).pdf \
			--metadata date='$(datesheet)' \
			$(path)/solution.md \
			$(tpl)/meta.yaml \
			$(tpl)/solution.yaml \
		; \
	fi


# Opens splitshow with the correct slides
present%: notes%
	open -a SplitShow $(notes).pdf


# Creates the build directory
builddir%:
	@mkdir -p $(build)


# Removes the build directory
clean:
	@rm -rf $(build)
