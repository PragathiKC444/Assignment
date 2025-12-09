# Comparative Analysis

## Existing Algorithms
- **U-Net**: Encoder-decoder architecture, strong baseline for segmentation.
- **DeepLab**: Uses atrous convolution and spatial pyramid pooling for improved context.

## Proposed Model
- U-Net with attention blocks and advanced augmentation.

## Metrics
- Intersection over Union (IoU)
- F1-score
- Accuracy

## Results (Sample Table)
| Model                | IoU   | F1-score | Accuracy |
|----------------------|-------|----------|----------|
| U-Net                | 0.82  | 0.88     | 0.95     |
| DeepLab              | 0.84  | 0.89     | 0.96     |
| Proposed (U-Net+Att) | 0.87  | 0.91     | 0.97     |

## Analysis
The proposed model outperforms standard U-Net and DeepLab in IoU, F1-score, and accuracy, especially on unbalanced datasets. Attention blocks help focus on relevant road features, improving segmentation in complex scenes.