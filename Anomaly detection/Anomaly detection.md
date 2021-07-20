## Anomaly detection



#### 정의

- Normal(정상) sample과 Abnormal(비정상, 이상치, 특이치) sample을 구별해내는 문제를 의미하여 제조업뿐만 아니라 CCTV, 의료 영상, Social Network 등 다양한 분야에서 응용 되고 있다.

- 학습 데이터 셋에 비정상적인 sample이 포함되는지, 각 sample의 label이 존재하는지, 비정상적인 sample의 성격이 정상 sample과 어떻게 다른지, 정상 sample의 class가 단일 class인지 멀티 class 인지 등에 따라 다른 용어를 사용한다.



#### 학습시 비정상 sample의 사용여부 및 label 유무에 따른 분류

1. **Supervised Anomaly Detection**

   주어진 학습 데이터 셋에 정상 sample과 비정상 sample의 Data와 Label이 모두 존재하는 경우 Supervised Learning 방식이기 때문에 Supervised Anomaly Detection이라 부릅니다. Supervised Learning 방식은 다른 방법 대비 정확도가 높은 특징이 있다. 그래서 높은 정확도를 요구로 하는 경우에 주로 사용되며, 비정상 sample을 다양하게 보유할수록 더 높은 성능을 달성할 수 있다.

   하지만 Anomaly Detection이 적용되는 일반적인 산업 현장에서는 정상 sample보다 비정상 sample의 발생 빈도가 현저히 적기 때문에 **Class-Imbalance(불균형)** 문제가 자주 발생한다. 이러한 문제를 해결하기 위해 Data Augmentation(증강), Loss function 재설계, Batch Sampling 등의 연구가 필요하다.

   - 장점: 양/불 판정 정확도가 높다.

   - 단점: 비정상 sample을 취득하는데 시간과 비용이 많이 든다. Class-Imbalance 문제를 해결해야 한다.

     

2. **Semi-supervised (One-Class) Anomaly Detection**

   Class-Imbalance가 매우 심한 경우 정상 sample만 이용해서 모델을 학습하기도 하는데, 이 방식을 One-Class Classification(혹은 Semi-supervised Learning)이라 한다.

   정상 sample들을 둘러싸는 discriminative boundary를 설정하고, 이 boundary를 최대한 좁혀 boundary 밖에 있는 sample들을 모두 비정상으로 간주하는 것이다.  **One-Class SVM** 이 One-Class Classification을 사용하는 대표적인 방법론으로 잘 알려져 있다.

   - 장점: 비교적 활발하게 연구가 진행되고 있으며, 정상 sample만 있어도 학습이 가능하다.

   - 단점: Supervised Anomaly Detection 방법론과 비교했을 때 상대적으로 양/불 판정 정확도가 떨어진다.

     

3. **Unsupervised Anomaly Detection**

   대부분의 데이터가 정상 sample이라는 가정을 하여 Label 취득 없이 학습을 시키는 Unsupervised Anomaly Detection 방법론이다. 가장 단순하게는 주어진 데이터에 대해 **Principal Component Analysis**(PCA, 주성분 분석)를 이용하여 차원을 축소하고 복원을 하는 과정을 통해 비정상 sample을 검출할 수 있다. 

   주로 Autoencoder를 사용하는데 **Autoencoder**란 입력을 코드 혹은 latent variable(잠재 변수)로 압축하는 Encoding과, 이를 다시 원본과 가깝게 복원해내는 Decoding 과정으로 진행한다. 

   (code size, latent variable의 dimension) 같은 hyper parameter에 따라 전반적인 복원 성능이 좌우 되기 때문에 양/불 판정 정확도가 Supervised Anomaly Detection에 비해 다소 불안정하다.

   또한, input과 output의 차이를 어떻게 방식을 정의할 것인지, 어느 loss function을 사용해 autoencoder를 학습시킬지 등 여러가지 요인에 성능이 달라진다.

   

   - 장점: Labeling 과정이 필요하지 않다.
   - 단점: 양/불 판정 정확도가 높지 않고 hyper parameter에 매우 민감하다.

   

   ![image-20210720081320970](C:\Users\JEONKYUBIN\AppData\Roaming\Typora\typora-user-images\image-20210720081320970.png)

![image-20210720081330767](C:\Users\JEONKYUBIN\AppData\Roaming\Typora\typora-user-images\image-20210720081330767.png)



그림 출처 : Improving Unsupervised Defect Segmentation by Applying Structural Similarity To Autoencoders , 2019 arXiv [autoencoder 기반 unsupervised anomoly detection]





#### 비정상 sample 정의에 따른 분류

크게 Novelty Detection과 Outlier Detection으로 구분하는데 종종 두 방법론을 합쳐서 Anomaly Detection라 부른다.

![image-20210720085057620](C:\Users\JEONKYUBIN\AppData\Roaming\Typora\typora-user-images\image-20210720085057620.png)

현재 보유 중인 데이터 셋에 이전에 없던 새로운 데이터 형태가 등장하는 경우를 Novel sample, Unseen Sample 등으로 부른다. 이러한 sample을 찾아내는 방법론을 Novelty Detection이라 부른다.

데이터셋에 전혀 관련 없는 sample들을 Outlier sample, Abnormal sample이라 부른다. 이러한 sample을 찾아내는 문제를 Outlier Detection이라 부른다.

**Novelty Detection**은 지금까지 등장하지 않았지만 충분히 등장할 수 있는 sample을 찾아내는 연구, 즉 데이터가 오염이 되지 않은 상황을 가정하는 연구와 관련된 용어라고 정의할 수 있다. 

**Outlier Detection**은 등장할 가능성이 거의 없는, 데이터에 오염이 발생했을 가능성이 있는 sample을 찾아 내는 연구와 관련된 용어 정도로 구분하여 정리할 수 있다.



#### 정상 sample의 class 개수에 따른 분류

정상 sample이 Multi-Class인 상황에서도 위의 Novelty Detection, Outlier Detection 기준을 똑같이 적용할 수 있다. 보통 이러한 경우 정상 sample이라는 표현 대신 **In-distribution sample**이라는 표현을 사용한다. 

In-distribution 데이터 셋으로 network를 학습시킨 뒤, test 단계에서 비정상 sample을 찾는 문제를 **Out-of-distribution Detection** 이라 부르며 학계에서는 널리 사용되는 주요 Benchmark 데이터 셋들을 이용하여 실험을 수행하고 있다.

대부분의 연구에서 주로 사용하는 SoftMax 기반 classifier는 class 개수를 정해 놓고 가장 확률이 높은 class를 결과로 출력하는 방식이기 때문에, 예시로  4가지 종류의 강아지를 구분하는 classifier에 호랑이 이미지를 넣어주면 사람은 비정상 sample이라고 구분할 수 있는 반면 classifier는 4가지 class 중 하나의 class로 예측을 하게 된다.  이러한 Outlier sample을 걸러 내기 위해 Out-of-distribution Detection 알고리즘을 사용할 수 있다.

또한 불독 이미지처럼 Novel 한 sample이 관찰됐을 때 이를 걸러낸 뒤, classifier가 기존에 있는 4가지 class 대신 불독이 새로 추가된 5가지 class를 구분하도록 학습하는 **Incremental Learning** 방법론과도 응용이 가능하다.





## Principal Component Analysis

##### autoencoder 종류

youtube naverD2 autoencoder 한 강의 설명하기  

간단한 난이도 통계학 공부



Revisit Deep Neural Networks

Maniford Learning

Autoencoders

- Linear Autoencoder
- Stacking Autoencoder
- **Denoising Autoencoder**
- Stacked Denoising Autoencoder
- Stochastic Contractive Autoencoder
- Contractive Auroencoder

- **Variational Autoencoders**
- **Adversarial Auroencoder**

Applications

