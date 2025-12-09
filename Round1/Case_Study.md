# Case Study

## Problem Statement and Objectives
Accurate road detection in satellite and street-level imagery is essential for autonomous vehicles and urban planning. The objective is to improve segmentation accuracy and generalization using deep learning.

## Data Preprocessing
- Normalize images
- Apply data augmentation (rotation, flipping, brightness/contrast)
- Address class imbalance with oversampling and weighted loss

## Model Selection and Development
- Select U-Net with attention blocks as the main architecture
- Compare with standard U-Net and DeepLab
- Train on Massachusetts Roads Dataset

## Visualizations and Insights
- Segmentation masks for test images
- Accuracy, IoU, and F1-score plots
- Comparative bar charts

## Recommendations
- Use attention mechanisms for improved feature focus
- Apply robust data augmentation for better generalization
- Address class imbalance for higher accuracy
