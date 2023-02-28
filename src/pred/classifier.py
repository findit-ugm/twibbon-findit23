from utils.utils import *
from pred.models.tf_pred import *
from typing import Any
import timeit


def tf_run_classifier(image: str, cat: str) -> Any:
    pred_results = []
    for _img in image:
        start_time = timeit.default_timer()
        img = load_image(_img)
        if img is None:
            tmp_pred = {"predicted_label": "",
                        "probability": "", "status_code": 404}
        else:
            tmp_pred = tf_predict_lite(img)
            tmp_pred["status_code"] = 200
        end_time = timeit.default_timer()
        tmp_pred['time_req'] = str(end_time-start_time)
        pred_results.append(tmp_pred)
    
    return pred_results