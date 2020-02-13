---
title: "Machine Learning Evaluation"
tags: [Machine Learning]
categories:
  - Machine Learning
date: 2020-02-03
---

## **2. Machine Learning Evaluation**


**Learning outcomes**
  - Define *overfitting.* Apply a strategy to avoid overfitting.
  - List the main accuracy metrics to measure the performance of a
    classifier.
  - Choose the appropriate metric for a given classification problem.
  - Apeopley the metrics to real data sets and classifiers.

**Feature selection**

  - We need to transform the input to sth we can use – into something
    measurable
      - Each of the objects after feature selection corresponds to a
        point in a graph space
  - An image something more dense and defined – exactly what we want the
    algo to look at
  - Classification is later used to find a separating boundary in the
    data point space

**Two possible solutions**

  - If we learn classifiers, we are learning decision boundary
  - We like the more regular model than the complex one. But what is it
    that we are looking for? Ultimate goal is to make predictions about
    stuff we’ve never seen. Can I find out an underlying pattern to make
    predictions about points we haven’t seen generalization\!\!\!
      - So which one would we generalize better?
          - The more regular model will generalize better.
  - We need to find a balance between the complexity of the model and
    the amount of data to prevent underfit or overfit.

**Overfitting**

|                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------- |
| A model *overfits* when it describes the randomness associated with the data, rather than the underlying relationship between the data points. |

: When its being too specific for the training data point – and that we
won’t be able to generalize as the data is trained to the exact shape of
the training set.

General method to avoid this– **Occam’s razor**

|                                                     |
| --------------------------------------------------- |
| Entities should not be multiplied **unnecessarily** |

  - The idea in our case is, our entities= parameters of classifiers.
    The more parameter, the more complex decision boundaries are. We
    want simple BUT complex classifier that can capture our dataset. We
    need to understand and find where the right balance lies.

**Preventing overfitting**

  - **Test** **set –** to produce the final results
      - We need a new dataset to test. Way to do it split the dataset
        into two batches - *training set* and the *test set.* and don’t
        use them for training\!\! still labelled and supervised
      - We can use this *test data* to see how well the model
        (classifier) generalises for unseen data. to estimate the
        accuracy of the classifier.


  - **Example: parametric classifier**
      - Then there’s an issue. Each one will give diff model when you
        model them. And they will have diff parameters. And very diff
        decision boundary. If I train the model on the training set and
        compare the 3 on the test set – we’ll find the optimal one
          - NEED TO SEPEARETE test and training\!\!\!--\> or else, the
            model may overfit the test set
      - **Parameter** – numbers we optimize to train the model e.g.
        weights of the polynomial
          - changes the decision boundary
      - **Meta parameter**- Order of the polynomial – sth that
        determines how many orders we have.
          - By changing them, we get diff model


  - **Validation set –** to keep track of how well it is doing as it
    learns.
      - We split it further – training, validation, and test set.
      - When you are choosing the model (= evaluating the meta
        parameter), you need a validation data so that it generalises as
        well as possible. . Then when you test a parameter (classifier),
        you need a test set.
  - Training: test: validation is typically 50:25:25


  - **When to stop learning**
      - ![image](https://user-images.githubusercontent.com/33334078/74363219-091b4e00-4dc2-11ea-9fe6-5d41d3b92706.png)

  - You train each model on the training set to reduce the error. This
    error will eventually go down to 0.
      - Error reduces, but the validation error increases again\!\!\!
        Because its started to overfit- its too specific for that set,
        and not general enough\!\!\! So the additional dataset is used
        to *validate* what has been learned.
      - If error goes down in validation, we are generalizing fine\!\!\!
      - **Generalization means we need to find answer from unseen data
        \!\!\! VERY VERT IMOPORTATNT**

  - **Cross validation –** when you are short of training data, split
    the data into subset and train different models. So in the end we’ve
    trained K different models.
      - You get one model ,and that’s the best you could do with that
        model. Same with model 2. Then you use 2 models to compare.
      - We create number of batches and use 123 for training and 4 for
        validation. Then you change the one 234 for training and 1 for
        validation. can test the learned model on more data points. So
        you are validating on whole dataset eventually

**Question**\!\! Very imp concept

|                                 |
| ------------------------------- |
| What is the validation set for? |

: We use the validation set to perform model selection and check for
overfitting, but then for testing we need a separate test set. can never
use a same set to test them\!\!

**Question** 2 – The accuracy of the training set is 90%. Do we aim for
100%?
  - Not on the training set\!\!\! Coz then it overfits. But you want to
    aim for 100 on the test set. Goal is never to predict 100% on the
    stuff we already know\!\! We wanna generalise the new ones

**Measuring accuracy**

  - **Accuracy on a binary classifier**
      - Binary classification: positive or negative
      - You are breaking down accuracy -\> very imp\! When you care abt
        one class over another
          - Medical classifiers – V important is supporting diagnosis
          - We prefer false positive – then we can learn\!
      - !![image](https://user-images.githubusercontent.com/33334078/74363245-15071000-4dc2-11ea-8257-a65156ef6d29.png)
      - true positive/ negatives over everything\!\! – predicted as
        positives and actually positive
      - **Accuracy** = total number of correct classification (TP+TN)/
        everything
      - **Sensitivity** – true positive / actual positives (TP+FN)
      - **Specificity** **–** true negatives/ actual negatives (FP +TN)
      - **Precision** – true positives/ predicted positives (TP+FP)
          - From what’s been classified as positive, what really is
            positive??
          - If precision is low, we could do more testing

    <!-- end list -->

      - **Recall** (=sensitivity) –true positives/ actual positives
        (TP+FN)

<!-- end list -->

  - Q: sensitivity =0.857. TN = 30. What is FN?
      - 0.857 = 30/ (30+ n)
      - 0.857(30+n)=30
      - 25.71 + 0.857n = 30
      - N = 5


  - **Accuracy metrics -** Formula is written in the exam.
      - **F<sub>1</sub> -** combined Precision and recall as a single
        measure.
      - **MCC** – <span class="underline">unbalanced dataset</span> –
        when one class has many more classifiers. When one bracket in
        the denominator is 0, the whole denom = 1.
          - E.g. Since healthy class is more likely, you could just
            classify it as healthy\!

<!-- end list -->

  - **Confusion matrix -** To represent the accuracy of multiclass
    (non-binary) classifiers
      - Diagonal line – correct classification.
      - Each entry at the coordinate (x,y) corresponds to the number of
        elements of class x classified at class y. So it which classes
        are confusing the classifiers?
          - So bigger the number, higher error it is\! Its confusing
            other classes


  - **ROC (Receiver Operator Characteristic) curve** \[p 24\]– used to
    find what classifier is better than another.
      - Percentage of false positive and true positive
      - You want a very high true positive rate. But also good is very
        false positive, as they are classifiers that are always wrong\!
        – say opposite\! Rain- sunny. Sunny- umbrella
