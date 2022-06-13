import os
import csv

datasets = {
    "categories": "categories.csv",
    "canada": "CAvideos.csv",
    "uk": "GBvideos.csv",
    "us": "USvideos.csv",
}


# Reads first six rows of csv formatted dataset
def read_csv(dataset_address: str) -> None:
    with open(dataset_address) as file:
        reader = csv.reader(file)
        count = 0
        for row in reader:
            print(row)
            if count > 5:
                break
            count += 1
    return


# Launch...
if __name__ == "__main__":
    # moves to the datasets folder
    os.chdir("../")
    os.chdir("datasets")
    read_csv(datasets["categories"])
else:
    pass
