"""
Generate synthetic data for road segmentation (demo purposes)
Creates simple images with white lines (roads) on black backgrounds.
"""
import numpy as np
import matplotlib.pyplot as plt

def generate_synthetic_data(num_samples=100, img_size=128):
    X = np.zeros((num_samples, img_size, img_size, 3), dtype=np.uint8)
    y = np.zeros((num_samples, img_size, img_size, 1), dtype=np.uint8)
    for i in range(num_samples):
        img = np.zeros((img_size, img_size, 3), dtype=np.uint8)
        mask = np.zeros((img_size, img_size, 1), dtype=np.uint8)
        # Draw a random line (road)
        x1, y1 = np.random.randint(0, img_size//2, size=2)
        x2, y2 = np.random.randint(img_size//2, img_size, size=2)
        rr, cc = np.linspace(x1, x2, img_size).astype(int), np.linspace(y1, y2, img_size).astype(int)
        img[rr, cc] = [255, 255, 255]
        mask[rr, cc, 0] = 1
        X[i] = img
        y[i] = mask
    return X, y

if __name__ == "__main__":
    X, y = generate_synthetic_data(10, 128)
    # Show sample
    for i in range(3):
        plt.subplot(2,3,i+1)
        plt.imshow(X[i])
        plt.title('Image')
        plt.axis('off')
        plt.subplot(2,3,i+4)
        plt.imshow(y[i].squeeze(), cmap='gray')
        plt.title('Mask')
        plt.axis('off')
    plt.tight_layout()
    plt.show()
