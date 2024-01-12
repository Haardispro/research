from PIL import Image, ImageDraw
import cv2 
import os

new = Image.new(mode="RGB", size=(500, 500), color="black")

#x = 250
y = 20 

images = []

for i in range(460):
    point_draw = ImageDraw.Draw(new)
    point_draw.polygon([(240, y), (260, y), (260, 20+y), (240, 20+y)], fill="white")
    new.save(f"frames/{i}.jpg")
    images.append(f"{i}.jpg")

    point_draw.polygon([(240, y), (260, y), (260, 20+y), (240, 20+y)], fill="black")
#    point_draw.point((x,y), fill="black")
#    x = x+1
    y = y+1

    point_draw.polygon([(240, y), (260, y), (260, 20+y), (240, 20+y)], fill="white")
#    point_draw.point((x,y), fill="white")
    new.save(f"frames/{i+1}.jpg")
    images.append(f"{i+1}.jpg")



image_folder = "frames/"
video_name = "video.avi"

frame = cv2.imread(os.path.join(image_folder, images[0]))

height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 50, (width, height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

#os.system("sudo rm -r frames/*")
