# Combat-drone
Savaşan İnsansız Hava Aracı için Hedef Takip Sistemi

<img height="200" src="/images/combot-drone.jpg"/>

### 1. Veri Seti Hazırlama

Hazır veri setleri yetersiz olduğundan youtube videolarından veri seti toplayacağız. Açık kaynak İnsansız Sabit Kanat Arac veri seti bulmak zor olduğundan dolayı kendii veri setimizi toplayıp bunu halka açık halinden paylaşmayı hedeflemekteyiz. Bu hedefi başka repoda gerçekleştirmekteyim. 

- [Açık Kaynak İnsansız Hava Araç Veri Seti[1]](https://github.com/kadirnar/uav-datasets)<br/>

* Youtube videosu indirmek için:`https://tr.savefrom.net/1-how-to-download-youtube-video.html`
* Video üzerindeki kare görüntüleri indirmek için:`split-videos-to-frames.py` "split-videos-to-frames.py" dosyasını düzeneleyip çalıştıracağız.
* Veri setindeki resimleri belli bir boyuta indirmek için: image_resize.py dosyasını düzeneleyip çalıştıracağız.<br/>

Yüksek doğruluk oranı elde etmek için, yüksek kaliteli resimler bulmalıyız. Bunun için HD kalitede çekilmiş İnsansız Hava Araçlar videolarını bulmalıyız. Bunu daha iyi anlamak için bir akademik makaleyi okumanızı tavsiye ederim.

- [Understanding How Image Quality Affects Deep
Neural Networks[2]](https://arxiv.org/pdf/1604.04004.pdf)<br/>
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

### Yapılacaklar Listesi:
* [ ] Yolov4, Yolov4x-Mish, Yolov4-Csp ve Yolov5-Pytorch ile Eğitim ve Test.
* [ ] Yolov4, Yolov4x-Mish, Yolov4-Csp ve Yolov5-Pytorch  modellerinin Karşılaştırılması.
* [ ] Test ettiği resimlerden kordinat ve nesne bilgisini .txt dosyasına yazdırma.
* [ ] Opencv Kullanarak Yolo Modellerini Test.
* [ ] Yolo modelini TF2-YOLO ve Yolov4-TensorRT modeline çevirme.
* [ ] Projeyi Script Haline Getirme.


Kaynaklar:

[1] : https://github.com/kadirnar/uav-datasets
[2] : https://arxiv.org/pdf/1604.04004.pdf


## Soru & Cevap

Dokümanlar, kaynak kodlar veya her hangi bir konuda ki sorularınızı **issues** bölümünü kullanarak sorabilirsiniz (new issues). Soru cevaplamak veya daha öncekilere göz atmak isterseniz yine bu bölümü kullanabilirsiniz.

**Nasıl Soru Sorulur?**

Öncelikle [issues](github.com/kadirnar/combat-drone/issues) bölümüne gidiniz. Sayfanın sağında yer alan **new issues** butonuna tıklayın. Açılan ilgili bölüme sorunuzu veya talebinizi açıklayıcı bir şekilde yazarak **Submit new issues** butonu aracılığıyla kaydedin.

## Lisans

Bu proje içerisinde yer alan doküman ve kaynak kodlar [MIT Lisansı](/LICENSE) ile lisanslanmıştır. İçeriğin **kaynak gösterilmeden** kullanılması durumunda bu kişiler/kurumlar [bu bölümde](/other/blacklist.md) paylaşılacaktır.
