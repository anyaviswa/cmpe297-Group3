# Dataset Preparation: The yelp_academic_dataset_review.json is taken from https://www.kaggle.com/yelp-dataset/yelp-dataset
# All the other fields except from stars and review was deleted and the data was divided uniformally into training and testing




import json
import ijson

counter = [0, 0, 0, 0, 0, 0]
temp_dict = {}
with open("yelp_academic_dataset_review.json", 'rb') as input_file:
    # load json iteratively
    parser = ijson.parse(input_file, multiple_values=True)
    for prefix, event, value in parser:
        if prefix == "stars":
            # print(value)
            temp_dict["stars"] = str(value)
        if prefix == "text":
            # print(value)
            temp_dict["review"] = str(value)
        if event == "end_map":
            counter[int(temp_dict["stars"].split(".")[0])] = counter[int(temp_dict["stars"].split(".")[0])] + 1
            if counter[int(temp_dict["stars"].split(".")[0])] < 120000:

                json_object = json.dumps(temp_dict, indent=4)

                # Writing to sample.json
                writeable_filename = "training_dataset.json"
                with open(writeable_filename, "a") as outfile:
                    outfile.write(json_object)
                # print(temp_dict)
                temp_dict = {}
            elif counter[int(temp_dict["stars"].split(".")[0])] > 120000 and counter[
                int(temp_dict["stars"].split(".")[0])] < 150000:

                json_object = json.dumps(temp_dict, indent=4)

                # Writing to sample.json
                writeable_filename = "testing_dataset.json"
                with open(writeable_filename, "a") as outfile:
                    outfile.write(json_object)
                # print(temp_dict)
                temp_dict = {}


