# DL4H_project


## Steps to replicate

1. Clone this repo: https://github.com/clu5/AAAI-22

2. Train the model
   This will generate prediction sets as json files

e.g. 
```
!python3 drive/MyDrive/AAAI-22/src/train.py -a resnet18 --multi_gpu -e 20 -r 1 -c drive/MyDrive/AAAI-22/skin-info-ahmad.csv -b drive/MyDrive/AAAI-22/images2/images -o drive/MyDrive/Outputs
```


3. Run the fitz.ipynb notebook for results on the generated prediction sets by altering the `run_dir` variable.


## What we did

First we trained the model in 3 ways: 
1. resnet50 with 100 epochs and 5 runs [original paper]
2. resnet18 with 20 epochs and 1 run 
3. 

Then we compared the results to see how changing the model affected the hypotheses


