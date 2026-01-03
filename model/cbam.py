import torch
import torch.nn as nn

class CBAM(nn.Module):
    """
    Convolutional Block Attention Module (CBAM)
    Implemented following the formulation described in the manuscript.
    """

    def __init__(self, channels, reduction=16):
        super().__init__()

        # Channel Attention
        self.channel_attention = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(channels, channels // reduction, kernel_size=1, bias=False),
            nn.ReLU(inplace=True),
            nn.Conv2d(channels // reduction, channels, kernel_size=1, bias=False),
            nn.Sigmoid()
        )

        # Spatial Attention
        self.spatial_attention = nn.Sequential(
            nn.Conv2d(2, 1, kernel_size=7, padding=3, bias=False),
            nn.Sigmoid()
        )

    def forward(self, x):
        # Channel attention
        x = x * self.channel_attention(x)

        # Spatial attention
        avg_out = torch.mean(x, dim=1, keepdim=True)
        max_out, _ = torch.max(x, dim=1, keepdim=True)
        x = x * self.spatial_attention(torch.cat([avg_out, max_out], dim=1))

        return x
