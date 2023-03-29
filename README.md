# Dört İşlem Oyunu

## Proje Hakkında
Oyunun amacı, 5 tek haneli sayı, 1 iki haneli sayı (onun katları olan sayı)
ve dört işlem kullanılarak üç haneli sayıyı yada ona ek yakın sayıyı
bulmaktır. Bu yazılım, üniversitemin Yazılım Yapımı dersi için sınıf
çalışması olarak geliştirilmiştir. Proje, Python ile geliştirilmiştir.

## Oyunun Yapısı

### Sayıları Belirleme
Yazılım, işlem yapılacak olan sayıları rastgele olarak oluşturmaktadır.
Yazılım, ilk olarak beşi tek haneli sayı, bir tanesi iki haneli ve onun
katı olan sayı olmak üzere rastgele sayılar oluşturur. Daha sonrasında
yazılım, oyuncunun hedefleyeceği üç haneli sayıyı bulmaya çalışır.
Bunun için, maksimum dört kereye mahsus olmak üzere, rastgele üretilen bu
sayıları rastgele işlemlere tabii tutar. Bu sayıyı üretmek için yazılım,
önceki işlemlerin sonuçlarını da yeni işlemlerde kullanabilir.
En sonunda yazılım, oluşturduğu sayılarla birlikte bu sayıyı kaç aşamada
oluşturduğunun bilgisini tutar.

### Sayıyı Dört İşlemle Oluşturma
Oyun, her turun başında yazılım, terminale kullanıcının kullanabileceği
sayıları, kaçıncı turda olduğu bilgisini ve son işlemin sonucunu yazdırır.
Daha sonrasında yazılım, kullanıcıdan verilen liste içerisinden iki sayı
seçmesini talep eder. Ardından yazılım, kullanıcıya bu iki sayı ile dört
işlemden hangisini yapmak istediğini sorar. Bu aşamada kullanıcı, sayıları
tekrardan seçmek için önceki menüye `"q"` girerek dönebilir. Eğer
dört işlemden birisi seçilirse verilen bilgiler ışığında yazılım, sonucu
hesaplayarak belleğe kaydeder. Eğer bulunan sayı ile hedeflenen
sayı arasında fark yeterince küçükse oyuncu, sayı girişi istendiği
anda `"q"` girerek oyunu bitirebilir.

### Puanın Hesaplanması
Oyun puanının hesaplanmasının belirli bir algoritması vardır.
Öncelikle en son işlem sonucu, eğer tam sayı değilse tam sayıya dönüştürülür.

Yazılım, ilk olarak temel puanı hesaplar. Temel puan $p_b$, hedef sayı $n_t$
ve hesaplanan sayı $n_c$ olmak üzere şu şekilde hesaplanır:

$$
p_b =
\begin{dcases}
0 && \text{if} && |n_t - n_c| > 9 \\
10 - |n_t - n_c| && \text{if} && |n_t - n_c| \leq 9
\end{dcases}
$$

Yazılım, bir puan çarpanı hesaplar. Puan çarpanı, kullanıcının sayıya daha
erken yaklaşmasını ödüllendirmek için var olan bir parametredir.
Puan çarpanı $k$, yazılımın üç basamaklı sayıyı oluşturmak için kullandığı
işlem sayısı $s_t$ ve kullanıcının sonucu bulmak için kullandığı işlem sayısı
$s_c$ olmak üzere şu şekilde hesaplanır:

$$
k = \max(0, s_t - s_c + 3)
$$

Son olarak, final puanı ($p_f$) bulmak için temel puan $p_b$ ve puan çarpanı
$k$ olmak üzere aşağıdaki formül uygulanır:

$$
p_f = p_b + 2 \cdot k
$$

Son olarak final puanı terminale yazdırılır ve oyun biter.

## Yazılımı Kullanmak

Yazılımı kullanmadan önce `git` ile projenin klonlanması gerekmektedir.

```bash
$ git clone https://github.com/berkakkaya/four-operations-game
$ cd four-operations-game/
```

Daha sonrasında, yazılımı `python` komutu ile şu şekilde
çalıştırabilirsiniz:

```bash
$ python main.py
```

Kullandığınız işletim sistemine göre, `python` komutu sisteminizde
`python3` olarak da tanımlı olabilir. O yüzden ilk komut çalışmazsa,
`python` kısmını `python3` ile değiştirip yeniden deneyin.
