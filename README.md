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

Veri seti için oluşturmak için kullandığımız videolar:<br/>

1. https://www.youtube.com/watch?v=nRTuh-CvZyI&list=UUUbR76-7gPBX7MR5nTEDbCA&index=2 [1080p]
2. https://www.youtube.com/watch?v=eC3An2zrEvA&list=UUUbR76-7gPBX7MR5nTEDbCA&index=5 [720p]
3. https://www.youtube.com/watch?v=z4RWVn7punk&list=UUUbR76-7gPBX7MR5nTEDbCA&index=7 [1080p]
4. https://www.youtube.com/watch?v=-MfdxbI5Ct0&list=UUUbR76-7gPBX7MR5nTEDbCA&index=9 [1440p]
5. https://www.youtube.com/watch?v=_p4eMDZ5vlY&list=UUUbR76-7gPBX7MR5nTEDbCA&index=10 [1440p] [Farklı bir iha türü]
6. https://www.youtube.com/watch?v=Tmb_-CaF86M&list=UUUbR76-7gPBX7MR5nTEDbCA&index=12 [1440p]
7. https://www.youtube.com/watch?v=5K7h9TASOHw&list=UUUbR76-7gPBX7MR5nTEDbCA&index=20 [720p]
8. https://www.youtube.com/watch?v=6-5IJg6E93o&list=UUUbR76-7gPBX7MR5nTEDbCA&index=25 [720p]
9. https://www.youtube.com/watch?v=zmIH-4zc70k&list=UUUbR76-7gPBX7MR5nTEDbCA&index=28 [720p]
10. https://www.youtube.com/watch?v=a8YrKYS9-zU&list=UUUbR76-7gPBX7MR5nTEDbCA&index=37 [1080p]
11. https://www.youtube.com/watch?v=a3gTVn9ItvM&list=UUUbR76-7gPBX7MR5nTEDbCA&index=38 [720p]
12. https://www.youtube.com/watch?v=VMkRVDmvUA0&list=UUUbR76-7gPBX7MR5nTEDbCA&index=39 [1080p]
13. https://www.youtube.com/watch?v=DDn4DialMmo&list=UUUbR76-7gPBX7MR5nTEDbCA&index=43 [1080p]
14. https://www.youtube.com/watch?v=MMD6m3Dla6E&list=UUUbR76-7gPBX7MR5nTEDbCA&index=46 [720p]
15. https://www.youtube.com/watch?v=6ghvve-Q-Ko&list=UUUbR76-7gPBX7MR5nTEDbCA&index=68 [1080p]
16. https://www.youtube.com/watch?v=C-m-rqg0edg&list=UUUbR76-7gPBX7MR5nTEDbCA&index=71
17. https://www.youtube.com/watch?v=kJEUxpVgHws&list=UUUbR76-7gPBX7MR5nTEDbCA&index=74

İlk denemeler de sadece 4 video üzerinde resimler indirip etiketleme yapacağım. Veri etiketleme için makesense.ai sitesini kullanacağız. Veri setlerinin boyutu fazla olduğundan dolayı örnek olması açısından 50 resim paylaşacağım.

#### Örnek Veri Etiketleme:

<img src="/images/makesense.png"/>


### 2. Veri Setini Düzenleme

Veri Setini Düzenleme 15.02.2021 tarihinde yayınlanacaktır.

### 3. Veri Artırma Yöntemleri

Veri Artırma Yöntemleri 15.02.2021 tarihinde yayınlanacaktır.

### 4. Veri Setinin Boyutunu İndirme

Veri Setinin Boyutunu İndirme: 28.02.2021 tarihinde yayınlanacaktır.

### 5. Yolov4-tiny Modeli Parametleri

Yolov4-tiny Modeli Parametleri: 01.02.2021 tarihinde yayınlanacaktır.


### 6. Hareketli Nesne Tespit Algoritmaları

Hareketli Nesne Tespit Algoritmaları: 15.03.2021 tarihinde yayınlanacaktır.


### 7. Yolov4-tiny ile Eğitim

Yolov4-tiny ile Eğitim: 20.02.2021 tarihinde yayınlanacaktır.


### 8. Yolov4-tiny + Deep Sort

 Yolov4-tiny + Deep Sort: 28.02.2021 tarihinde yayınlanacaktır.

### 9. Fps Düşürme Algoritmaları


Fps Düşürme Algoritmaları: 02.03.2021 tarihinde yayınlanacaktır.

### 10. Sonuç ve Değerlendirme

Sonuç ve Değerlendirme: 07.03.2021 tarihinde yayınlanacaktır.

##### Proje 13.03.2021 tarihinde tamanlanacaktır.

Kaynaklar:

[1] : https://arxiv.org/pdf/1604.04004.pdf
