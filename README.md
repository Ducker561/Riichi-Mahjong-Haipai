# Riichi-Mahjong-Haipai
This is a project of using Python Random library to check the haipai average shanten.

### Run

1. You can get a single haipai by using the function *single_haipai()* in **main.py**. And that haipai's yama info using the function *get_yama()* in **main.py**.
2. You can simply change the parameter *n* in **main.py** and make a n-round independent haipai test. And will feedback the average shanten of the n-round independent haipai test. 

### Libraries

Need **numpy**, but it's only used for calculating the average, you can change it into a normal one in **main.py -> *samples()***

### Results

Doing a 100000-round independent haipai test, the average shanten may be around **3.18**.

### References

The calculation of shanten is based on this link : https://blog.csdn.net/qq_51273457/article/details/113100157

