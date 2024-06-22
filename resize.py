import cv2
import os

def resize_images_in_folder_with_opencv(folder_path, target_size=(1024, 1920)):
    """
    Resize all images in the specified folder to the target size using OpenCV.
    
    Parameters:
        folder_path (str): Path to the folder containing the images.
        target_size (tuple): Target size in the format (width, height).
    """
    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        # Construct the full path to the image file
        image_path = os.path.join(folder_path, filename)
        
        # Check if the file is a supported image file
        if filename.lower().endswith(('.png', '.jpg')):
            try:
                # Read the image
                img = cv2.imread(image_path)
                if img.shape != (1920, 1024, 3):    
                    # Resize the image to the target size
                    resized_img = cv2.resize(img, target_size)
                
                    # Save the resized image, overwriting the original file
                    cv2.imwrite(image_path, resized_img)
                
                    print(f"Resized {filename} successfully.")
                else:
                    print(f"{filename} not needed.")
            except Exception as e:
                print(f"Error resizing {filename}: {e}")

if __name__ == "__main__":
    folder_path = '/home/hamster02/courses/ugp_1/Motion_induction/tree/VOCdevkit/VOC2012/JPEGImages'  # Update this with the path to your folder
    resize_images_in_folder_with_opencv(folder_path)