import argparse

parse = argparse.ArgumentParser()

parse.add_argument('--is_show', action='store_true', default=True, help='initial weights path')
parse.add_argument('--is_save_img', action='store_true', default=True, help='initial weights path')
parse.add_argument('--save_period', type=float, default=0.01, help='initial weights path')
parse.add_argument('--output_dir', type=str, default='./label_data', help='initial weights path')
parse.add_argument('--img_size', type=tuple, default=(1280,720), help='initial weights path')
parse.add_argument('--thres', type=float,default=0.5, help='')

args = parse.parse_args()