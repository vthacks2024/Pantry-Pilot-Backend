import requests
import os

# Set up the endpoint and API key
subscription_key = "70634a8b4c274b3987fbfdcaccd871bc"  # Replace with your actual subscription key
endpoint = "https://vthax2024.cognitiveservices.azure.com//"  # Replace with your actual endpoint URL
training_url = endpoint + "/vision/v3.2/analyze"

# Path to the imager"C:\Users\gabeg\Documents\GabrielCollege\fridge2.jpg"
image_path = r"C:\Users\gabeg\Documents\GabrielCollege\fridge2.jpg"  # Update path if necessary


    # Open the image file
with open(image_path, "rb") as image_file:
    image_data = image_file.read()

# Define headers and parameters
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/octet-stream'
}
params = {
    'visualFeatures': 'Objects,Categories,Tags'
}

# Make the request
response = requests.post(training_url, headers=headers, params=params, data=image_data)
response.raise_for_status()  # This will raise an exception for HTTP errors

# Parse and print the results
analysis = response.json()

print("Detected objects:")
for obj in analysis.get("objects", []):
    print(f" - {obj['object']} with confidence {obj['confidence']:.2f}")

print("Detected tags:")
for tag in analysis.get("tags", []):
    print(f" - {tag['name']} with confidence {tag['confidence']:.2f}")







##tag = trainer.create_tag(project_id, tag_name)
## 