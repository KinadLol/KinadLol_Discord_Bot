from PIL import Image, ImageDraw

image = Image.open("Images/PP.webp")

w, h = image.size

mask = Image.new('L', (w, h), 0)

draw = ImageDraw.Draw(mask)

draw.ellipse((0, 0, w, h), fill = 255)

result = Image.new("RGBA",(w, h))

result.paste(image, (0,0), mask = mask)

result.save('circleCropped.png')

fond = Image.open("Images/bienvenue.png")

pp = Image.open("circleCropped.png")
test = pp.resize((197,197), Image.BICUBIC)
fondw, fondh = fond.size

final = Image.new("RGBA",(fondw, fondh))

final.paste(fond, (0,0))
final.paste(test, (792, 142), mask= test)

final.save('testing.png')