def texify(cogstate,language):
    lines="""\documentclass[a4paper,12pt,parskip=half]{scrartcl}\n\\begin{document}
    \\begin{tabular}{|c|ccccccccccccccccccccccccccccccc|}
    \\hline \n          """
    for prop in language:
      lines = lines + " & $"+prop+"$"
    lines = lines + " \\\\ \n    \hline \n"
    for world in cogstate:
      lines=lines+"       $"+str(world["meta"]["NAME"])+"$"
      for prop in language:
	lines = lines + "  &  " + str(world["values"][prop])
      lines = lines + "  \\\\ \n"
    lines= lines + """    \hline
    \\end{tabular}\n\\end{document}"""
    return lines