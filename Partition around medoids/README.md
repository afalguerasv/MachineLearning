# README

This is a university practice that asks us if we can make a Partition Around Medoids algorithm using only string data,
no integers or any type of standardization.

You can find the data used in this algorithm in the machine learning repository in this [link](http://archive.ics.uci.edu/ml/datasets/Adult)

Algorithm open the data in a .csv format in a specific path, to use the algorithm is necessary modify the path to the source as you need.

The difficult part of the algorithm is deciding how to measure the distance between different data. I decided to measure distance as the number of different words between medoids and each instance like the example below:

These are two instances of the data set, supose the first one as a medoid and the second as an instance

```python

[[‘Federal-gov’, ‘HS-grad’, ‘Never-married’, ‘Other-service’, ‘Own-child’, ‘Black’, ‘Male’, United-States’, ‘&lt;=50K’]
[‘Private’, ‘Assoc-acdm’, ‘Divorced’, ‘Exec-managerial’, ‘Unmarried’, ‘White’, ‘Female’, ‘England’, ‘&lt;=50K’]]
```

Distance between them will be 8 because they have not any equal value in any column, take care, the last column is the class and is not used to calculate distance.

If we have for example:

```python
[[‘Federal-gov’, ‘HS-grad’, ‘Never-married’, ‘Other-service’, ‘Own-child’, ‘Black’, ‘Male’, United-States’, ‘&lt;=50K’]
[‘Federal-gov’, ‘HS-grad’, ‘Never-married’, ‘Other-service’, ‘Own-child’, ‘Black’, ‘Female’, United-States’, ‘&lt;=50K’]]
```

The only difference is the gender, so distance is equal to 1.

### Conclusions after use the algorithm:

Algorithm is not good to make predictions; it usually does not have a got predictions rate. The problem is that the algorithm does not deep enough, it considers the same distance this:

```python
[[‘Federal-gov’, ‘HS-grad’, ‘Never-married’, ‘Other-service’, ‘Own-child’, ‘Black’, ‘Male’, United-States’, ‘&lt;=50K’]
[‘Federal-gov’, ‘HS-grad’, ‘Never-married’, ‘Other-service’, ‘Own-child’, ‘Black’, ‘Female’, United-States’, ‘&lt;=50K’]]
```

And this:

```python
[[‘Federal-gov’, ‘HS-grad’, ‘Never-married’, ‘Other-service’, ‘Own-child’, ‘Black’, ‘Male’, United-States’, ‘&lt;=50K’]
[‘Private’, ‘HS-grad’, ‘Never-married’, ‘Other-service’, ‘Own-child’, ‘Black’, ‘Male’, United-States’, ‘&lt;=50K’]]
```

In first case only gender is different in the second case only the workclass is different but algorithm give in both cases distance 1.

#### A possible solution:

Giving the above examples, we should consider for second case with distance equal to 1 because the first column is diferent. In first case is the 7 th column different so distance should be equal to 7.

If we have more than one column different like:

```python
[[‘Federal-gov’, ‘HS-grad’, ‘Never-married’, ‘Other-service’, ‘Own-child’, ‘Black’, ‘Male’, United-States’, ‘&lt;=50K’]
[‘Private’, ‘HS-grad’, ‘Never-married’, ‘Other-service’, ‘Own-child’, ‘White’, ‘Female’, United-States’, ‘&lt;=50K’]]
```

Columns 1, 6 and 7 are diferent, so distance between them should be, 1+6+7=14
