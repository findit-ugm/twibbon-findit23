from utils.utils import *
from pred.models.tf_pred import *
from typing import Any



def tf_run_classifier(image: str, cat: str) -> Any:
    pred_results = []
    for _img in image:
        img = load_image(_img)
        if img is None:
            tmp_pred = {"predicted_label": "",
                        "probability": "", "status_code": 404}
        else:
            tmp_pred = tf_predict(img)
            tmp_pred["status_code"] = 200
        pred_results.append(tmp_pred)
    return pred_results