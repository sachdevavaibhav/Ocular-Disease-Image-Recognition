from tensorflow.keras.datasets import mnist

def load_data():
    """
    Loads the MNIST data and normalize it.
    params:
    return: (train_images, train_labels,test_images, test_labels)
    """
    (train_images, train_labels),(test_images, test_labels) = mnist.load_data()
    len_train_data = len(train_images)
    len_test_data = len(test_images)
    train_images = train_images.reshape(len_train_data, 28*28)
    train_images=train_images.astype('float32')/255
    test_images = test_images.reshape(len_test_data, 28*28)
    test_images=test_images.astype('float32')/255
    return (train_images, train_labels,test_images, test_labels)