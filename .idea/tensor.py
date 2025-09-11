from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np
path = "data\\hymenoptera_data\\train\\ants\\0013035.jpg"
image = Image.open(path)
image_np=np.array(image)
image.show()
print (type(image_np))
print(image_np.shape)
writer = SummaryWriter("logs")
writer.add_image("test",image_np,1,dataformats='HWC')
writer.add_image("test",np.array(Image.open("data\\hymenoptera_data\\train\\ants\\5650366_e22b7e1065.jpg")),1,dataformats='HWC')
for i in range (100):
    writer.add_scalar("y=x",2*i,i)
writer.close()