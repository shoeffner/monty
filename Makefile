path = $(shell ls | grep $*)
build = ./output

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


zip%: builddir% sheet% solution%
	@if [ -f $(rsheet).list ]; then \
		echo Zipping exercises for $(path) ; \
		awk '{print "$(path)/" $$0} END {print "$(sheet).pdf"}' $(rsheet).list | zip -@ $(sheet).zip \
		; \
	fi; \
	if [ -f $(rsolution).list ]; then \
		echo Zipping solutions for $(path) ; \
		awk '{print "$(path)/" $$0} END {print "$(solution).pdf"}' $(rsolution).list | zip -j -@ $(solution).zip \
		; \
	fi


# Builds builds the uploadable slides
slides%: builddir%
	@if [ -f $(rslides).md ]; then \
		echo Creating slides for $(path) ; \
		pandoc \
			-t beamer \
			--filter pandoc-img-glob \
			-o $(slides).pdf \
			--metadata date='$(dateslides)' \
			$(path)/slides.md \
			./templates/meta.yaml \
			./templates/slides.yaml \
		; \
	fi


# Builds the lecture notes in a split slide pdf
notes%: builddir%
	@if [ -f $(rslides).md ]; then \
		echo Creating notes for $(path) ; \
		pandoc \
			-t beamer \
			--filter pandoc-img-glob \
			-o $(notes).pdf \
			--metadata date='$(dateslides)' \
			$(path)/slides.md \
			./templates/meta.yaml \
			./templates/notes.yaml \
		; \
	fi


# Builds the exercise sheet
sheet%: builddir%
	@if [ -f $(rsheet).md ]; then \
		echo Creating exercises for $(path) ; \
		pandoc \
			--filter pandoc-img-glob \
			-o $(sheet).pdf \
			--metadata date='$(datesheet)' \
			$(path)/sheet.md \
			./templates/meta.yaml \
			./templates/sheet.yaml \
		; \
	fi


# Builds the solution sheet
solution%: builddir%
	@if [ -f $(rsolution).md ]; then \
		echo Creating solutions for $(path) ; \
		pandoc \
			--filter pandoc-img-glob \
			-o $(solution).pdf \
			--metadata date='$(datesheet)' \
			$(path)/solution.md \
			./templates/meta.yaml \
			./templates/solution.yaml \
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
