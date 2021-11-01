
def load_dataset(dataset_name):
    with open(dataset_name,"r") as f:
        satir_liste=f.readlines()
        f.close()
    return satir_liste