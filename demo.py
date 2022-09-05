# -- coding: utf-8 --`
import argparse
import os
# engine
from stable_diffusion_engine import StableDiffusionEngine
# scheduler
from diffusers import LMSDiscreteScheduler, PNDMScheduler
# utils
import cv2
import numpy as np

# -*- coding: utf-8 -*-
from bottle import route, run, template, response


def main():
    np.random.seed(None)
    scheduler = LMSDiscreteScheduler(
        beta_start=0.00085,
        beta_end=0.012,
        beta_schedule="scaled_linear",
        tensor_format="np"
    )

    engine = StableDiffusionEngine(
        model = "bes-dev/stable-diffusion-v1-4-openvino",
        scheduler = scheduler,
        tokenizer = "openai/clip-vit-large-patch14"
    )
    image = engine(
        prompt = "Concept is vtuber girl, she is red hair, red eyes, wear glasses. she love computer. pixiv",
        init_image = None,
        mask = None,
        strength = 0.5,
        num_inference_steps = 32,
        guidance_scale = 7.5,
        eta = 0.0
    )
    cv2.imwrite("output.png", image)

@route('/output.png')
def sample_image():
    main()

    response.content_type = 'image/png'
    with open('./output.png', 'rb') as fh:
        content = fh.read()
    response.set_header('Content-Length', str(len(content)))
    return content

run(host='localhost', port=8080)