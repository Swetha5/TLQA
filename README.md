# TLQA - TimeLogic: A Temporal Logic Benchmark for Video QA

## TLQA Dataset 
The TLQA benchmark is released under `./data` for all the datasets.

For each of the datasets, we provide Boolean and Multiple-Choice benchmark splits. 

We provide QA pairs for each temporal category as a pickle file. 

Each sample has `video_id`, `question_id`, `question`, `answer`, `answer_option` (for multiple-choice only)

For boolean splits, the questions are under `positive_questions` and `negative_questions` while MCQ is `word_questions`.

### Usage

```python
import pickle

def load_pkl(pkl_file):
    # load pkl
    with open(pkl_file, 'rb') as handle:
        b = pickle.load(handle)
        return b

data = load_pkl('path_to_pkl_file')
```



## Framework

The source code for framework will be released under `src`

We only provide the processed files for each dataset, please download the videos and annotations for each dataset from original dataset webpage.

* [STAR](https://bobbywu.com/STAR/)
* [AGQA](https://cs.stanford.edu/people/ranjaykrishna/agqa/)
* [Breakfast](https://serre-lab.clps.brown.edu/resource/breakfast-actions-dataset/)
* [CrossTask](https://github.com/DmZhukov/CrossTask)






