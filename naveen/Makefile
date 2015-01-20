Src=paper

all : dirs tex bib  tex tex done

one : dirs tex done 

view :
	- cp $(HOME)/tmp/$(Src).pdf .; evince $(HOME)/tmp/$(Src).pdf &

timm :
	cp $(HOME)/tmp/$(Src).pdf $(HOME)/public_html/tmp

done :
	@printf "\n\n\n==============================================\n"
	@printf       "see output in $(HOME)/tmp/$(Src).pdf\n"
	@printf       "==============================================\n\n\n"
	@printf "\n\nWarnings (may be none):\n\n"
	grep arning $(HOME)/tmp/${Src}.log; cp $(HOME)/tmp/$(Src).pdf .

dirs : 
	- [ ! -d $(HOME)/tmp ] && mkdir $(HOME)/tmp

tex :
	- pdflatex -output-directory=$(HOME)/tmp $(Src)

embedfonts:
	@ gs -q -dNOPAUSE -dBATCH -dPDFSETTINGS=/prepress -sDEVICE=pdfwrite \
          -sOutputFile=$(HOME)/tmp/$(Src)-embedded.pdf $(HOME)/tmp/$(Src).pdf
	@ mv              $(HOME)/tmp/$(Src)-embedded.pdf $(HOME)/tmp/$(Src).pdf	

bib : 
	- cp thesis.bib $(HOME)/tmp; cd $(HOME)/tmp; bibtex $(Src)


