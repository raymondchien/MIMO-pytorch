# MIMO-pytorch

PyTorch implementation of MIMO proposed in [Training independent subnetworks for robust prediction](https://openreview.net/forum?id=OGg9XnKxFAH).

# Model Training

``` sh
python train.py
```

# Results

For convenience, I trained small CNN-based models on MNIST for 10 epochs.
Note that the result below is not thoroughly verified.

## Valid set Accuracy

| The number of subnetworks (M) | Valid Set Accuracy |
| -------------| ---------- |
| 1 (Baseline) | 99.19%     |
| 2            | 99.27%     |
| 3            | 99.21%     |
| 4            | 99.26%     |
| 5            | 99.17%     |

# References

``` plain
@inproceedings{havasi2021training,
  author = {Marton Havasi and Rodolphe Jenatton and Stanislav Fort and Jeremiah Zhe Liu and Jasper Snoek and Balaji Lakshminarayanan and Andrew M. Dai and Dustin Tran},
  title = {Training independent subnetworks for robust prediction},
  booktitle = {International Conference on Learning Representations},
  year = {2021},
}
```

* https://github.com/google/edward2/tree/master/experimental/mimo
