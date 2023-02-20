from flask import Flask, jsonify, request
import tensorflow as tf
import tensorflow_addons as tfa
import numpy as np
import os
import cv2

app = Flask(__name__)

model = tf.keras.models.load_model("./model/model_2_v4.h5")

def crop_image(filename):
    im=cv2.imread(filename)
    # Convert the image to grayscale
    g_Im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

    # Convert the PIL image to a numpy array
    g_Im_np = np.array(g_Im) #gray
    c_Im_np = np.array(im) #RGB

    # Find the non-zero regions of the image
    non_zero_indices = cv2.findNonZero(g_Im_np)

    # Get the bounding box coordinates
    x, y, w, h = cv2.boundingRect(non_zero_indices)

    # Crop the image using the bounding box coordinates
    cropped_image_np = cv2.getRectSubPix(c_Im_np, (w,h), (x+w//2,y+h//2))

    # Convert the numpy array back to a PIL image
    # c_Im = Image.fromarray(cropped_image_np)
    
    return cropped_image_np

@app.route('/predict/<string:filename>')
def predict(filename):
    image = crop_image(f'./images/{filename}')
    image = tf.image.resize(image, [250, 250])
    image = tf.keras.applications.inception_resnet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    print(prediction)
    prediction = prediction[0].round().astype(int).tolist()
    pred_map = {
        "N":prediction[0],
        "D":prediction[1],
        "G":prediction[2],
        "C":prediction[3],
        "A":prediction[4],
        "H":prediction[5],
        "M":prediction[6],
        "O":prediction[7],
    }
    os.remove(f'./images/{filename}')
    print(f'The file {filename} has been deleted.')
    return jsonify({"prediction": pred_map})

@app.route('/upload', methods=["POST"])
def upload_image():
    image = request.files['file']
    print(image)
    if image:
        image_name = image.filename
        image.save(os.path.join("images", image_name))
        return jsonify({"message": "File saved successfully.", "status": 200})
    else:
        return jsonify({"message": "No file found. Please upload a file", "status":400})


if __name__ == "__main__":
    app.run(debug=True, port=8000)