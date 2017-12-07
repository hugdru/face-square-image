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

import cv2 as cv


def process(image_path, padding):
    face_cascade = cv.CascadeClassifier(
        "training_data/haarcascade_frontalface_default.xml")

    img = cv.imread(image_path)
    img_height, img_width, _ = img.shape

    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)

    if len(faces) != 1:
        raise Exception("not_one_face:{}".format(image_path))

    (x, y, w, h) = faces[0]

    square_size = max(w, h)
    padding_factor = padding / 100
    if padding_factor < 0:
        raise Exception("negative_padding:{}".format(image_path))
    padding = int(square_size * padding_factor)

    w_side_delta_to_square = int((square_size - w) / 2)
    h_side_delta_to_square = int((square_size - h) / 2)

    top_left_x = max(0, x - w_side_delta_to_square - padding)
    top_left_y = max(0, y - h_side_delta_to_square - padding)

    bottom_right_x = min(img_width,
                         x + square_size + w_side_delta_to_square + padding)
    bottom_right_y = min(img_height,
                         y + square_size + h_side_delta_to_square + padding)

    return img[top_left_y:bottom_right_y, top_left_x:bottom_right_x]


def write(image, destination):
    cv.imwrite(destination, image)


def show(image):
    cv.imshow("Face", image)
