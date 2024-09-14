import requests

# Set up the endpoint and headers
url = "https://vthaxpredictionmodel2.cognitiveservices.azure.com/customvision/v3.0/Prediction/c72b30d5-6946-45de-ad62-0a961cf38006/detect/iterations/Iteration2/image"
headers = {
    "Prediction-Key": "e8c3802bc6a94f83a4299b0b531b99ef",
    "Content-Type": "application/octet-stream"
}

# Open the image file and read the content
image_path = r"C:\Users\gabeg\Documents\GabrielCollege\jaiFridge.jpg"  # Replace with your actual image file path
with open(image_path, "rb") as image_data:
    # Make the request with image file as the body
    response = requests.post(url, headers=headers, data=image_data)

# Check the response
if response.status_code == 200:
    predictions = response.json()
    print(predictions)
else:
    print(f"Error: {response.status_code}, {response.text}")