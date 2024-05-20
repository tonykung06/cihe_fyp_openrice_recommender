if __name__ != "__main__":
    print("Please run this main program directly")
    exit(1)

import recommender_models.recommender

picked_userid = 1644
print(recommender_models.recommender.recommend(picked_userid))
