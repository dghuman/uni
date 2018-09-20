(TeX-add-style-hook
 "Assignment_3"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "10pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("geometry" "letterpaper" "left=25mm" "right=25mm")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "ragged2e"
    "fancyhdr"
    "amsmath"
    "amsthm"
    "amssymb"
    "bbm"
    "inputenc"
    "geometry")
   (TeX-add-symbols
    "Z"
    "R"
    "Q"
    "C"))
 :latex)

