import os
baseurl = os.path.dirname(__file__)
print (baseurl)
"""
研究资料 % python pytree.py 
Conversion complete. The Markdown file has been saved as TOC.md.
"""
furl = os.path.join(baseurl,"..","docs/src/TRR_TOC.txt")
with open(furl,"r",encoding="utf8") as f:
    lines = f.readlines()

# if "├──" in line
# print(lines[:5])
mdls = ""

def cvt_letter(txt="AGGREGATE  POLISHING  RESISTANCE  PRE-EVALUATION.pdf"):
    try: 
        a,b = txt.split(".pdf")
    except:
        print (txt)
    return f"{a.title()}.pdf\n"



for line in lines:#[:20]:
    if ".pdf" in line[-5:]:
        # print(line)
        if "└──" in line:
            fname = line.split("└──")[1]
        else:
            fname = line.split("├──")[1]
        mdline =  f"* {cvt_letter(fname)}"
    elif "│   │   ├──" in line:
        mdline =  line.replace("│   │   ├──","### ")
    elif "│   ├──" in line:
        mdline =  line.replace("│   ├──","## ")
    elif "├──" in line:
        mdline =  line.replace("├──","# ")
    else:
        mdline = line
    # else:
        # print(f"# {line[3:]}")
    if "(1).pdf" in mdline:
        pass
    else:
        # print (mdline)
        mdls+= mdline

with open("TRR_TOC.md","w",encoding="utf-8") as f:
    f.write(mdls)