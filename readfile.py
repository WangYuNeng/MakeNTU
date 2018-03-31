import time

def read(file_name):
    txt = open(file_name,'r', encoding='latin-1')
    out=txt.read()
    string_list=[]
    string_list.append(time.strftime("%m%d-%H:%M:%S", time.localtime()))
    name_list = ["frequency", "close_eye", "yawn", "posture", "unknown"]
    for target in name_list:
        target_content = ""
        pos =  out.find(target)
        pos += (len(target)+3)
        for i in range(pos, len(out)):
            if target == "frequency" and out[i] == ' ':
                for j in range(i+1,len(out)):
                    target_content += out[j]
                    if out[j+1] == ',':
                        break
                break

            if out[i] == '\"':
                for j in range(i+1,len(out)):
                    target_content += out[j]
                    if out[j+1] == '\\':
                        break
                break
        string_list.append(target_content)
    txt.close()
    return string_list

