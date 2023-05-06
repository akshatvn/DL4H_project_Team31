# DL4H_project


## Steps to replicate

### 1. Clone the original repo
https://github.com/clu5/AAAI-22

### 2. Download the images using scraper.py

### 3. Train the model
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


### 4. Run the fitz.ipynb notebook for results on the generated prediction sets by altering the `run_dir` variable.


## What we did

First we trained the model in the following ways: 
1. resnet50 with 20 epochs and 1 run
2. resnet18 with 20 epochs and 1 run 

Then we compared the results to see how changing the model affected the hypotheses, for example


