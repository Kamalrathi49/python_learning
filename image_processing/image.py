from PIL import Image, ImageFilter

img = Image.open("./images/bulbasaur.jpg")

filtered_img = img.filter(ImageFilter.CONTOUR)
filtered_img.save("contour.png", "png")

print(filtered_img)
