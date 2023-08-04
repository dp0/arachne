A model is not provided as part of this repository, you will need to download
one and put it in this directory.

The model must be a quantized (OnnxStream) compatible model. An example of this
can be found at
[github:vitoplantamura/OnnxStream](https://github.com/vitoplantamura/OnnxStream/releases/tag/v0.1).

This directory should have a structure similar to that shown below when
populated:
```
model/
├── README.md
├── text_encoder_fp32/
├── tokenizer/
├── unet_fp16/
├── vae_decoder_fp16/
└── vae_decoder_qu8/
```
