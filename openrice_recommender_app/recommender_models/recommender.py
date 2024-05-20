import os
from functools import lru_cache

import keras
import numpy as np
import pandas as pd
import tensorflow as tf

absolute_path = os.path.dirname(__file__)
restaurant_id_to_link = pd.read_csv(
    os.path.join(absolute_path, "./restaurant_id_to_link.csv")
)
restaurant_id_to_link = restaurant_id_to_link.set_index("restaurantId")[
    "restaurantShortedUrl"
].to_dict()
test_df = pd.read_csv(os.path.join(absolute_path, "./test_df.csv"))
train_df = pd.read_csv(os.path.join(absolute_path, "./train_df.csv"))
full_restaurant_ids = list(set(train_df.restaurantId))

model = keras.models.load_model(os.path.join(absolute_path, "./model.h5"))

if not model:
    raise Exception("model could not be loaded")

predicted_rating_threshold = 4.0


@lru_cache(maxsize=128)
def recommend(picked_userid, *, blacklist=None, randomized=False):
    blacklist = blacklist or []

    candidate_restaurant_ids = full_restaurant_ids
    if blacklist:
        candidate_restaurant_ids = [
            v for v in candidate_restaurant_ids if v not in blacklist
        ]

    item_data = np.array(candidate_restaurant_ids)
    user = np.array([picked_userid for i in range(len(item_data))])

    predictions = model.predict([user, item_data])

    # predictions[0] -> item_data[0], predictions[1] -> item_data[1], ...
    predictions = np.array([v[0] for v in predictions])

    sorted_predictions = (-predictions).argsort()

    sorted_predictions_up_to_index = 0
    for i, v in enumerate(sorted_predictions):
        if float(predictions[v]) < predicted_rating_threshold:
            sorted_predictions_up_to_index = i
            break
    sorted_predictions = sorted_predictions[:sorted_predictions_up_to_index]

    if randomized:
        np.random.shuffle(sorted_predictions)

    item_index = sorted_predictions
    item_ids = [item_data[v] for v in item_index]

    return tuple(
        (
            predictions[sorted_predictions[i]],
            restaurant_id_to_link[item_ids[i]],
            item_ids[i],
        )
        for i in range(len(item_ids))
    )
