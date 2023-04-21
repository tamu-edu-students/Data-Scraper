import os

ID_of_pics = 1482
location = r"C:\Users\Jared\OneDrive\Desktop\Scraper\\"

for i in range(282, ID_of_pics + 1):
    old_name_temp = location + str(i) + ".JPEG"
    new_name_temp = location + str(i + 2637) + ".JPEG"
    os.rename(old_name_temp, new_name_temp)