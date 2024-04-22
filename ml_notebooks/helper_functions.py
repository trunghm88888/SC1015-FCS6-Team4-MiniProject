from matplotlib import pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder


# Encode categorical features
label_encoder = LabelEncoder()

def encode_categorical_features(df):
    for col in df.columns:
        if df[col].dtype == 'object' or df[col].dtype == 'bool' or df[col].dtype == 'category':
            df[col] = label_encoder.fit_transform(df[col])


def encode_categorical_features_as_frequency_encoding(df):
    for col in df.columns:
        if (df[col].dtype == 'object' or df[col].dtype == 'bool' or df[col].dtype == 'category'):
            df[col] = df[col].map(df[col].value_counts())


# Plot confusion matrix with annotations
def plot_confusion_matrix(cm, classes=['Negative', 'Positive'],
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        # print("Normalized confusion matrix")
    else:
        pass
        # print('Confusion matrix, without normalization')

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, format(cm[i, j], fmt),
                     ha="center", va="center",
                     color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()


def print_feature_importances(feature_importances, feature_names):
    # Feature importances
    indices = np.argsort(feature_importances)[::-1]

    # Print the feature ranking
    print("Feature ranking:")
    for f in range(len(feature_names)):
        print("%d. feature %s (%f)" % (f + 1, feature_names[indices[f]], feature_importances[indices[f]]))