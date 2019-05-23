from PIL import Image
from resizeimage import resizeimage

image = Image.open('37.png')
new_image = image.resize((500, 400))
new_image.save('image_400.png')