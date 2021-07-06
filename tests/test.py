import torch

from dcn_v2_pytorch import DCNv2


def test():
    m = DCNv2(3, 3, 3)
    m.to('cuda')
    x = torch.ones(1, 3, 10, 20, dtype=torch.float32, device='cuda')
    out = m(x)
    assert out.shape == x.shape
