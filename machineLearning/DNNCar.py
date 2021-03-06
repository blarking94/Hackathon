import os
from six.moves.urllib.request import urlopen

import numpy as np
import tensorflow as tf

import data_converter
import config

# Data sets
CAR_DATA = "car_training.csv"
CAR_DATA_URL = config.CAR_DATA_URL

classifier = None

def main():
  # If the training and test sets aren't stored locally, download them.
  if not os.path.exists(CAR_DATA):
    raw = urlopen(CAR_DATA_URL).read()
    with open(CAR_DATA_URL, "wb") as f:
      f.write(raw)

  # Load Data sets
  d_vals = []
  t_vals = []
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

        d_vals.append([buying, maint, doors, persons, lug_boot, safety])
        t_vals.append(acceptability_value)

  # Specify that all features have real-value data
  feature_columns = [tf.feature_column.numeric_column("x", shape=[6])]

  # Build 4 layer DNN with 10, 20, 10 units respectively.
  global classifier
  classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                          hidden_units=[10, 20, 10],
                                          n_classes=4,
                                          label_vocabulary=["unacc","acc","good","vgood"],
                                          model_dir="/tmp/car_model")


  print("PRINTING TRAINING SET")
  print(np.array(d_vals))
  print("PRINTING TRAINING SET TARGET")
  print(np.array(t_vals))

  test_values = []
  train_values= []
  test_keys= []
  train_keys= []
  i= 0
  for x in d_vals:
    y = np.random.randint(low=0, high=100)
    if y > 60:
          test_values.append(x)
          test_keys.append(t_vals[i])
    else:
        train_values.append(x)
        train_keys.append(t_vals[i])

    i = i+1

  print(len(train_values))
  print(len(test_values))

  # Define the training inputs
  train_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": np.array(train_values)},
      y=np.array(train_keys),
      num_epochs=None,
      shuffle=True)


  # Train model.
  classifier.train(input_fn=train_input_fn, steps=2000)

  # Define the test inputs
  test_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": np.array(test_values)},
      y=np.array(test_keys),
      num_epochs=1,
      shuffle=False)

  # Evaluate accuracy.
  accuracy_score = classifier.evaluate(input_fn=test_input_fn)["accuracy"]

  print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

  #Classify two new car samples.
  new_samples = np.array(
    [[1, 2, 3, 1, 2, 1],
     [2, 3, 2, 3, 1, 2]], dtype=np.float32)


  predict_input_fn = tf.estimator.inputs.numpy_input_fn(
  x={"x": new_samples},
  num_epochs=1,
  shuffle=False)

  predictions = list(classifier.predict(input_fn=predict_input_fn))
  predicted_classes = [p["classes"] for p in predictions]

  print(
      "New Samples, Class Predictions:    {}\n"
      .format(predicted_classes))

  classifyNew([1,2,1,3,2,1])

def classifyNew(new_data):
    new_samples = np.array([new_data], dtype=np.float32)
    predict_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"x": new_samples},
    num_epochs=1,
    shuffle=False)

    predictions = list(classifier.predict(input_fn=predict_input_fn))
    predicted_classes = [p["classes"] for p in predictions]

    print(
        "New Samples, Class Predictions:    {}\n"
        .format(predicted_classes))
    return predicted_classes

if __name__ == "__main__":
    main()
