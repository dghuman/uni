(TeX-add-style-hook
 "Assignment Template"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("ragged2e" "document") ("inputenc" "utf8")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "ragged2e"
    "geometry"
    "fancyhdr"
    "amsmath"
    "amsthm"
    "amssymb"
    "inputenc")
   (TeX-add-symbols
    "R"
    "Z"
    "Q"
    "N")
   (LaTeX-add-environments
    "definition"))
 :latex)

