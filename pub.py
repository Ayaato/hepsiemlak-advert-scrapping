backslash = '\ '.replace(' ','')

def publisher(titlename):
    i = 0
    characters = ['"',":","*","?",'<','>','|',"/",backslash,'+','!','^',"'",'#','$','%','½','£','{','}',
    '(',')','/','[',']','=','-','_',';','`','.']
    for character in characters:
        i=i+1
        if character in titlename:
            titlename = titlename.replace(character,"")
        if len(characters)==i+1:
            return titlename 
        else:
            continue