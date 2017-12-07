# Copyright 2017 Hugo Drumond

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse


class Arguments:
    def __init__(self, images_paths, inplace, output_dir, padding):
        self.images_paths = images_paths
        self.inplace = inplace
        self.output_dir = output_dir
        self.padding = padding


def parse():
    parser = argparse.ArgumentParser(
        description='A program to crop a human face to a square',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
        '-s',
        '--sources',
        required=True,
        metavar='image_path',
        type=str,
        dest='images_paths',
        nargs='+',
        help='The images for processing')

    output_group = parser.add_mutually_exclusive_group(required=True)

    output_group.add_argument(
        '-i',
        '--inplace',
        dest='inplace',
        action='store_true',
        help='The path to the html file that represents the index of the book'
        'in relation to the main page url')

    output_group.add_argument(
        '-o',
        '--output',
        metavar='output_dir',
        type=str,
        dest='output_dir',
        help='The directory to place the resulting images')

    parser.add_argument(
        '-p',
        '--padding',
        default=50,
        metavar='padding_percentage',
        type=str,
        dest='padding',
        help='The padding for the cropped square face image')

    args = parser.parse_args()

    return Arguments(
        images_paths=args.images_paths,
        inplace=args.inplace,
        output_dir=args.output_dir,
        padding=args.padding)
