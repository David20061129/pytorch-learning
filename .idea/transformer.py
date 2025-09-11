from torchvision import transforms
from PIL import Image
path = "data\\hymenoptera_data\\train\\ants\\0013035.jpg"
img = Image.open(path)
tens = transforms.ToTensor()
to = tens(img)
print(to)