# Deformable Convolution v2 PyTorch Layer for old networks like CenterNet v1
Old repositories (1 year-old+) like [CenterNet](https://github.com/xingyizhou/CenterNet) 
are using PyTorch < 1.0.0, so DCN extension could not be built because of API change.

This repo contains useful replacement of DCN extension with `torchvision` function.

So you can install this module and replace such code:
```
from .DCNv2.dcn_v2 import DCN
```
to:
```
from dcn_v2_pytorch import DCNv2 as DCN
```
and models will work without diving in problems of extension compilation.

## Installation
```
pip install git+https://github.com/lobanov-m/dcn-v2-pytroch.git
```
Repository requires `pytorch >= 1.8.1` and `torchvision >= 0.9.0` 
(in this version torchvision started to support modulated deformable convolutions).