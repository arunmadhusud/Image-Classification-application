from PIL import Image
from torchvision import transforms
import torch
from fastapi import FastAPI, UploadFile, File
import uvicorn
from contextlib import asynccontextmanager
import torchvision.models as models
    
# Load the ImageNet classes file
with open("imagenet_classes.txt", "r") as f:
    categories = [s.strip() for s in f.readlines()]

# Define the function to return image label
def returnImageLabel(image: Image.Image, model):
    # Preprocess the image
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)

    # Use GPU if available
    if torch.cuda.is_available():
        input_batch = input_batch.to('cuda')
        model.to('cuda')

    with torch.no_grad():
        output = model(input_batch)

    # Apply softmax to get probabilities
    probabilities = torch.nn.functional.softmax(output[0], dim=0)

    # Find the top 5 results
    top5_prob, top5_catid = torch.topk(probabilities, 5)
    result = []
    for i in range(top5_prob.size(0)):
        result.append((categories[top5_catid[i]], top5_prob[i].item()))
    return result

app = FastAPI()


# Load the model on app startup
@app.on_event("startup")
def load_model():
    global model
    model = torch.load('resnet18.pth')
    model.eval()

@app.post("/process")
async def process_image(file: UploadFile = File(...)):
    img = Image.open(file.file)
    result = returnImageLabel(img, model)
    return {"predictions": result}

@app.get("/model-health")
def model_health():
    return {"status": "ok", "service": "model"}

