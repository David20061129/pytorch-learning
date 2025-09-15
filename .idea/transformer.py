from torchvision import transforms
from PIL import Image
import cv2

path = "data\\hymenoptera_data\\train\\ants\\0013035.jpg"
numpy_picture = cv2.imread(path)
print(numpy_picture)
img = Image.open(path)
tens = transforms.ToTensor()
to = tens(img)
print(to)
print(tens(numpy_picture))
