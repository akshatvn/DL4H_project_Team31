# DL4H_project
UIUC Spring 2023

Authors: Akshat Agarwal and Ahmad Raza. 

## Original paper

Lu, Charles, Andréanne Lemay, Ken Chang, Katharina Höbel, and Jayashree Kalpathy-Cramer. "Fair conformal predictors for applications in medical imaging." In Proceedings of the AAAI Conference on Artificial Intelligence, vol. 36, no. 11, pp. 12008-12016. 2022.

## Link to the original paper’s repo 
https://github.com/clu5/AAAI-22

## Dependencies
All requirements from requirements.txt file from the original paper's repo plus
```
monai
TensorRT
```

## Data download instruction

1. Download the CSV from the original repo.
2. Run scraper.py from this repo
   1. Remember to alter `SAVE_DIR` in the scraper.py
   2. Remember to alter line 16 with actual path of the CSV file
   3. For efficiency I chose to run 8 separate processes, on separate chunks of the CSV file. A single process might take too long.

## Training Code

### 1. Clone the original repo
https://github.com/clu5/AAAI-22

### 2. Train the model
   This will generate prediction sets as json files
 Arguments to note:
 
|  arg  | purpose | 
|------|-------|
|   -a  | the architecture to use |
|   -e  | epochs |
|   -r  | runs |
|   -c  | the csv file to use |
|   -b  | the images directory (where you downloaded all the images using the scraper) |
|   -o  | the output directory (where you want the json files to go) |

e.g. 
```
!python3 drive/MyDrive/AAAI-22/src/train.py -a resnet18 --multi_gpu -e 20 -r 1 -c drive/MyDrive/AAAI-22/skin-info-ahmad.csv -b drive/MyDrive/AAAI-22/images2/images -o drive/MyDrive/Outputs
```

## Evaluation code + command

Run the [fitz.ipynb](https://github.com/clu5/AAAI-22/blob/main/fitz.ipynb) notebook for results on the generated prediction sets by altering the `run_dir` variable. 

## Reproducability result

<img width="1110" alt="resnet18_1" src="https://user-images.githubusercontent.com/5070409/236713175-62e6402d-2ff3-4af6-a993-72fd37e194fe.png">

<img width="1115" alt="resnet18_2" src="https://user-images.githubusercontent.com/5070409/236713189-18b12c0b-b5a4-439e-b7a8-01a419646bc2.png">

<img width="1113" alt="resnet18_3" src="https://user-images.githubusercontent.com/5070409/236713201-3937d3cd-a14a-4124-94c8-fb19ac727fd5.png">

## What we did

First we trained the model in the following ways: 
1. resnet50 with 20 epochs and 1 run [notebook here](https://github.com/akshatvn/DL4H_project_Team31/blob/main/results/fitz_resnet18_r1_e20.ipynb)
2. resnet18 with 20 epochs and 1 run [notebook here](https://github.com/akshatvn/DL4H_project_Team31/blob/main/results/fitz_resnet50_r1_e20.ipynb)

Then we compared the results to see how changing the model affected the hypotheses.


