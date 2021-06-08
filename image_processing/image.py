from PIL import Image, ImageFilter

img = Image.open("./images/bulbasaur.jpg")

box = (100, 100, 400, 400)
filtered_img = img.crop(box)
filtered_img.save("cropped_img.png", "png")
print(filtered_img)
