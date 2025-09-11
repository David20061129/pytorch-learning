from torch.utils.data import Dataset
from PIL import Image
import os

class Mydata(Dataset):
    def __init__(self,root_dir,label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir,self.label_dir)
        self.path_list = os.listdir(self.path)
    def __getitem__(self, index):
        image_name = self.path_list[index]
        image_item_path = os.path.join(self.path,image_name)
        image = Image.open(image_item_path)
        lable = self.label_dir
        image.show()
    def __len__(self):
        return len(self.path_list)
    
ant_dataset = Mydata("data\\hymenoptera_data\\train","ants")
ant_dataset.__getitem__(0)
print("success")