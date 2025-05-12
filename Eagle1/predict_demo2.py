import os
import torch
import numpy as np
import csv
import typing_extensions as typing
from eagle import conversation as conversation_lib
from eagle.constants import DEFAULT_IMAGE_TOKEN
from eagle.constants import IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN, DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN
from eagle.conversation import conv_templates
from eagle.model.builder import load_pretrained_model
from eagle.utils import disable_torch_init
from eagle.mm_utils import tokenizer_image_token, get_model_name_from_path, process_images
from PIL import Image
from transformers import TextIteratorStreamer
from threading import Thread
from loguru import logger


def process_image(image_path,prompt_type):
    model_path = "NVEagle/Eagle-X5-13B-Chat"
    conv_mode = "vicuna_v1"
    image = Image.open(image_path).convert('RGB')
    model_name = get_model_name_from_path(model_path)
    tokenizer, model, image_processor, context_len = load_pretrained_model(model_path, 
                                                                        None, 
                                                                        model_name, 
                                                                        False, 
                                                                        False)

    if model.config.mm_use_im_start_end:
        input_prompt = DEFAULT_IM_START_TOKEN + DEFAULT_IMAGE_TOKEN + DEFAULT_IM_END_TOKEN + '\n' + prompt_type
    else:
        input_prompt = DEFAULT_IMAGE_TOKEN + '\n' + prompt_type

    conv = conv_templates[conv_mode].copy()
    conv.append_message(conv.roles[0], input_prompt)
    conv.append_message(conv.roles[1], None)
    prompt = conv.get_prompt()
    image_tensor = process_images([image], image_processor, model.config)[0]
    input_ids = tokenizer_image_token(prompt, tokenizer, IMAGE_TOKEN_INDEX, return_tensors='pt')

    input_ids = input_ids.to(device='cuda', non_blocking=True)
    image_tensor = image_tensor.to(dtype=torch.float16, device='cuda', non_blocking=True)

    with torch.inference_mode():
        output_ids = model.generate(
            input_ids.unsqueeze(0),
            images=image_tensor.unsqueeze(0),
            image_sizes=[image.size],
            do_sample=True,
            temperature=0.2,
            top_p=0.5,
            num_beams=1,
            max_new_tokens=256,
            use_cache=True)

    outputs = tokenizer.batch_decode(output_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True)[0].strip()
    return outputs

# Process all images in the folder
def eagle_csv_generator(folder_path,output_csv,prompt,face_feature_list):
    # data = []
    # temp=0
    # for filename in os.listdir(folder_path):
    #     if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
    #         image_path = os.path.join(folder_path, filename)
    #         description = process_image(image_path,prompt)
    #         # logger.debug(description)
    #         description = str(description)
    #         description_list =  description.split(";")
    #         logger.debug(description_list)
    #         # for i in range(len(description_list)):
    #         #     logger.error(str(description_list[i]))
    #         list(map(str,description_list))
    #         # for i in range(len(description_list)):
    #         #     logger.info((str(description_list[i])).split(":")[1])
    #         facial_dict = {"image_path": image_path}
    #         for feature,descr in zip(face_feature_list,description_list):
    #             facial_dict[feature]=descr.split(":")[1]
    #         data.append(facial_dict)
    #         print(f"Processed {image_path}")
    #         temp=temp+1
    #         logger.debug(temp)
    # logger.info(data)
    # with open(output_csv, mode='w', newline='') as file:
    #     face_feature_list.insert(0,"image_path")
    #     writer = csv.DictWriter(file, fieldnames=face_feature_list)
    #     writer.writeheader()
    #     writer.writerows(data)

    face_feature_list_with_path = ["image_path"] + face_feature_list  # Ensure image_path is first

    with open(output_csv, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=face_feature_list_with_path)
        writer.writeheader()

        for count, filename in enumerate(os.listdir(folder_path), start=1):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(folder_path, filename)
                try:
                    description = process_image(image_path, prompt)
                    description_list = str(description).split(";")
                    logger.debug(description_list)

                    facial_dict = {"image_path": image_path}
                    for feature, descr in zip(face_feature_list, description_list):
                        key_value = descr.split(":")
                        if len(key_value) == 2:
                            facial_dict[feature] = key_value[1].strip()
                        else:
                            facial_dict[feature] = ""

                    writer.writerow(facial_dict)
                    print(f"Processed and saved {image_path}")
                    logger.debug(f"Processed count: {count}")

                except Exception as e:
                    logger.error(f"Failed to process {image_path}: {e}")

    print(f"Descriptions saved to {output_csv}")
