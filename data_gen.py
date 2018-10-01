import os, shutil

def dataset_generation(download_dir,base_dir,number_of_classes,class_names):
    """
        Collects data from download location, segregates data in different folders
        based on object class.

        Parameters:

        download_dir : Original location of the data downloaded.
        base_dir : Location of the directory where data will be stored as training and test sets based on their class.
        number_class : Number of object classes
        class_names : Names of the classes, for example: cats, dogs, horses.

        Returns : training and test directory.

    """

    os.mkdir(base_dir)

    dataset_folders = ['train','validation','test']
    object_class = ['cat','dog','horse']
    os.mkdir(base_dir)
    for folder in dataset_folders:
        for obj_cls in object_class:
            training_dir = base_dir + os.sep +'{}'.format(folder)
            if not os.path.exists(base_dir+os.sep +'{}'.format(folder)):
                os.mkdir(training_dir)
            class_dir = training_dir + os.sep + '{}'.format(obj_cls)
            if not os.path.exists(training_dir + os.sep + '{}'.format(obj_cls)):
                os.mkdir(class_dir)
