import pickle


def save_pkl(pkl_file, answers):
    with open(pkl_file, 'wb') as handle:
        pickle.dump(answers, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_pkl(pkl_file):
    # load pkl
    with open(pkl_file, 'rb') as handle:
        b = pickle.load(handle)
        return b

