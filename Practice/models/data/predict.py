import matplotlib.pyplot as plt

def extract_results(predictions):
    predictions = list(map(lambda prediction:prediction.argmax(), predictions))
    return predictions

def plot_results(predictions, test_images, test_labels):
    rows = 4 
    cols = 4
    fig = plt.figure(figsize=(15,15))
    for j in range(rows*cols):
        fig.add_subplot(rows, cols, j+1)
        plt.text(1,-1,f'label:{test_labels[j]} prediction:{predictions[j]}', size='xx-large')
        plt.imshow(test_images[j].reshape(28,28),cmap=plt.cm.binary)
