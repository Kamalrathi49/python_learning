from PIL import Image, ImageFilter

img = Image.open("./images/bulbasaur.jpg")

filtered_img = img.rotate(-90)
filtered_img.save("rotated_img2.png", "png")
print(filtered_img)
