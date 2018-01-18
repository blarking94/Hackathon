import os
from six.moves.urllib.request import urlopen
import tensorflow as tf
import math
import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import config
import data_converter


# Create graph
sess = tf.Session()

CAR_DATA = "car_training.csv"
CAR_DATA_URL = config.CAR_DATA_URL

# If the training and test sets aren't stored locally, download them.
if not os.path.exists(CAR_DATA):
  raw = urlopen(CAR_DATA_URL).read()
  with open(CAR_DATA, "wb") as f:
    f.write(raw)

# unacc = 1
# acc = 2
# good = 3
# vgood = 4
d_vals = []
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

      d_vals.append([buying, maint, doors, acceptability_value])

x_vals = np.array([[x[0], x[1], x[2], x[3]] for x in d_vals])

y_vals1 = np.array([1 if y[3]==1 else -1 for y in d_vals])
y_vals2 = np.array([1 if y[3]==2 else -1 for y in d_vals])
y_vals3 = np.array([1 if y[3]==3 else -1 for y in d_vals])
y_vals4 = np.array([1 if y[3]==4 else -1 for y in d_vals])


y_vals = np.array([y_vals1, y_vals2, y_vals3, y_vals4])

z_vals = np.array([[x[2]] for x in d_vals])

print("PRINTING Z VALUES")
print(z_vals)

class1_y = []
class1_x = []
class1_z = []
class2_y = []
class2_x = []
class2_z = []
class3_y = []
class3_x = []
class3_z = []
class4_y = []
class4_x = []
class4_z = []

for x in x_vals:

    if x[2] == 1:
        class1_x.append([x[0]])
        class1_y.append([x[1]])
        class1_z.append([x[2]])
    elif x[2] == 2:
        class2_x.append([x[0]])
        class2_y.append([x[1]])
        class2_z.append([x[2]])
    elif x[2] == 3:
        class3_x.append([x[0]])
        class3_y.append([x[1]])
        class3_z.append([x[2]])
    elif x[2] == 4:
        class4_x.append([x[0]])
        class4_y.append([x[1]])
        class4_z.append([x[2]])

    #x.pop()
    #print(x)

x_vals2 = np.delete(x_vals, np.s_[3:], axis=1)

for x in z_vals:
    print(x)

batch_size = 50

# Initialize placeholders
x_data = tf.placeholder(shape=[None, 3], dtype=tf.float32)
z_data = tf.placeholder(shape=[None, 3], dtype=tf.float32)
y_target = tf.placeholder(shape=[4, None], dtype=tf.float32)
prediction_grid = tf.placeholder(shape=[None, 3], dtype=tf.float32)

# Create variables for svm
b = tf.Variable(tf.random_normal(shape=[4,batch_size]))

# Gaussian (RBF) kernel
gamma = tf.constant(-10.0)
dist = tf.reduce_sum(tf.square(x_data), 1)
dist = tf.reshape(dist, [-1,1])
sq_dists = tf.multiply(2., tf.matmul(x_data, tf.transpose(x_data)))
my_kernel = tf.exp(tf.multiply(gamma, tf.abs(sq_dists)))

# Declare function to do reshape/batch multiplication
def reshape_matmul(mat):
    v1 = tf.expand_dims(mat, 1)
    v2 = tf.reshape(v1, [4, batch_size, 1])
    return(tf.matmul(v2, v1))

# Compute SVM Model
first_term = tf.reduce_sum(b)
b_vec_cross = tf.matmul(tf.transpose(b), b)
y_target_cross = reshape_matmul(y_target)

second_term = tf.reduce_sum(tf.multiply(my_kernel, tf.multiply(b_vec_cross, y_target_cross)),[1,2])
loss = tf.reduce_sum(tf.negative(tf.subtract(first_term, second_term)))

# Gaussian (RBF) prediction kernel
rA = tf.reshape(tf.reduce_sum(tf.square(x_data), 1),[-1,1])
rB = tf.reshape(tf.reduce_sum(tf.square(prediction_grid), 1),[-1,1])
pred_sq_dist = tf.add(tf.subtract(rA, tf.multiply(2., tf.matmul(x_data, tf.transpose(prediction_grid)))), tf.transpose(rB))
pred_kernel = tf.exp(tf.multiply(gamma, tf.abs(pred_sq_dist)))

prediction_output = tf.matmul(tf.multiply(y_target,b), pred_kernel)
prediction = tf.arg_max(prediction_output-tf.expand_dims(tf.reduce_mean(prediction_output,1), 1), 0)
accuracy = tf.reduce_mean(tf.cast(tf.equal(prediction, tf.argmax(y_target,0)), tf.float32))

# Declare optimizer
my_opt = tf.train.GradientDescentOptimizer(0.01)
train_step = my_opt.minimize(loss)

# Initialize variables
init = tf.global_variables_initializer()
sess.run(init)

# Training loop
loss_vec = []
batch_accuracy = []
for i in range(100):
    rand_index = np.random.choice(len(x_vals2), size=batch_size)

    rand_x = x_vals2[rand_index]
    rand_y = y_vals[:,rand_index]
    rand_z = x_vals2[rand_index]

    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y, z_data: rand_z})

    temp_loss = sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y, z_data: rand_z})
    loss_vec.append(temp_loss)

    acc_temp = sess.run(accuracy, feed_dict={x_data: rand_x,
                                             y_target: rand_y,
                                             z_data: rand_z,
                                             prediction_grid:rand_x})
    batch_accuracy.append(acc_temp)

    if (i+1)%25==0:
        print('Step #' + str(i+1))
        print('Loss = ' + str(temp_loss))

# Create a mesh to plot points in
x_min, x_max = x_vals2[:, 0].min() - 1, x_vals2[:, 0].max() + 1
y_min, y_max = x_vals2[:, 1].min() - 1, x_vals2[:, 1].max() + 1
z_min, z_max = x_vals2[:, 2].min() - 1, x_vals2[:, 2].max() + 1

xx, yy, zz = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02),
                     np.arange(z_min, z_max, 0.02))
grid_points = np.c_[xx.ravel(), yy.ravel(), zz.ravel()]
grid_predictions = sess.run(prediction, feed_dict={x_data: rand_x,
                                                   y_target: rand_y,
                                                   z_data: rand_z,
                                                   prediction_grid: grid_points})
grid_predictions = grid_predictions.reshape(xx.shape)

# Plot points and grid

fig = plt.figure(figsize=(8, 8))
ax = fig.gca(projection='3d')

n = len(x_vals2)

xs = []
yz = []
zs = []
for x in x_values:
    xs.append(x[0])
    yz.append(x[1])
    zs.append(x[2])

ax.scatter(xs, yz, zs, c=c, marker=m)

ax.set_xlim3d(0, 4)
ax.set_ylim3d(0, 4)
ax.set_zlim3d(0, 4)

#plt.contourf(xx, yy, grid_predictions, cmap=plt.cm.Paired, alpha=0.8)
#plt.plot(class1_x, class1_y, 'ro', label='unacc')
#plt.plot(class2_x, class2_y, 'kx', label='acc')
#plt.plot(class3_x, class3_y, 'gv', label='good')
#plt.plot(class4_x, class4_y, 'gx', label='vgood')
#plt.title('Gaussian SVM Results on Car Data')
#plt.xlabel('Buying')
#plt.ylabel('MainT')
#plt.legend(loc='lower right')
#plt.ylim([0, 4])
#plt.xlim([0, 4])
plt.show()

# Plot batch accuracy
plt.plot(batch_accuracy, 'k-', label='Accuracy')
plt.title('Batch Accuracy')
plt.xlabel('Generation')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()

# Plot loss over time
plt.plot(loss_vec, 'k-')
plt.title('Loss per Generation')
plt.xlabel('Generation')
plt.ylabel('Loss')
plt.show()
