<img src="https://te.legra.ph/file/be559ace3fe2b387dec9a.jpg" align="right" width="200" height="200"/>

# Dejavu Music Bot <img src="https://img.shields.io/github/v/release/DegGixM/DejavuMusicBot?color=black&logo=github&logoColor=black&style=social" alt="AZAD ET">

[Dejavu Music Bot](https://github.com/DegGixM/DejavuMusicBot) Pyrogram və Py-Tgcalls-dan istifadə edərək Python dilində yazılmış Güclü Telegram Musiqi+Video Botdur, onun vasitəsilə müxtəlif mənbələr vasitəsilə qrup zənglərinizdə mahnıları, videoları və hətta canlı yayımları yayımlaya bilərsiniz.

* Youtube, Soundcloud, Apple Music, Spotify, Resso və Telegram Audios & Videos dəstəyi.
* Sıfırdan yazılmışdır, onu sabit və daha az qəza edir.
* Cəlbedici miniatürlər, şriftlər və şəkillər, təcrübəni daha istifadəçi dostu və interaktiv edir.
* Döngə, Axtar, Qarışıq, Xüsusi Skip, Pleylistlər və s. dəstəyi
* Qlobal, İstifadəçilər, Söhbətlər Top 10 ifa olunan trek statistikası
* Çoxdilli dəstək


# 🔗 Ümumi Baxış

Yukki Music Bot-un yüksək səviyyəli qısa icmalı:

Bu layihə [Pyrogram](https://github.com/pyrogram) və [Py-Tgcalls](https://github.com/pytgcalls/pytgcalls) əsasındadır. Pyrogram müasir, zərif və asinxron MTProto API çərçivəsidir.

* Verilənlər bazası üçün Yukki məlumat və açarları saxlamaq üçün MongoDB-dən istifadə edir. [MongoDB](https://www.mongodb.com/) sizə lazım olan sorğu və indeksləşdirmə ilə istədiyiniz genişlənmə və çevikliyə malik sənəd verilənlər bazasıdır.
* Layihə bir çox platforma təfərrüatlarını əldə etmək üçün bs4 veb sökülməsindən istifadə edir. [Gözəl Şorba](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) HTML və XML fayllarından məlumatları çıxarmaq üçün Python kitabxanasıdır.
* Layihə miniatürlər üçün əsas şrift kimi [`Raleway`](../assets/font2.ttf) şriftindən istifadə edir.
* Layihələr [assets](../assets/) kataloqunda əldə edə biləcəyiniz cəlbedici şəkillər və nişanlardan istifadə edir.

Dejavu Music Bot-u gücləndirən texnologiyalar haqqında ətraflı məlumat üçün [Sənədlər]-ə baxın (https://notreallyshikhar.gitbook.io/yukkimusicbot/).


# ⚡️ Başlanır

### Dejavu Music Bot-u yerləşdirməzdən əvvəl [bütün mövcud konfiqurasiya variantlarına](../config/README.md) nəzər salın, həmçinin [bütün mövcud əmrləri](../strings/command.yml) yoxlayın. layihə.

> Əgər siz Yukki Music Bot ilə işləməyə başlamaq istəyirsinizsə, repo yükləyə və ya idxal edə bilərsiniz.
> Rəsmi [sənəd saytı](https://te.legra.ph/file/be559ace3fe2b387dec9a.jpg) çoxlu məlumat ehtiva edir. Başlamaq üçün ən yaxşı yer yerləşdirmə bölməsindəndir.
> Bizimlə danışmaq istəyirsinizsə, [Telegram Qrupumuzda] bizə qoşulun (https://t.me/DejavuGurup)


## 🖇 İlkin şərtlər

> Layihənizdə ziddiyyətlərin qarşısını almaq üçün sizdə olmalıdır/quraşdırılmalıdır

- [Python3.9](https://www.python.org/downloads/release/python-390/)
- [Telegram API Açarı](https://docs.pyrogram.org/intro/setup#api-keys)
- [Telegram Bot Token](https://t.me/botfather)
- [MongoDB URI](https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb)
- [Pyrogram String Session](https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/string-session)


## 🖇 Piroqqramma sim seansının yaradılması

- [Replit] (https://replit.com/@NotReallyShikhar/Yukki-Music-String-Gen) vasitəsilə Piroqram Simli Sessiya yaradın

- [Telegram String Generation Bot] (https://t.me/YukkiStringBot) vasitəsilə Piroqram Simli Sessiya yaradın


## 🚀 Heroku Yerləşdirmə

<h4> Dejavu-ni Heroku-da yerləşdirmək üçün aşağıdakı düyməyə klikləyin! </h4>    
<a href="https://heroku.com/deploy/"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=https://github.com/DegGixM/DejavuMusicBot=heroku" width="200""/></a>

> Heroku Deployment haqqında ətraflı izahat istəyirsiniz? [Click Here](https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/heroku)

## 🚀 Okteto Yerləşdirmə

<h4>Yukki-ni Okteto-da yerləşdirmək üçün aşağıdakı düyməyə klikləyin!</h4>
<a href="https://cloud.okteto.com/deploy?repository=https://github.com/TeamYukki/YukkiMusicBot"><img src="https://img.shields.io/badge/Deploy%20To%20Okteto-informational?style=for-the-badge&logo=Okteto" width="200""/></a>



## 🖇 VPS Yerləşdirmə

> VPS Yerləşdirməsi üzrə Ətraflı İzahat üçün [Sənədləri](https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/local-hosting-or-vps) yoxlayın.


```console
shikhar@MacBook~ $ git clone https://github.com/TeamYukki/YukkiMusicBot
shikhar@MacBook~ $ cd YukkiMusicBot
shikhar@MacBook~ $ sudo bash setup
```
> Quraşdırma hər bir tələbi, nodejs və pip paketlərini avtomatik quraşdıracaq. Tələbləri uğurla quraşdırdıqdan sonra quraşdırma sizdən parametrlərinizi daxil etməyi xahiş edəcək.
> Variantlarınızı düzgün daxil edin.

```console
shikhar@MacBook~ $ bash start
```

> VPS Metodunu Almırsınız? [Təlimçiliyə baxın](https://t.me/DejavuSupport)


<img src="https://telegra.ph/file/6b75b57da50ef1183fcdc.jpg" align="center">

## 🏷 Dəstək

Aşağıdakı yerlərdən birində baxıcı ilə əlaqə saxlayın:

- [GitHub Problemləri](https://github.com/TeamYukki/yukkimusicbot/issues/new?assignees=&labels=question&template=SUPPORT_QUESTION.md&title=support%3A+)
- [bu GitHub profilində] sadalanan əlaqə seçimləri(https://github.com/TeamYukki)
- [Telegram Dəstəyi](https://t.me/DejavuSupport)

## 🎗 Layihəyə yardım

**təşəkkür edirəm** demək və/və ya YukkiMusicBot-un aktiv inkişafına dəstək vermək istəyirsinizsə:

- Layihəyə [GitHub Star](https://github.com/DegGixM/DejavuMusicBot) əlavə edin.
- Repo çəngəl :)
- [Dev.to](https://dev.to/), [Medium](https://medium.com/) və ya şəxsi bloqunuzda layihə haqqında maraqlı məqalələr yazın.

P.S: Siz də mənə qəhvə ala bilərsiniz :)
<p><a href="https://www.buymeacoffee.com/notreallysy" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png " alt="Mənə Qəhvə Al" style="height: 35px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box- kölgə: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !vacib;" >></a></p>

Biz birlikdə YukkiMusicBot-u **daha yaxşı** edə bilərik!

## ✍🏻 Töhfə

Əvvəlcə, töhfə vermək üçün vaxt ayırdığınız üçün təşəkkür edirik! Töhfələr açıq mənbə icmasını öyrənmək, ruhlandırmaq və yaratmaq üçün heyrətamiz bir yerə çevirən şeydir. Etdiyiniz hər hansı töhfə hamıya fayda verəcək və **çox təqdirəlayiqdir**.

Lütfən, [töhfə təlimatlarımızı](CONTRIBUTING.md) oxuyun və iştirak etdiyiniz üçün təşəkkür edirik!

## 👨🏻‍💻 Müəlliflər və töhfə verənlər

Bu deponun orijinal quraşdırılması [Dejavu](https://t.me/DejavuSupport) tərəfindəndir.

Bütün müəlliflərin və töhfə verənlərin tam siyahısı üçün [əməkdaşlar səhifəsinə](https://github.com/TeamYukki/YukkiMusicBot/contributors) baxın.

## ⚠️ Təhlükəsizlik

YukkiMusicBot yaxşı təhlükəsizlik təcrübələrini izləyir, lakin 100% təhlükəsizlik təmin edilə bilməz. YukkiMusicBot heç bir **zəmanət** olmadan **"olduğu kimi"** təmin edilir. Öz riskinizlə istifadə edin.

Ətraflı məlumat və təhlükəsizlik problemlərini bildirmək üçün [`SECURITY.md`](SECURITY.md) ünvanımıza müraciət edin.


## 🗂 Lisenziya

Bu layihə **GNU General Public License v3** əsasında lisenziyalaşdırılıb. Bütün dizaynlar [ MUCVE ](https://t.me/MUCVE_M) tərəfindən yaradılmışdır.

Ətraflı məlumat üçün [LICENSE](../LICENSE) baxın.

## 📑 Təşəkkür

Yukki Music Bot-u gücləndirməyə kömək edən bu heyrətamiz layihələrə/insanlara xüsusi təşəkkürlər:

- [Pirogram](https://github.com/pyrogram/pyrogram)
- [Py-Tgcalls](https://github.com/pytgcalls/pytgcalls)
- [CallsMusic Team](https://github.com/Callsmusic)
- [TheHamkerCat](https://github.com/TheHamkerCat)
- [Charon Links](https://github.com/XCBv021)


Xatırla ki, sən böyüksən, kifayətsən, varlığın qiymətlidir. Psixi sağlamlığınızla mübarizə aparırsınızsa, lütfən, sevdiyiniz biri ilə əlaqə saxlayın və bir mütəxəssislə məsləhətləşin.
