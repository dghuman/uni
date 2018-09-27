(TeX-add-style-hook
 "QP3_ProblemSet3_Q2"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("ucs" "mathletters") ("inputenc" "utf8x") ("enumitem" "inline") ("ulem" "normalem")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "fontenc"
    "mathpazo"
    "graphicx"
    "caption"
    "adjustbox"
    "xcolor"
    "enumerate"
    "geometry"
    "amsmath"
    "amssymb"
    "textcomp"
    "upquote"
    "eurosym"
    "ucs"
    "inputenc"
    "fancyvrb"
    "grffile"
    "hyperref"
    "longtable"
    "booktabs"
    "enumitem"
    "ulem")
   (TeX-add-symbols
    '("WarningTok" 1)
    '("InformationTok" 1)
    '("AttributeTok" 1)
    '("PreprocessorTok" 1)
    '("ExtensionTok" 1)
    '("BuiltInTok" 1)
    '("OperatorTok" 1)
    '("ControlFlowTok" 1)
    '("VariableTok" 1)
    '("CommentVarTok" 1)
    '("AnnotationTok" 1)
    '("DocumentationTok" 1)
    '("ImportTok" 1)
    '("SpecialStringTok" 1)
    '("VerbatimStringTok" 1)
    '("SpecialCharTok" 1)
    '("ConstantTok" 1)
    '("NormalTok" 1)
    '("ErrorTok" 1)
    '("RegionMarkerTok" 1)
    '("FunctionTok" 1)
    '("AlertTok" 1)
    '("OtherTok" 1)
    '("CommentTok" 1)
    '("StringTok" 1)
    '("CharTok" 1)
    '("FloatTok" 1)
    '("BaseNTok" 1)
    '("DecValTok" 1)
    '("DataTypeTok" 1)
    '("KeywordTok" 1)
    "tightlist"
    "maxwidth"
    "Oldincludegraphics"
    "br"
    "gt"
    "lt"
    "PY"
    "PYZbs"
    "PYZus"
    "PYZob"
    "PYZcb"
    "PYZca"
    "PYZam"
    "PYZlt"
    "PYZgt"
    "PYZsh"
    "PYZpc"
    "PYZdl"
    "PYZhy"
    "PYZsq"
    "PYZdq"
    "PYZti"
    "PYZat"
    "PYZlb"
    "PYZrb")
   (LaTeX-add-environments
    "Shaded"))
 :latex)

