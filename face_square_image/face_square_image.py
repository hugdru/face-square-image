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

import os
import sys
import command_line as cml
import image as im


def main():
    arguments = cml.parse()

    if not arguments.inplace:
        os.makedirs(arguments.output_dir, exist_ok=True)

    for image_path in arguments.images_paths:
        try:
            cropped_image = im.process(image_path, arguments.padding)
            if arguments.inplace:
                im.write(cropped_image, image_path)
            else:
                im.write(cropped_image,
                         os.path.join(arguments.output_dir,
                                      os.path.basename(image_path)))
        except Exception as e:
            print(e, file=sys.stderr)


if __name__ == "__main__":
    main()
