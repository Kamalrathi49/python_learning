from PIL import Image, ImageFilter

img = Image.open("./images/profile_img.jpg")

img.thumbnail((150, 150))
img.save("profile123.jpg", "png")
