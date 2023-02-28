from fastapi import FastAPI, HTTPException
from pred.classifier import *
from schemas.img_schemas import Img

app = FastAPI(title="Twibbon Checker API")



@app.post("/v1/predict/tf/", status_code=200)
async def predict_tf(request: Img):
    prediction = tf_run_classifier(request.img_url, request.category)
    if not prediction:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail="Image could not be downloaded"

        )

    return prediction