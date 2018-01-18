import os
from six.moves.urllib.request import urlopen
import tensorflow as tf

import config

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
    #total = tf.reduce_sum(features, name='total')

    printerop = tf.Print(acceptability, [features], name='printer')

    with open(CAR_DATA) as inf:
        for line in inf:
            # Read data, using python, into our features
            print(line)
            buying, maint, doors, persons, lug_boot, safety, acceptability = line.strip().split(",")

            buying = str(buying)
            maint = str(maint)
            doors = str(doors)
            persons = str(persons)
            lug_boot = str(lug_boot)
            safety = str(safety)

            # Run the Print ob
            print("read in data")
            total = sess.run(printerop, feed_dict={features: [buying, maint, doors, persons, lug_boot, safety], acceptability:acceptability})
            print(acceptability, total)


main()
