from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from six.moves.urllib.request import urlopen

import numpy as np
import tensorflow as tf

import data_converter
import config

# Data sets
CAR_DATA = "car_training.csv"
CAR_DATA_URL = config.CAR_DATA_URL

def main():
  # If the training and test sets aren't stored locally, download them.
  if not os.path.exists(CAR_DATA):
    raw = urlopen(IRIS_TRAINING_URL).read()
    with open(CAR_DATA_URL, "wb") as f:
      f.write(raw)

  # Load Data sets
  d_vals = []
  t_vlas = []
  with open(CAR_DATA) as inf:
      for line in inf:
        # Read data, using python, into our features
        buying, maint, doors, persons, lug_boot, safety, acceptability_value = line.strip().split(",")

        buying = int(data_converter.convert_buying(buying))
        maint = int(data_converter.convert_maint(maint))
        doors = int(data_converter.convert_doors(doors))
        persons = int(data_converter.convert_persons(persons))
        lug_boot = int(data_converter.convert_lug_boot(lug_boot))
        safety = int(data_converter.convert_safety(safety))
        acceptability_value = int(data_converter.convert_acceptability(acceptability_value))

        d_vals.append([buying, maint, doors, persons, lug_boot, safety])
        t_vlas.append([acceptability_value])

  # Specify that all features have real-value data
  feature_columns = [tf.feature_column.numeric_column("x", shape=[6])]

  # Build 3 layer DNN with 10, 20, 10 units respectively.
  classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                          hidden_units=[10, 20, 10],
                                          n_classes=4,
                                          model_dir="/tmp/car_model")

  # Define the training inputs
  train_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": tf.stack(d_vals[:1500])},
      y=tf.stack(t_vlas[:1500]),
      num_epochs=None,
      shuffle=True)

  # Train model.
  classifier.train(input_fn=train_input_fn, steps=2000)

  # Define the test inputs
  test_input_fn = tf.estimator.inputs.numpy_input_fn(
     x={"x": tf.stack(d_vals[1500:])},
     y=tf.stack(t_vlas[1500:]),
      num_epochs=1,
      shuffle=False)

  # Evaluate accuracy.
  accuracy_score = classifier.evaluate(input_fn=test_input_fn)["accuracy"]

  print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

  # Classify two new flower samples.
  #new_samples = np.array(
#      [[6.4, 3.2, 4.5, 1.5],
       #[5.8, 3.1, 5.0, 1.7]], dtype=np.float32)
  #predict_input_fn = tf.estimator.inputs.numpy_input_fn(
      #x={"x": new_samples},
      #num_epochs=1,
      #shuffle=False)

  #predictions = list(classifier.predict(input_fn=predict_input_fn))
  #predicted_classes = [p["classes"] for p in predictions]

  #print(
      #"New Samples, Class Predictions:    {}\n"
      #.format(predicted_classes))

if __name__ == "__main__":
    main()
