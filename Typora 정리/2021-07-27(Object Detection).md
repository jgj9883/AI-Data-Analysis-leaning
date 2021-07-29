### classification

![image-20210727122407327](C:\Users\USER\Desktop\code\Practice\image\image-20210727122407327.png)

이미지를 다루는 분야의 Deep Leaning 에서 분류 (classification)이란, 입력으로 주어진 이미지 안의 객체 Object 의 종류(이는 Class, Label 혹은 Class Label 이라고 불린다. )를 구분하는 행위이다. 

예를 들어 MNIST data set의 경우 0부터 9까지 총 10개의 숫자들을 각각의 class로 구별하며 임의의 숫자 한 개의 이미지 입력에 대하여 학습된 딥러닝 모델은 입력된 이미지의 class가 0부터 9까지의 숫자 중 어떤 숫자인지 분류하여 출력하게 된다. 

이미지의 첫번째 경우 입력된 고양이 이미지에 대해 모델이 "입력된 이미지의 class는 CAT" 이라는 출력을 한 셈이다.





### localization

![image-20210727122342071](C:\Users\USER\Desktop\code\Practice\image\image-20210727122342071.png)

다음 이미지 같이 모델이 주어진 이미지 안의 Object가 이미지 안의 어느 위치에 있는지 위치 정보를 출력해주는 것으로, 주로 Bounding box의 꼭지점 pixel 좌표가 출력되는 것이 아닌 left top, 혹은 right bottom 좌표를 출력한다.

![image-20210727121933490](C:\Users\USER\Desktop\code\Practice\image\image-20210727121748766.png)

- 위와 같이 이미지가 주어졌을 때, 이미지를 car라고 분류하는 것을 'Image classification' 이라고 한다.
- 이 때, car가 이미지 속에 어디에 있는지까지 알아내는 것을 'Classification with localization' 이라고 한다.
- localization을 사용해, 이미지에서 하나의 객체가 아닌 여러 객체를 인식하는 것을 'Detection' 이라고 한다. 



### Object Detection

![image-20210727123009757](C:\Users\USER\Desktop\code\Practice\image\image-20210727123009757.png)

보편적으로 Classification과 Localization이 동시에 수행되는 것을 의미한다. 

모델의 학습 목적에 따라서 특정 Object만 Detection 하는 경우도 있고 ( 이 경우 학습시 검출하고자 하는 Object에 대한 학습정보만 입력함), 여러개의 객체를 검출하는 Multi object detection 모델을 만들기도 한다. 

종종 Object detection은 localization의 의미로만 사용되는 경우도 있다. 이 경우는 이미지 위에 모델이 학습한 object 위치만 bounding box로 표현되고 class 종류는 구분하지 않는 경우다.





### semantic segmentation 

Segmentation이란, Image를 Pixel단위로 구분해 각 Pixel이 어떤 물체 class인지 구분하는 문제다.

![image-20210727134541115](C:\Users\USER\Desktop\code\Practice\image\image-20210727134541115.png)



Segmentation은 두가지로 나뉜다. Semantic Segmentation과 Instance Segmentation 로 구분되는데  Semantic Segmentation은 pixel 단위로 물체를 구분한뒤 각각의 물체가 어떤 class인지만 구분 하는 문제고, Instance Segmentation이란 같은 class이더라도 다른 것이라면 구분하는 문제라 할 수 있다.

Semantic Segmentation이란 단순하게 bounding box 등을 이용하여 검출할 대상을 나타내는 것이 아니라, 보통은 픽셀 단위의 예측을 수행하며 의미 있는 단위로  대상을 분리해낸다. 

영상속에 무엇이 있는지를 확인하는 것 뿐만 아니라 어느 위치에 있는지 location까지 정확하게 파악 해야한다. 하지만 semantic과 location은 그 성질상 지향하는 바가 다르기 때문에 이것을 조화롭게 해결해야 segmantic segmentation의 성능이 올라간다.

![image-20210727142831467](C:\Users\USER\Desktop\code\Practice\image\image-20210727142831467.png)![image-20210727145051637](C:\Users\USER\Desktop\code\Practice\image\image-20210727145051637.png)

즉, Semantic segmentation은 같은 class인 object들은 같은 영역 혹은 색으로 분할하는 것이다.

- 각 픽셀별로 어떤 class에 속하는지 label을 구해줘야 한다.

  ![image-20210727143652213](C:\Users\USER\Desktop\code\Practice\image\image-20210727143652213.png)

  따라서 One-Hot encoding으로 각 class에 대해 class개수만큼 출력채널을 만든다.

  그 후 argmax를 통해 위 이미지처럼 하나의 output을 계산한다.

![image-20210727143754961](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210727143754961.png)



이렇게 semantic segmentation은 각 pixel들이 각 class에 대해 binary하게 포함되는지 안되는지 여부를 따진다.

예시로, 강아지 output channel에서는 각 pixel들에 대해 강아지에 포함되는 pixel인지 아닌지, 사람 output channel에서는 각 pixel들이 사람에 포함되는 pixel인지 아닌지, ..0과 1로 binary하게 값을 갖는다.



1. FCN
   - Fully Convolutional Network의 약자로, FC Layer 대신 1x1 Convolution layer를 사용한다.
   - 모든 Network를 Convolution layer만 사용함으로써 input size의 제한을 받지 않고, 위치정보를 보존할 수 있게 되었다. 
   - ![image-20210727135948830](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210727135948830.png)
     - Feature를 추출하는 Convolution 단계
     - 뽑아낸 feature에 대해 pixelwise prediction 단계
     - classification을 한뒤 각 원래의 크기로 만들기 위한 Upsampling 단계
   - 이러한 단계를 거친 후 각 pixel에 class 따라 색칠을 한 뒤 Segmentation 결과를 보여준다. 



### instance segmentation



![image-20210727143402629](C:\Users\USER\Desktop\code\Practice\image\image-20210727143402629.png)![image-20210727145121319](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210727145121319.png)

instance segmentation은 같은 class이여도 서로 다른 instance로 구분해주는 것이다. 즉, pixel 별로object가 있는지 없는지 여부만 계산한다. 일반적으로 Mask R-CNN과 같은2-stage detector에서는 먼저 object들을 bounding box를 통해 localization시킨다. 그후 위에서 class별로 output 채널을 만든 것과 같이 localize된 ROI마다 class의 개수만큼 binary mask(instance인지 아닌지) 마스크를 씌워준다.

semantic segmantation과 다르게 이미지 사이즈 크기로 class 개수만큼 output 채널이 존재하지 않고 RoI별로 class 개수만큼 output 채널이 존재하고 동일 class더라도 서로 다른 instance, 즉 RoI가 focus하는 instance부분만 value를 갖도록 한다.

1. **Mask R-CNN**

   - faster R-CNN RPN 에서 결과로 나온 bounded box proposal을 이용해서 RoI pooling 이라는 방법을 사용한다. 기존의 RoI pooling은 정수 좌표밖에 지원하지 않았다. 

   - Mask R-CNN 에서는 RoIAlign 이라는 새로운 pooling layer을 제안하는데, interpolation(보간)을 통해서 소수점 픽셀 레벨의 풀링을 지원한다. 그러므로써 좀 더 정교한 feature를 뽑을 수 있게 되어 뒷단의 성능 증가로 이어지게 된다.

     ![image-20210727151106185](C:\Users\USER\Desktop\code\Practice\image\image-20210727151106185.png)

   - 기존의 faster R-CNN에서는 pooling 된 feature 위에 올라가 있던 classification 과 box regression head가 두개 있다. 

   - Mask R-CNN은 기존의 head 옆에 mask branch 하나가 더 있다. 

     - upsampling을 통해서 각 클래스별로 binary mask를 예측하도록 하는 구조를 가지고 있다.
     - semantic sementation map과 동일 , 하나의 bounding box에 대해서 일괄적으로 모든 클래스에 대한 마스크를 일단 생성한다, 그 다음에 classification head 에서 클래스를 예측하는 결과를 이용해서 어떤 마스크를 선택할지 참조한다.
     - ![image-20210727151729294](C:\Users\USER\Desktop\code\Practice\image\image-20210727151729294.png)

   

   

   N x N 사이즈의 input 이미지가 주어졌을때 **Mask R-CNN의 과정**은 다음과 같다.

   1.  **800 ~ 1024 사이즈로 이미지를 resize한다. (bilinear interpolation)**
   2. **Backbone network의 input으로 들어가기 위해 1024 x 1024의 input size로 맞춘다. (padding)**
   3. **ResNet-101을 통해 각 layer(stage)에서 feature map (C1, C2, C3, C4, C5)를 생성한다.**
   4. **FPN을 통해 이전에 생성된 feature map에서 P2, P3, P4, P5, P6 feature map을 생성한다.**
   5. **최종 생성된 feature map에 각각 RPN을 적용하여 classification, bbox regression output값을 도출한다.**
   6. **output으로 얻은 bbox regression값을 원래 이미지로 projection시켜서 anchor box를 생성한다.**
   7. **Non-max-suppression을 통해 생성된 anchor box 중 score가 가장 높은 anchor box를 제외하고 모두 삭제한다.**
   8. **각각 크기가 서로다른 anchor box들을 RoI align을 통해 size를 맞춰준다.**
   9. **Fast R-CNN에서의 classification, bbox regression branch와 더불어 mask branch에 anchor box값을 통과시킨다.**

   ![image-20210727181430038](C:\Users\USER\Desktop\code\Practice\image\image-20210727181430038.png)

   

   즉, Fast R-CNN의 classification, localization(bounding box regression) branch에 새롭게 mask branch가 추가됐다.

   RPN 전에 FPN(feature pyramid network)가 추가됐다.

   Image segmentation의 masking을 위해 RoI align이 RoI pooling을 대신하게 됐다.

   

   

   

2. summary of the R-CNN family

   ![image-20210727151751890](C:\Users\USER\Desktop\code\Practice\image\image-20210727151751890.png)

3. YOLACAT (You Only Look At CoefficientTs)

   ![image-20210727152300871](C:\Users\USER\Desktop\code\Practice\image\image-20210727152300871.png)

   - single-stage network

   - 기본 backbone 구조는 feature pyramid 구조를 사용한다. (고해상도 feature map을 가지고 사용할 수 있다.)

     ![image-20210727152921049](C:\Users\USER\Desktop\code\Practice\image\image-20210727152921049.png)

   - 가장 큰 특징은 마스크의 프로토타입을 추출해서 사용한다.

   - 마스크는 아니지만 추후에 마스크로 합성될 수 있는 기본적인 여러 물체의 soft segmentation component 들을 생성한다.

     ![image-20210727152959048](C:\Users\USER\Desktop\code\Practice\image\image-20210727152959048.png)

   - prediction head에서 각 detection에 대해서 프로토타입들을 잘 합성하기 위한 coefficient들을 출력한다.

   - 이 cofficient과 프로토타입을 선형 결합을 해주므로써 각 detection에 적합한 mask response map을 생성한다.

   - 마스크를 효율적으로 생성하기 위해서 프로토타입 갯수를 object(class) 갯수하고 상관없이 적당하게 작게 설정하는 대신에 그것을 선형 결합으로 다양한 마스크를 생성하는 것이 핵심이다

4. YolactEdge (2020)
   - 이전 frame 중에서 key frame에 해당하는 frame의 feature를 다음 frame의 전달을 해서 특징 map의 계산량을 획기적으로 줄인다
   - feature를 전달해서 속도적인 측면에서는 개선을 했지만 실제로 비디오에 따라서 독립적으로 processing이 되는 구조이기 때문에 아직까지는 mask의 한계점들이 존재한다.



DeepMask, FCIS, SOTA 모델 

### panoptic segmentation

기존의 instance segmentation은 배경에 관심이 없고 그저 움직이는 작은 물체들에 대해서 segmentation을 수행하는데

panoptic segmentation은 배경정보 뿐만 아니라 관심을 가질만한 물체들의 instance까지도 구분해서 segmentation을 수행한다.