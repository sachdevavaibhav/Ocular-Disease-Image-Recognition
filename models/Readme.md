# Comparing different models and there accuracy on train dataset 

|  Model  | Layer | Layer Type | Units | Activation | Epochs | Train Accuracy(%)|
|:-------:|:-----:|:----------:|:-----:|:----------:|:------:|:----------------:|
|  Model1 |   1   |    Dense   |  512  |    relu    |    5   |       98.88      |
|         |   2   |    Dense   |   10  |   softmax  |        |                  |
|  Model2 |   1   |    Dense   |  512  |    relu    |    5   |       98.95      |
|         |   2   |    Dense   |  256  |    relu    |        |                  |
|         |   3   |    Dense   |  128  |    relu    |        |                  |
|         |   4   |    Dense   |   10  |   softmax  |        |                  |
|  Model3 |   1   |    Dense   |  512  |    relu    |    5   |       98.86      |
|         |   2   |    Dense   |  256  |    relu    |        |                  |
|         |   3   |    Dense   |  128  |    relu    |        |                  |
|         |   4   |    Dense   |   64  |    relu    |        |                  |
|         |   5   |    Dense   |   10  |   softmax  |        |                  |
|  Model4 |   1   |    Dense   |  512  |    relu    |    5   |       98.84      |
|         |   2   |    Dense   |  256  |    relu    |        |                  |
|         |   3   |    Dense   |  128  |    relu    |        |                  |
|         |   4   |    Dense   |   64  |    relu    |        |                  |
|         |   5   |    Dense   |   32  |    relu    |        |                  |
|         |   6   |    Dense   |   10  |   softmax  |        |                  |
|  Model5 |   1   |    Dense   |  512  |    relu    |    5   |       98.66      |
|         |   2   |    Dense   |  256  |    relu    |        |                  |
|         |   3   |    Dense   |  128  |    relu    |        |                  |
|         |   4   |    Dense   |   64  |    relu    |        |                  |
|         |   5   |    Dense   |   32  |    relu    |        |                  |
|         |   6   |    Dense   |   16  |    relu    |        |                  |
|         |   7   |    Dense   |   10  |   softmax  |        |                  |
|  Model6 |   1   |    Dense   |  512  |    relu    |    5   |       99.09      |
|         |   2   |    Dense   |  256  |    relu    |        |                  |
|         |   3   |    Dense   |   10  |   softmax  |        |                  |
|  Model7 |   1   |    Dense   |  512  |   sigmoid  |    5   |       97.25      |
|         |   2   |    Dense   |  256  |   sigmoid  |        |                  |
|         |   3   |    Dense   |   10  |   softmax  |        |                  |
|  Model8 |   1   |    Dense   |  512  |    relu    |   10   |       99.65      |
|         |   2   |    Dense   |  256  |    relu    |        |                  |
|         |   3   |    Dense   |   10  |   softmax  |        |                  |
|  Model9 |   1   |    Dense   |  512  |    relu    |   20   |       99.91      |
|         |   2   |    Dense   |  256  |    relu    |        |                  |
|         |   3   |    Dense   |   10  |   softmax  |        |                  |
| Model10 |   1   |    Dense   |  512  |    relu    |   30   |       99.93      |
|         |   2   |    Dense   |  256  |    relu    |        |                  |
|         |   3   |    Dense   |   10  |   softmax  |        |                  |