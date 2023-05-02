import tensorflow as tf
import pandas as pd
import numpy as np

class DataHandler:

    # def __init__(self):

    def load_excel(self, path:str) -> pd.DataFrame:
        """
        path: path to excel file
        """
        return pd.read_excel(path)

    def combine_and_load_excel(self, paths:list, axis:int=0) -> pd.DataFrame: 
        """
        paths: array of path to excel files
        axis: axis to combine along. Default value=0
        """
        data_frames = [self.load_excel(path) for path in paths ]
        return pd.concat(data_frames, axis)

    def load_jpeg_image(self, image_path:tf.Tensor, label:tf.Tensor) -> tuple:
        """
        Loads jpeg images with three channels
        image_path: path to image
        label: corresponding label
        size: list of length 2 having [width, height]
        """
        image = tf.io.read_file(image_path)
        image = tf.io.decode_jpeg(image, channels=3)
        image = tf.image.resize(image, [250, 250])
        image = tf.keras.applications.inception_resnet_v2.preprocess_input(image)
        return image, label

    def load_data(self, path, base_image_path, batch_size=32):
        df = self.load_excel(path)
        image_path_df = base_image_path + df["Fundus"].values
        labels_df = df.iloc[:, 4:].values
        image_path_df = tf.constant(image_path_df)
        labels_df = tf.constant(labels_df)
        dataset = tf.data.Dataset.from_tensor_slices((image_path_df, labels_df))
        dataset = dataset.map(self.load_jpeg_image)
        dataset = dataset.batch(batch_size)
        return dataset

    def split_data(self, dataset:tf.data.Dataset, train_split:float, test_split:float, val_split:float) -> tuple:
        # Calculate the size of each split
        dataset_size = dataset.reduce(tf.constant(0, dtype=tf.int64), lambda acc, _: acc + 1).numpy()
        train_size = int(dataset_size * train_split)
        val_size = int(dataset_size * val_split)
        test_size = int(dataset_size * test_split)

        # Shuffle the elements of the dataset randomly
        dataset = dataset.shuffle(buffer_size=dataset_size, seed=42)

        # Split the dataset into train, validation, and test sets
        train_dataset = dataset.take(train_size)
        remaining_dataset = dataset.skip(train_size)
        val_dataset = remaining_dataset.take(val_size)
        test_dataset = remaining_dataset.skip(val_size)
        return train_dataset, test_dataset, val_dataset

    def plot_acc_loss(self, history):
        import matplotlib.pyplot as plt
        plt.plot(history.history['accuracy'])
        plt.plot(history.history['val_accuracy'])
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'validation'], loc='upper left')
        plt.show()
        # "Loss"
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'validation'], loc='upper left')
        plt.show()

    

        