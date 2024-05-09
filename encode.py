import base64

# Read the image file
with open("roadcase.png", "rb") as img_file:
    # Convert image to base64 format
    img_base64 = base64.b64encode(img_file.read()).decode()