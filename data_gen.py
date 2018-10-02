import os

DOWNLOAD_DIR = '/Users/rajaraju/Downloads/Birds/'
BASE_DIR = '/Users/rajaraju/Downloads/birds_classes'


def data_directory(class_labels):
    """
        Creates the folder structure for Training, Validation and Test data and Class Labels.

        Parameters:
        class_labels : Names of the classes, for example: cats, dogs, horses.

    """

    dataset_folders = ['train','validation','test']
    object_class = class_labels
    os.mkdir(BASE_DIR)

    for folder in dataset_folders:
        for obj_cls in object_class:
            training_dir = BASE_DIR + os.sep +'{}'.format(folder)
            if not os.path.exists(BASE_DIR+os.sep +'{}'.format(folder)):
                os.mkdir(training_dir)
            class_dir = training_dir + os.sep + '{}'.format(obj_cls)
            if not os.path.exists(training_dir + os.sep + '{}'.format(obj_cls)):
                os.mkdir(class_dir)
