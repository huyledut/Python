from read_file import read_img
from read_camera import read_img_from_cam

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    size = (650, 650)
    camera_id = 0
    path = "videos/VID_1.mp4"
    read_img_from_cam(camera_id = camera_id, size = size, sleep = 1)