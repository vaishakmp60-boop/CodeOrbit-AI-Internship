import torch
from torchvision import models
from PIL import Image
import os

# Pretrained Model Explanation:
# Uses MobileNetV2 pretrained on ImageNet (over 1.4 million images)
# to extract visual features and classify the input image.

def classify():
    image_path = os.path.join(os.path.dirname(__file__), "test_image.jpg")

    
    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found.")
        return

    print("Loading pretrained PyTorch MobileNetV2...")
    weights = models.MobileNet_V2_Weights.DEFAULT
    model = models.mobilenet_v2(weights=weights)
    model.eval()

    preprocess = weights.transforms()
    img = Image.open(image_path).convert("RGB")
    batch = preprocess(img).unsqueeze(0)

    print("Classifying image...")
    with torch.no_grad():
        prediction = model(batch).squeeze(0).softmax(0)

    top3_prob, top3_catid = torch.topk(prediction, 3)
    categories = weights.meta["categories"]

    print("\n--- PREDICTION RESULTS ---")
    for i in range(top3_prob.size(0)):
        label = categories[top3_catid[i]]
        score = top3_prob[i].item() * 100
        print(f"{label.capitalize()}: {score:.2f}% confidence")
    print("--------------------------\n")

if __name__ == "__main__":
    classify()