import os
import random
from app.finder.ImageFinder import ImageFinder
from app.api.ApiBuilder import ApiBuilder

home_dir = os.path.expanduser('~')
images_dir = home_dir + '/Изображения/'


class ImageGetter:

    def __init__(self):
        self.finder = ImageFinder()

    def run(self):
        depth = 0
        image_list = self.finder.run()
        while len(image_list) < 1 and depth < 10:
            self.finder.command_line_args = ["-r", "--max-depth"]
            depth += 1
            self.finder.command_line_args.insert(2, str(depth))
            image_list = self.finder.run()
        if depth >= 10:
            print("Max depth exceeded")
        if len(image_list) > 1:
            your = random.randrange(0, len(image_list) - 1, 1)
        else:
            your = image_list[0]
        your_json = ApiBuilder().convert_to_json(your)
        # print(your.path)
        return your_json


if __name__ == '__main__':
    ImageGetter().run()
