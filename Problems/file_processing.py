i_f=r"C:\Users\manikandan.r\OneDrive - InTimeTec Visionsoft Pvt. Ltd.,\Desktop\Python_assignment2\text_file_processing\input.txt"
o_f=r"C:\Users\manikandan.r\OneDrive - InTimeTec Visionsoft Pvt. Ltd.,\Desktop\Python_assignment2\text_file_processing\output.txt"
with open(i_f, "r") as f:
    text = f.read()
s_c=text.count(" ")
words=text.split()
cw= [i.capitalize() for i in words]
n_w=" ".join(cw)
with open(o_f, "w") as f:
    f.write(n_w)
print("text:", n_w)
print("Total spaces:", s_c)