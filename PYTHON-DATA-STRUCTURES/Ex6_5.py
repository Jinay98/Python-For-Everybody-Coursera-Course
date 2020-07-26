text = "X-DSPAM-Confidence:    0.8475";
index = text.find("0")
no  = float(text[index:])
print(no)
