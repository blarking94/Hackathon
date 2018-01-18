import os
from six.moves.urllib.request import urlopen

import config

# Data sets
CAR_DATA = "car_training.csv"
CAR_DATA_URL = config.CAR_DATA_URL

#  70/30 split training and test data
CAR_TRAINING_DATA

CAR_TEST_DATA


def main():
  # If the training and test sets aren't stored locally, download them.
  if not os.path.exists(CAR_DATA):
    raw = urlopen(CAR_DATA_URL).read()
    with open(CAR_DATA, "wb") as f:
      f.write(raw)

  # Split the data sets randomly 70 / 30
  


main()
