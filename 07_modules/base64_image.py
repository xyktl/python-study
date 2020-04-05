import base64
with open("./index.gif","rb") as f:
    base64_data = base64.b64encode(f.read())
    print(base64_data)

#图片加密