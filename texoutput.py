def texheader(title,author=""):
    lines="""\documentclass[a4paper,12pt,parskip=half]{scrartcl}
    \\title{""" + title + """}
    \\author{""" + author + """}
    \\usepackage{ulem}
    \\begin{document}
    \\maketitle\n"""
    return lines

def texify(cogstate):
    # define the language
    language = cogstate[0]['values'].keys()
    # the main stuff
    lines="""\\begin{tabular}{|c|"""+('c'*len(language))+"""|}
    \\hline \n             """
    for prop in language:
      lines = lines + " & $"+prop+"$"
    lines = lines + " \\\\ \n    \hline \n"
    for world in cogstate:
      if not world["meta"]["US"]:
        lines=lines+"\sout{$"+str(world["meta"]["name"])+"$}"
      elif world["meta"]["FS"]:
	lines=lines+"      $|"+str(world["meta"]["name"])+"$"
      else:
	lines=lines+"       $"+str(world["meta"]["name"])+"$"
      for prop in language:
	lines = lines + "  &  " + str(world["values"][prop])
      lines = lines + "  \\\\ \n"
    lines= lines + """    \hline
    \\end{tabular}"""
    return lines

def texfooter():
    lines="""\n\\end{document}"""
    return lines