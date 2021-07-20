#### 차원의 저주

머신러닝에서 데이터 셋의 특성(feature)가 많아지면, 각 특성인 하나의 차원(dimension) 또한 증가하게 된다. 이렇게 데이터의 차원이 증가할 수록 데이터의 공간의 부피가 기하 급수적으로 증가하기 때문에, 데이터의 밀도는 차원이 증가할 수록 회소(sparse)해진다.

데이터의 차원이 증가할수록 데이터 포인트 간의 거리 또한 증가하고, 이러한 데이터를 이용해 머신러닝 알고리즘을 학습 하게되면 모델이 복잡해지게 된다. 따라서, 오버피팅(overfitting) 위험이 커진다.

#### 

#### 차원 축소를 위한 접근 방법

1. 투영 (Projection)

   일반적으로 대부분의 실제 데이터셋에서는 모든 데이터의 특성, 즉 차원이 고르게 분포되어 있지 않다. 필기체 숫자 데이터셋인 MNIST를 예시로, 어떤 특성(각 pixel을 하나의 특성으로 볼 때)은 거의 변화가 없고, 또 어떤 특성은 다른 특성들과 서로 연관되어 있다.

   이렇듯 학습 데이터셋은 고차원 공간에서 저차원 부분 공간(subspace)에 위치하게 된다. 즉, 고차원의 데이터 특성 중 일부 특성으로 데이터를 표현할 수 있다는 말이 된다.

![image-20210720211513734](C:\Users\JEONKYUBIN\AppData\Roaming\Typora\typora-user-images\image-20210720211513734.png)





2. 매니폴드 학습 (Manifold Learning)

   매니폴드는 다양체라고도 하며 국소적으로 유클리드 공간과 닮은 위상 공간이다. 즉, 국소적으로는 유클리드 공간과 구별할 수 없으나 , 대역적으로 독특한 위상수학적 구조를 가질 수 있다(출처: *위키피디아* ). 예를들어, 아래의 원 그림은 모든 점에 대해서 국소적으로 직선과 같은 구조를 가지는 1차원 매니폴드라 할 수 있다.

   아래 그림은 스위스 롤(swiss roll, 롤케잌 모양의 데이터셋) 데이터셋이며 2D-매니폴드의 한 예이다. 그림에서 볼 수 있듯이 2D-매니폴드는 고차원(3차원) 공간에서 휘거나 말린 2D 모양이다. 일반적으로 -차원 매니폴드는 국소적으로 -차원 초평면으로 볼 수 있는 -차원 공간의 일부이다(). 스위스 롤은 이고 인, 국소적으로는 2D 평면이지만 3차원으로 말려있는 데이터이다.

   

   ![image-20210720211755683](C:\Users\JEONKYUBIN\AppData\Roaming\Typora\typora-user-images\image-20210720211755683.png)



대부분의 차원 축소 알고리즘이 이러한 매니폴드를 모델링하는 방식으로 동작하고 이를 매니폴드 학습이라 한다. 매니폴드 학습은 매니폴드 가정 또는 매니폴드 가설에 의해, 고차원인 실제 데이터셋이 더 낮은 저차원 매니폴드에 가깝게 놓여 있다고 가정한다. 



매니폴드 가정은 분류나 회귀같은 작업을 하기전에 학습 데이터셋을 저차원의 매니폴드 공간으로 표현하면 더 간단하게 문제를 해결할 수 있다라는 가정을 할 수 있다.

![image-20210720214057836](C:\Users\JEONKYUBIN\AppData\Roaming\Typora\typora-user-images\image-20210720214057836.png)

반대로 이러한 가정이 통하지 않는 경우가 발생한다. 저차원 매니폴드가 오히려 결정 경계(decision boundary)를 찾는 것이 더 어려운 것을 알 수 있다. 

![image-20210720214200759](C:\Users\JEONKYUBIN\AppData\Roaming\Typora\typora-user-images\image-20210720214200759.png)



따라서, 모델을 학습시키기 전에 학습 데이터셋의 차원을 감소시키면 학습 속도는 빨라지지만 모델의 성능은 항상 더 낫거나 간단한 모델이 되는 것은 아니다. 이것은 데이터셋이 어떠한 모양을 하고 있느냐에 따라 달라진다.





#### PCA (Principal Component Analysis)



1. 분산 보존

   저차원의 초평면에 데이터를 투영하기 전에 먼저 적절한 초평면을 선택해야 한다. PCA는 데이터의 분산이 최대가 되는 축을 찾는다. 즉, 원본 데이터셋과 투영된 데이터셋 간의 **평균제곱거리**를 **최소화** 하는 축을 찾는다.

![image-20210720214645681](C:\Users\JEONKYUBIN\AppData\Roaming\Typora\typora-user-images\image-20210720214645681.png)

​      C1 축을 기준으로 투영한 데이터가 분산이 최대로 보존되는 것을 확인할 수 있다. 



2. 주성분(Principal Component)

   PCA는 다음과 같은 단계로 이루어진다.

   (1) 학습 데이터셋에서 분산이 최대인 축(axis)을 찾는다.

   (2) 찾은 첫번째 축과 직교(orthogonal)하면서 분산이 최대인 두 번째 축을 찾는다.

   (3) 첫 번째 축과 두 번째 축에 직교하고 분산을 최대한 보존하는 세 번째 축을 찾는다.

   (4) 1~3 과 같은 방법으로 데이터셋의 차원(특성 수)만큼 의 축을 찾는다.

   

   이렇게 i-번째 축을 정의하는 **단위 벡터**(unit vector)를 i-번째 **주성분**(PC, Principal Component)이라고 한다.







### Autoencoder의 종류

- Autoencoders

  우선 VAE의 배경이 되는 Autoencoder는 data를 만들어내기 위하여 사용하지 않고, label 되어있지 않은 트레이닝 데이터로부터 lower dimensional feature을 unsupervised learning을 통해 배운다.

  input data x가 있고 이 데이터로부터 feature z를 생성하도록 Encoder을 학습시킬 것이다.

  원래의 인코더는 linear + nonlinearity를 통해서 설계되었고 그 후 Deep, fc 모델을 통해서, 그리고 그 후에는 ReLU CNN을 통해서 설계되어 왔다.

  주로, z는 x보다 dimensionality가 축소된다. 그 이유는 z는 x로부터 뽑힌 가장 중요한 정보들만을 담고 있어야 하기 때문이다.

  ![image-20210720221512774](C:\Users\JEONKYUBIN\AppData\Roaming\Typora\typora-user-images\image-20210720221512774.png)

  이 autoencoder을 학습시키는 방법은 x를 통해 x를 복원하는 방법을 사용한다.

  주로 이 모델은 conv를 이용해서 설계한다. 그냥 데이터만 복구시키면 의미있는 feature들만 남는 이유는 

  **손실된 적은 양의 정보(z)를 통해서 원본을 복구하기 위해서 의미있는 feature만 남기기** 때문이다.

  마지막으로 훈련이 끝나면 디코더를 삭제하면 의미있는 feature들을 만들어내는 decoder이 완성된다.

​		![image-20210720221942663](C:\Users\JEONKYUBIN\AppData\Roaming\Typora\typora-user-images\image-20210720221942663.png)

​		이 encoder로부터 나온 데이터를 feature로 추가적인 모델을 붙여서 classifier의 전처리로 사용할 수도 있다.

​		좋은 feature을 뽑기 때문이다.

- Linear Autoencoder

- Stacking Autoencoder

- **Denoising Autoencoder**

  

- Stacked Denoising Autoencoder

- Sparse Autoencoder

- Stochastic Contractive Autoencoder

- Contractive Auroencoder

- **Variational Autoencoders**

  AE와 VAE의 차이점은 AE는 잠재공간 z에 값을 저장하고 VAE는 확률 분포를 저장하여 (평균, 분산) 파라미터를 생성한다는 점이다.

  ![image-20210720223310722](C:\Users\JEONKYUBIN\AppData\Roaming\Typora\typora-user-images\image-20210720223310722.png)

  VAE의 decoder는 encoder가 만들어낸 z의 평균, 분산을 모수로 하는 정규분포를 전제하고 데이터의 사후확률 p(z|x)를 학습한다. 하지만 사후확률의 계산이 어렵기 때문에 다루기 쉬운 분포 q(z)로 근사하는 variational inference (변분추론)을 사용한다. 변분추론은 p(z|x)와 q(z)사이의 KL-Divergence를 계산하고, KLD가 줄어드는 쪽으로 q(z)를 조금씩 업데이트 해서 q(z)를 얻어낸다.

  - 아래 식은 데이터가 고차원인 경우 q학습이 어렵다. 복잡한 데이터에 비해 지나치게 단순한 모델이기 때문.

  1) q(z) = N(평균,분산)

  그래서 q의 파라미터를 x에 대한 함수로 한다. 이렇게 설정하고 ELBO를 구하면 x가 달라질 때마다, q의 분포가 달라짐. (q의 모수인 평균 분산이 바뀌기 때문)

  2) q(z|x) = N(평균(x),분산(x))

  따라서, encoder는 x를 받아서 z의 평균, 분산을 만들어내는 두개의 뉴럴 네트워크를 포함하여 복잡한 데이터에 대해 적절한 모델을 적용할 수 있다. 추가로, z를 생성하는 과정을 설명하면, zero-mean Gaussian에서 노이즈를 하나 뽑아 평균 분산을 더하고 곱하여 z를 샘플링한다. 주의할 점은 데이터에서 직접 샘플링 하는 것이 아니라 노이즈를 샘플링 하기 때문에 동일한 데이터 x가 들어가더라도 얼마든지 다른 z가 나올 수 있다. (그래서 variational이 붙었다고 한다.)

- **Adversarial Autoencoder**



Revisit Deep Neural Networks

Applications

