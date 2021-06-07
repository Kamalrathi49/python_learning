from PIL import Image, ImageFilter

img = Image.open("./images/bulbasaur.jpg")

filtered_img = img.convert("L")
filtered_img.save("converted_img.png", "png")

print(filtered_img)
