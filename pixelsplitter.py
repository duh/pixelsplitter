from PIL import Image
import argparse

argparser = argparse.ArgumentParser(description="Splits the pixels of an image into their RGB components (3x3 grid of red, green, blue), returning an image 3 times larger", epilog="@duh")
argparser.add_argument('source_path', type=str)
argparser.add_argument('output_path', type=str)
args = argparser.parse_args()

target_image = Image.open(args.source_path)
target_image = target_image.convert("RGB")

split_image = Image.new('RGB', (target_image.width * 3, target_image.height), (0,0,0))
split_image_data = []

target_image_data = target_image.getdata()

for item in target_image_data:
        split_image_data.append((item[0], 0, 0))
        split_image_data.append((0, item[1], 0))
        split_image_data.append((0, 0, item[2]))
        
split_image.putdata(split_image_data);
split_image = split_image.resize((split_image.width, split_image.height * 3))
split_image.save(args.output_path)