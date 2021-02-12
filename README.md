# Combat-drone
Savaşan İnsansız Hava Aracı için Hedef Takip Sistemi

<a href="" target="_blank"><img height="350" src="https://www.baykarsavunma.com/upload/sayfa/savasaniha.jpg"></a>

### 1. Veri Seti Hazırlama

Hazır veri setleri yetersiz olduğundan youtube videolarından veri seti toplayacağız. 

* Youtube videosu indirmek için: https://tr.savefrom.net/1-how-to-download-youtube-video.html
* Video üzerindeki kare görüntüleri indirmek için: "split-videos-to-frames.py" dosyasını düzeneleyip çalıştıracağız.
* Veri setindeki resimleri belli bir boyuta indirmek için: image_resize.py dosyasını düzeneleyip çalıştıracağız.<br/>

Yüksek doğruluk oranı elde etmek için, yüksek kaliteli resimler bulmalıyız. Bunun için HD kalitede çekilmiş İnsansız Hava Araçlar videolarını bulmalıyız. Bunu daha iyi anlamak için bir akademik makaleyi okumanızı tavsiye ederim.

- [Understanding How Image Quality Affects Deep
Neural Networks[1]](https://arxiv.org/pdf/1604.04004.pdf)

Veri seti için oluşturmak için kullandığımız video kanalı:<br/>

- https://www.youtube.com/channel/UCUbR76-7gPBX7MR5nTEDbCA

İlk denemeler de sadece 4 video üzerinde resimler indirip etiketleme yapacağım. Veri etiketleme için makesense.ai sitesini kullanacağız. Veri setlerinin boyutu fazla olduğundan dolayı örnek olması açısından 50 etiketli resim paylaşacağım.

#### Örnek Veri Etiketleme:

<img height="350" src="/images/makesense.png"/>

### 2. Veri Artırma Yöntemleri

Veri Artırma Yöntemleri 15.02.2021 tarihinde yayınlanacaktır.

### 3. Veri Setinin Boyutunu İndirme

Veri Setinin Boyutunu İndirme: 28.02.2021 tarihinde yayınlanacaktır.

### 4. Yolov4-tiny Modeli Parametleri

Yolov4-tiny Modeli Parametleri: 01.02.2021 tarihinde yayınlanacaktır.


### 5. Hareketli Nesne Tespit Algoritmaları

Hareketli Nesne Tespit Algoritmaları: 15.03.2021 tarihinde yayınlanacaktır.


### 6. Yolov4-tiny ile Eğitim

1000 etiketli veri setini yolov4-tiny modelindeki test sonuçları:

<img src="/videos/uav.gif"/>
<img height="600" src="/images/chart.png"/>
Eğitim sonuçlarının yüksek çıkmasının sebebi benzer resimlerin çok olmasından kaynaklı. Farklı bir İHA modeli gördüğünde tanımakta zorlanacaktır. Bu yüzden farklı İHA videolarından resim çekip modelimizi güçlendireceğiz.

Yolov4-tiny ile Eğitim: 20.02.2021 tarihinde yayınlanacaktır.


### 7. Yolov4-tiny + Deep Sort

 Yolov4-tiny + Deep Sort: 28.02.2021 tarihinde yayınlanacaktır.

### 8. Fps Düşürme Algoritmaları


Fps Düşürme Algoritmaları: 02.03.2021 tarihinde yayınlanacaktır.

### 9. Sonuç ve Değerlendirme

Sonuç ve Değerlendirme: 07.03.2021 tarihinde yayınlanacaktır.

##### Proje 13.03.2021 tarihinde tamanlanacaktır.

Kaynaklar:

[1] : https://arxiv.org/pdf/1604.04004.pdf
