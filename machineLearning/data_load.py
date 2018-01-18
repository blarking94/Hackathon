import os
from six.moves.urllib.request import urlopen
import tensorflow as tf
import math

import config
import data_converter

# Data sets
CAR_DATA = "car_training.csv"
CAR_DATA_URL = config.CAR_DATA_URL

def main():
  # If the training and test sets aren't stored locally, download them.
  if not os.path.exists(CAR_DATA):
    raw = urlopen(CAR_DATA_URL).read()
    with open(CAR_DATA, "wb") as f:
      f.write(raw)

  # Split the data sets randomly 70 / 30
  with tf.Session() as sess:
    sess.run( tf.global_variables_initializer())

    features = tf.placeholder(tf.int32, shape=[6], name='features')
    acceptability = tf.placeholder(tf.string, name='acceptability')

    printerop = tf.Print(acceptability, [features], name='printer')

    total_data = []

    y_vals = np.array(["unacc", "acc", "good", "vgood"])


    # Declare batch size
    batch_size = 50

    # Initialize placeholders
    x_data = tf.placeholder(shape=[None, 6], dtype=tf.float32)
    y_target = tf.placeholder(shape=[4, None], dtype=tf.float32)
    prediction_grid = tf.placeholder(shape=[None, 6], dtype=tf.float32)







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

            # Run the Print ob
            total = sess.run(printerop, feed_dict={features: [buying, maint, doors, persons, lug_boot, safety], acceptability:acceptability_value})
            total_data.append(total)
            print(acceptability_value, features)

    # Split Data into training and test
    #training_data_size = math.floor(total_data.size() * 0.7)

    #training_data = total_data[:training_data_size]
    #test_data = total_data[training_data_size:]



main()
