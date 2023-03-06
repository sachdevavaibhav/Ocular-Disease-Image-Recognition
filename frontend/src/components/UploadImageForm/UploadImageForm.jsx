import { useState } from "react";
import axios from 'axios'
import {toast} from 'react-toastify';

const diseaseMap = {
    "A": "Age Related Macular Degeneration",
    "C": "Cataract",
    "D": "Diabetic Retinopathy",
    "G": "Glaucauma",
    "H": "Hypertension Macular Degeneration",
    "M": "Myopia",
    "N": "Normal",
    "O": "Other"
}

function UploadImageForm() {
    const [selectedFile, setSelectedFile] = useState(null);
    const [prediction, setPrediction] = useState([])

    function handleFileInputChange(event) {
        setSelectedFile(event.target.files[0]);
        toast(`Click the upload button to upload ${event.target.files[0].name}`, {
            position: "bottom-right",
            autoClose: 5000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined,
            theme: "light",
            })
      }
    
      async function handleSubmit(event) {
        event.preventDefault();
        const formData = new FormData();
        formData.append('file', selectedFile);

        try {
            await toast.promise(axios.post(`${process.env.REACT_APP_BACKEND_API}/upload`, formData, {
                headers: {
                'Content-Type': 'multipart/form-data'
                }
            }), {pending: 'Uploading Image', success: 'Image uploaded successfully', error: 'Got unexpected error. Please try again.'});
        } catch(error) {
            console.error('Error uploading image:', error);
        }
      }

      async function handlePredict() {
        try {
            const response = await toast.promise(axios.get(`${process.env.REACT_APP_BACKEND_API}/predict/${selectedFile.name}`),
            {pending: 'Predecting disease', success: 'Got prediction results', error: 'Got unexpected error. Please try again.'})
            const response_data = Object.entries(response.data.prediction)

            let diseases = []
            for (let pred of response_data) {
                if (pred[1]) {
                    diseases.push(diseaseMap[pred[0]])
                }
            }
            if (diseases.length === 0) {
                diseases = null
            }
            setPrediction(diseases)
        } catch(error) {
            setPrediction([])
            console.error("Error predicting", error)
        }
        setSelectedFile(null)
      }


    return(
        <div className="container">
            <h1>Upload Fundus Image</h1>
            <div className="card">
                <form onSubmit={handleSubmit} encType="multipart/form-data">
                    <div className="form-group">
                        <label htmlFor="file" className="upload-label"><span>Choose an image</span></label>
                        <input type="file" id="file" name="file" accept="image/*" onChange={handleFileInputChange} />
                    </div>
                    <div className="buttons">
                        <button className="btn" type="submit" disabled={!selectedFile}>Upload</button>
                        <button className="btn btn-predict" type="button" onClick={handlePredict} disabled={!selectedFile}>Predict</button>
                    </div>
                </form>
                <div className="prediction">
                    {prediction===null?<p>Sorry, the system could not predict the disease.</p>
                    :prediction.map((pred, index) => {
                        if (pred ==='Normal') {
                            return(<p key={index}>The system thinks your eye is Normal.</p>)
                        }
                        else if (pred === 'Other') {
                            return (<p key={index}>The image uploaded is out of the scope of this system.</p>)
                        }
                        else {
                            return(
                                <div key={index}>
                                    <p>The system thinks your eye has:</p>
                                    <li>{pred}</li>
                                </div>
                            )
                        }
                    })}                   
                </div>
            </div>
        </div>
    )
}

export default UploadImageForm