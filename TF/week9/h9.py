# Import necessary libraries
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# Load MNIST data from the `.npz` file
mnist_data = np.load('TF\week9\mnist\mnist.npz')  # Update the path if necessary

# Extract training and test data
train_Data, train_Label = mnist_data['x_train'], mnist_data['y_train']
test_Data, test_Label = mnist_data['x_test'], mnist_data['y_test']

# Display dataset dimensions
print('Train data:', len(train_Data))
print('Test data:', len(test_Data))
print('Train data dim:', train_Data.shape)
print('Train label dim:', train_Label.shape)

# Function to plot images
def plot_image(data):
    fig = plt.gcf()  # Get current figure
    fig.set_size_inches(4, 4)  # Set display size
    plt.imshow(data, cmap='binary')  # Show image in binary color
    plt.savefig("TF/week9/img.png")
    plt.show()

# Display sample image
plot_image(train_Data[0])
print('Label:', train_Label[0])

# Set learning parameters
learning_rate = 0.01
training_epoch = 1000
batch_size = 2000

# Preprocess data: normalize to range 0-1
train_Data_R = train_Data.reshape(-1, 784).astype('float32') / 255
test_Data_R = test_Data.reshape(-1, 784).astype('float32') / 255

# Create TensorFlow datasets
train_Data_M = tf.data.Dataset.from_tensor_slices((train_Data_R, train_Label))
train_Data_M = train_Data_M.shuffle(5000).batch(batch_size)

# Build model with Dense layers and softmax activation for output
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Define optimizer
optimizer = tf.keras.optimizers.SGD(learning_rate)

# Loss function: cross-entropy loss
def cross_entropy_loss(y, y_pred):
    y = tf.cast(y, tf.int64)            # Ensure labels are int64
    y_pred = tf.cast(y_pred, tf.float32) # Ensure predictions are float32
    return tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=y_pred))

# Accuracy metric
# Accuracy metric
def accuracy(y_true, y_pred):
    y_pred = tf.argmax(y_pred, axis=1, output_type=tf.int32)  # Get predicted class
    y_true = tf.cast(y_true, tf.int32)  # Ensure y_true is in int32 format for comparison
    correct_prediction = tf.equal(y_true, y_pred)
    return tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


# Arrays to store metrics
test_loss_arr = []
test_acc_arr = []
epochs = []

# Training loop
for epoch in range(training_epoch):
    for step, (batch_data, batch_label) in enumerate(train_Data_M):
        with tf.GradientTape() as tape:
            pred_data = model(batch_data)
            loss = cross_entropy_loss(batch_label, pred_data)
            acc = accuracy(batch_label, pred_data)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    # Evaluate on test data after each epoch
    test_pred = model(test_Data_R)
    test_loss = cross_entropy_loss(test_Label, test_pred)
    test_acc = accuracy(test_Label, test_pred)
    print(f"Epoch {epoch+1}, Test Loss: {test_loss:.4f}, Test Accuracy: {test_acc:.4f}")

    test_loss_arr.append(test_loss)
    test_acc_arr.append(test_acc)
    epochs.append(epoch + 1)

# Plot loss and accuracy
plt.plot(epochs, test_loss_arr)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid()
plt.savefig("TF/week9/loss_graph.png")
plt.show()

plt.plot(epochs, test_acc_arr)
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.grid()
plt.savefig("TF/week9/accuracy_graph.png")
plt.show()
