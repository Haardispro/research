from PIL import Image, ImageDraw
import cv2
import os 

img = Image.new("RGB", (500,500), (0, 0, 0))
draw = ImageDraw.Draw(img)

"""
for size in [1,25]:
    for n in range(step,w,step):
        for x in range(step,h-step,step):
            draw.ellipse([n-size/2,x-size/2,n+size//2,x+size//2], fill="yellow")
    img.save('size_{:d}.png'.format(size))
"""
"""
n = 1 
x = 25
draw.polygon([(250, 250+20), (300, 250+20), (300, 300+20), (250, 300+20)], fill="yellow")
img.save("test.png")


draw.polygon([(250, 250+20), (300, 250+20), (300, 300+20), (250, 300+20)], fill="black")
draw.polygon([(250, 250), (300, 250), (300, 300), (250, 300)], fill="yellow")
img.save("test1.png")
"""
"""
draw.polygon([(240, 0), (260, 0), (260,20), (240, 20)], fill="white")
img.save("test.png")
"""


# need a program that spits out the values of y wrt g 

# total t = 9.79secs
# total distance to be covered = 480m 

images = []

a = 10 
y = 0 
x = 250
t = 0 
for i in range(10):
    draw.point((x,y), fill="white")
    img.save(f"images/{i}.jpg")
#    images.append(f"{i}.jpg")
    draw.point((x,y), fill="black")
    y = (1/2)*a*(t**2)
    draw.point((x, y), fill="white")    
    t = t+1 
    print(y)
    img.save(f"images/{i+1}.jpg")
#    images.append(f"{i+1}.jpg")

"""
image_folder = "images/"
video_name = "test.avi"

frame = cv2.imread(os.path.join(image_folder, images[0]))

height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 60, (width, height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

#os.system("sudo rm -r images/*")


"""



