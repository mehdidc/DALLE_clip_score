# DALLE_clip_score

Simple script to compute CLIP scores based on a trained DALL-e model, using OpenAI's CLIP <https://github.com/openai/CLIP>.
CLIP scores measures the compatibility between an image and a caption. The raw value is using cosine similarity, so it is 
between -1 and 1. In CLIP, the value is scaled by 100 by default, giving a number between -100 and 100, where 100 means
maximum compatibility between an image and text. Typical values are around 20-30.

## How to install ?

1. Install CLIP from <https://github.com/openai/CLIP>
2. Install DALL-E lucidrains implementation <https://github.com/lucidrains/DALLE-pytorch> 
3. `python setup.py install`

## How to use ?


Here is an example:

`clip_score --dalle_path dalle.pt --image_text_folder CUB_200_2011 --taming --num_generate 8 --dump`

here:

- `dalle_path` is the path of the model trained with DALL-E using <https://github.com/lucidrains/DALLE-pytorch> 
- `image_text_folder` is the folder of the dataset following <https://github.com/lucidrains/DALLE-pytorch/loader.py>  format
- `taming`: specify that we use taming transformers as an image encoder
- `num_generate`: number of images to generate per caption
- `dump`: save all the generated images in the folder `outputs` (by default) and their respective metrics

Example output:

```
CLIP_score_real 28.47281265258789
CLIP_score 26.4765625
CLIP_score_top1 29.54296875
CLIP_score_relative 0.9353748559951782
CLIP_score_relative_top1 1.043790578842163
CLIP_atleast 0.9900000095367432
```

Note that all the metrics will also be saved on `clip_score.json`.
_
- `CLIP_score_real`: average CLIP score for real images
- `CLIP_score`: average CLIP score for all generated images.
- `CLIP_score_top1`: for each caption, retain the generated image with best CLIP score, then compute the average CLIP score like in `CLIP_score`.
- `CLIP_score_relative`: similar to <https://arxiv.org/abs/2104.14806>, we compute CLIP score of the generated image divided by the CLIP score of the real image, then average. In general, between 0 and 1, although it can be bigger than 1. Bigger than 1 means the CLIP score is higher 
- `CLIP_score_relative_top1`: same as `CLIP_score_relative` but using the top CLIP score like in `CLIP_score_top1`.
- `CLIP_atleast`: for each caption, it is 1 if CLIP score can reach at least `--clip_thresh` (by default **25**), 0 if not, then we average over all captions. This score gives a number between 0 and 1.

For all scores, the higher, the better.
