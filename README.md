# Combat-drone
Savaşan İnsansız Hava Aracı için Hedef Takip Sistemi

<img height="350" src="/images/combot-drone.jpg"/>

### 1. Veri Seti Hazırlama

Hazır veri setleri yetersiz olduğundan youtube videolarından veri seti toplayacağız. 

* Youtube videosu indirmek için:`https://tr.savefrom.net/1-how-to-download-youtube-video.html`
* Video üzerindeki kare görüntüleri indirmek için:`split-videos-to-frames.py` "split-videos-to-frames.py" dosyasını düzeneleyip çalıştıracağız.
* Veri setindeki resimleri belli bir boyuta indirmek için: image_resize.py dosyasını düzeneleyip çalıştıracağız.<br/>

Yüksek doğruluk oranı elde etmek için, yüksek kaliteli resimler bulmalıyız. Bunun için HD kalitede çekilmiş İnsansız Hava Araçlar videolarını bulmalıyız. Bunu daha iyi anlamak için bir akademik makaleyi okumanızı tavsiye ederim.

- [Understanding How Image Quality Affects Deep
Neural Networks[1]](https://arxiv.org/pdf/1604.04004.pdf)<br/>
Veri seti için oluşturmak için kullandığımız video kanalı:<br/>

- https://www.youtube.com/channel/UCUbR76-7gPBX7MR5nTEDbCA
<img height="150" src="/images/mhavkfpv.png"/>

Toplam 20 video üzerinden esimler indirip etiketleme yapacağım. Veri etiketleme için makesense.ai sitesini kullanacağız. Veri setlerinin boyutu fazla olduğundan dolayı örnek olması açısından 50 etiketli resim paylaşacağım.

#### Örnek Veri Etiketleme:

<img height="200" src="/images/makesense.png"/>

### Yolov4-tiny ile Eğitim

1000 etiketli veri setini yolov4-tiny modelindeki test sonuçları:

<img src="/videos/uav.gif"/>
<img height="500" src="/images/chart.png"/>
Eğitim sonuçlarının yüksek çıkmasının sebebi benzer resimlerin çok olmasından kaynaklı. Farklı bir İHA modeli gördüğünde tanımakta zorlanacaktır. Bu yüzden farklı İHA videolarından resim çekip modelimizi güçlendireceğiz.

Yolov4-tiny ile Eğitim: 20.02.2021 tarihinde yayınlanacaktır.

### Sonuç ve Değerlendirme

Sonuç ve Değerlendirme: 07.03.2021 tarihinde yayınlanacaktır.

##### Proje halen devam etmektedir.

### TODO
* [x] Yakında eklenecek.
* [ ] Yakında eklenecek.
* [ ] Yakında eklenecek.
* [ ] Yakında eklenecek.
* [ ] Yakında eklenecek.
* [ ] Yakında eklenecek.
* [ ] Mosaic data augmentation
* [ ] Mish activation
* [ ] yolov4 tflite version
* [ ] yolov4 in8 tflite version for mobile


Kaynaklar:

[1] : https://arxiv.org/pdf/1604.04004.pdf
