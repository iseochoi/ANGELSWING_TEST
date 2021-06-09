import argparse
import io

import torch
from PIL import Image
from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/predict', methods=["POST"])
def predict():
    if not request.method == "POST":
        return

    data_img = json.loads(request.get_data())
    im_path = data_img["image_path"]
    with open(im_path, "rb") as file:
        img_bytes = file.read()

    img = Image.open(io.BytesIO(img_bytes))

    results = model(img, size=640)  # reduce size=320 for faster inference
    if len(results.pandas().xyxy[0]) !=0 :
        output_json = json.dumps({'prediction': [
                                {
                                "label": str(results.pandas().xyxy[0]["name"][0]),
                                "confidence": str(float(results.pandas().xyxy[0]["confidence"][0])),
                                "bbox" : str(results.pandas().xyxy[0].iloc[0,:4].values.tolist())
                                }
                                ]
                                })
        return Response(response=output_json, status=200, mimetype="application/json")
    else:
        return "The machine can't detect anything in this picture"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask API exposing YOLOv5 model")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    parser.add_argument("--weight", default='./model/best.pt', type=str, help="pretrained model path")
    args = parser.parse_args()

    model = torch.hub.load('ultralytics/yolov5', 'custom', path=args.weight)
    app.run(host="0.0.0.0", port=args.port)  # debug=True causes Restarting with stat
