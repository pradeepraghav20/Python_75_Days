s="pradeep raghav"
if s.isdigit():
    print("Yess")
else:
    print("Noo")

s='<link rel="stylesheet" href="chrome://resources/css/text_defaults_md.cs>Pradeep Raghav>'
import  re
res=re.findall(r'<link rel="stylesheet".*?>(.*?)>',s)[0]
print(res)
