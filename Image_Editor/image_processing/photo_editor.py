from PIL import Image, ImageEnhance, ImageFilter
import os
import ast



path = '../imgs'
path_out = '../edited_imgs'


def parameters(params, path, path_out, filename):
    
        image = Image.open(f"{path}/{filename}")
        img = image
        
        if filename.endswith('.png'):
            img = image.convert('RGB')
            
        # sharpen the image
        sharpen = input("Do you want to sharpen the image? (y/n): ")
        if sharpen == 'y':
            img = img.filter(ImageFilter.SHARPEN)
            
        # enhance the image
        contrast = input("Do you want to enhance the image? (y/n): ")
        if contrast == 'y':
            factor = 1.5
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(factor)
            
        # crop the image
        crop_image = input("Do you want to crop the image? (y/n): ")
        if crop_image == 'y':
            box = (100, 100, 400, 400)
            img = img.crop(box)
            
        clean_name = os.path.splitext(filename)[0]
            
        img.save(f"{path_out}/{clean_name}_edited.jpg")
        print(f"{filename} edited successfully +")
      


def asset_editing(bulk, edit_type):
    edit_type = edit_type.split()
    
    if bulk == "b":
        for filename in os.listdir(path):
            parameters(edit_type, path, path_out, filename)
        print("Bulk editing done!")    
    elif bulk == "i":
        print("Individual editing done!")
    else:
        print("Invalid input!")
    
        
        
        
        

# user interaction in the terminal
initiate = input("Bulk editing (b) --- Individual editing (i):\n")

user_input = input("Type the image processing method: \n>> Sharpen\n>> Enhance\n>> Crop\n if you want to apply all or more than one type 'All' or ex. 'Sharpen Enhance'\n")

# user_dict = ast.literal_eval(user_input)

if initiate == 'b':
    pass
    # print(user_input)
    asset_editing(initiate, user_input)