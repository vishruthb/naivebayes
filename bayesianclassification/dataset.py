import uncertainty
import pandas as pd

df = pd.DataFrame()

df = df.append(uncertainty.anomaly("test_mnist_2labels_1", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[0,1], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_2labels_2", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[2,7], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_2labels_3", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[8,9], plot = False))

df = df.append(uncertainty.anomaly("test_mnist_5labels_1", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[0,2,4,6,8], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_5labels_2", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[1,3,5,7,9], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_5labels_3", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[0,1,2,3,4], plot = False))

df = df.append(uncertainty.anomaly("test_mnist_8labels_1", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[2,3,4,5,6,7,8,9], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_8labels_2", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[0,1,3,4,5,6,8,9], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_8labels_3", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[0,1,2,3,4,5,6,7], plot = False))

df = df.append(uncertainty.anomaly("test_mnist_2labels_1", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[0,1], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_2labels_2", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[2,7], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_2labels_3", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[8,9], plot = False))

df = df.append(uncertainty.anomaly("test_mnist_5labels_1", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[0,2,4,6,8], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_5labels_2", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[1,3,5,7,9], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_5labels_3", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[0,1,2,3,4], plot = False))

df = df.append(uncertainty.anomaly("test_mnist_8labels_1", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[2,3,4,5,6,7,8,9], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_8labels_2", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[0,1,3,4,5,6,8,9], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_8labels_3", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[0,1,2,3,4,5,6,7], plot = False))

df = df.append(uncertainty.anomaly("test_mnist_2labels_1", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[0,1], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_2labels_2", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[2,7], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_2labels_3", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[8,9], plot = False))

df = df.append(uncertainty.anomaly("test_mnist_5labels_1", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[0,2,4,6,8], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_5labels_2", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[1,3,5,7,9], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_5labels_3", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[0,1,2,3,4], plot = False))

df = df.append(uncertainty.anomaly("test_mnist_8labels_1", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[2,3,4,5,6,7,8,9], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_8labels_2", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[0,1,3,4,5,6,8,9], plot = False))
df = df.append(uncertainty.anomaly("test_mnist_8labels_3", "mnist", acc_threshold = 0.985, num_epochs = 100, inside_labels=[0,1,2,3,4,5,6,7], plot = False))


"""
df = df.append(uncertainty.anomaly("test_cifar_2labels_1", "cifar", num_epochs = 100, inside_labels=[0,1], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_2labels_2", "cifar", num_epochs = 100, inside_labels=[2,7], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_2labels_3", "cifar", num_epochs = 100, inside_labels=[8,9], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_5labels_1", "cifar", num_epochs = 100, inside_labels=[0,2,4,6,8], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_5labels_2", "cifar", num_epochs = 100, inside_labels=[1,3,5,7,9], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_5labels_3", "cifar", num_epochs = 100, inside_labels=[0,1,2,3,4], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_8labels_1", "cifar", num_epochs = 100, inside_labels=[2,3,4,5,6,7,8,9], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_8labels_2", "cifar", num_epochs = 100, inside_labels=[0,1,3,4,5,6,8,9], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_8labels_3", "cifar", num_epochs = 100, inside_labels=[0,1,2,3,4,5,6,7], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_2labels_1", "cifar", num_epochs = 100, inside_labels=[0,1], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_2labels_2", "cifar", num_epochs = 100, inside_labels=[2,7], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_2labels_3", "cifar", num_epochs = 100, inside_labels=[8,9], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_5labels_1", "cifar", num_epochs = 100, inside_labels=[0,2,4,6,8], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_5labels_2", "cifar", num_epochs = 100, inside_labels=[1,3,5,7,9], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_5labels_3", "cifar", num_epochs = 100, inside_labels=[0,1,2,3,4], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_8labels_1", "cifar", num_epochs = 100, inside_labels=[2,3,4,5,6,7,8,9], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_8labels_2", "cifar", num_epochs = 100, inside_labels=[0,1,3,4,5,6,8,9], plot = False))
df = df.append(uncertainty.anomaly("test_cifar_8labels_3", "cifar", num_epochs = 100, inside_labels=[0,1,2,3,4,5,6,7], plot = False))
"""
df.to_csv("uncertainty_experiments.csv")
