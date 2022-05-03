#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """ ✅**<u>Admin Əmrləri:</u>**

**c** kanal oyunu deməkdir.

/pause və ya /cpause - Musiqinin ifasına fasilə verin.
/resume və ya /cresume - Pauza edilmiş musiqini davam etdirin.
/muse və ya /cmute - Musiqinin səsini söndürün.
/unmute və ya /cunmute - Səssiz musiqinin səsini açın.
/skip və ya /cskip- Hazırda ifa olunan musiqini keçin.
/stop və ya /cstop- Musiqinin ifasını dayandırın.
/shuffle və ya /cshuffle- Növbəyə qoyulmuş pleylistləri təsadüfi qarışdırır.
/seek və ya /cseek - Sonrakı Musiqini müddətə görə axtarın.
/seekback və ya /cseekback - Müddəti ilə musiqini axtarın.
/yenidən başladın - Söhbətiniz üçün botu yenidən başladın.


✅<u>**Xüsusi Atlama:**</u>
/skip və ya /cskip [Nömrə(misal: 3)]
    - Musiqini göstərilən növbəli nömrəyə keçir. Nümunə: /skip 3 musiqini üçüncü növbəli musiqiyə keçir və növbəti 1 və 2 musiqiyə məhəl qoymur.

✅<u>**Loop Play:**</u>
/loop və ya /clop [enable/disable] və ya [nömrə 1-10]
    - Aktivləşdirildikdə, bot səsli çatda səsləndirilən musiqini 1-10 dəfə çevirəcək. Varsayılan olaraq 10 dəfə.
    
✅<u>**Auth İstifadəçiləri:**</u>
Auth İstifadəçiləri söhbətinizdə admin hüquqları olmadan admin əmrlərindən istifadə edə bilərlər.

/auth [İstifadəçi adı] - Qrupun AUTH SİYAHISINA istifadəçi əlavə edin.
/unauth [İstifadəçi adı] - Qrupun AUTH LIST-dən istifadəçini çıxarın.
/authusers - Qrupun AUTH SİYAHISINI yoxlayın."""


HELP_2 = """✅<u>**Oynatma Əmrləri:**</u>

Mövcud Əmrlər = play , vplay , cplay

ForcePlay Əmrləri = playforce , vplayforce , cplayforce

**c** kanal oyunu deməkdir.
**v** video oynatma deməkdir.
**force** güc oyunu deməkdir.

/play və ya /vplay və ya /cplay - Bot verdiyiniz sorğunu səsli söhbətdə oynatmağa və ya səsli söhbətlərdə canlı bağlantıları yayımlamağa başlayacaq.

/playforce və ya /vplayforce və ya /cplayforce - **Force Play** səsli çatda cari ifa olunan treki dayandırır və növbəni pozmadan/təmizləmədən axtarılan treki dərhal ifa etməyə başlayır.

/channelplay [Söhbət istifadəçi adı və ya id] və ya [Disable] - Kanalı qrupa qoşun və qrupunuzdan kanalın səsli söhbətində musiqi yayımlayın.


✅**<u>Botun Server Pleylistləri:</u>**
/playlist - Serverlərdə Saxlanmış Pleylistinizi yoxlayın.
/deleteplaylist - Pleylistinizdə saxlanan hər hansı musiqini silin
/play - Serverlərdən Saxlanmış Pleylistinizi oynatmağa başlayın."""

HELP_3 = """✅<u>**Bot Əmrləri:**</u>

/stats - Top 10 Track Global Stats, Top 10 Bot Users, Top 10 Chats on the bot, Top 10 Played in Chat and s.

/sudolist - Yukki Musiqi Botunun Sudo İstifadəçilərini yoxlayın

/lyrics [Musiqi Adı] - Vebdə xüsusi Musiqi üçün Lirikləri axtarır.

/song [Track Adi] və ya [YT Link] - YouTube-dan mp3 və ya mp4 formatında istənilən treki yükləyin.

/player - İnteraktiv Oyun Paneli əldə edin.

**c** kanal oyunu deməkdir.

/queue və ya /cqueue- Musiqinin Növbə Siyahısını yoxlayın."""

HELP_4 = """✅<u>**Əlavə Əmrlər:**</u>
/start - Musiqi Botunu işə salın.
/ help - Əmrlərin ətraflı izahı ilə Əmrlər Köməkçisi Menyusunu əldə edin.
/ping- Botu pingləyin və Botun Ram, CPU və s. statistikasını yoxlayın.

✅<u>**Qrup Parametrləri:**</u>
/settings - Daxili düymələrlə tam qrup parametrlərini əldə edin.

🔗 **Parametrlərdəki seçimlər:**

1️⃣ Siz səsli söhbətdə yayımlamaq istədiyiniz **Audio Keyfiyyətini** təyin edə bilərsiniz.

2️⃣ Siz səsli söhbətdə yayımlamaq istədiyiniz **Video Keyfiyyətini** təyin edə bilərsiniz.

3️⃣ **Auth Users**:- Admin əmrləri rejimini buradan hamıya və ya yalnız adminlərə dəyişə bilərsiniz. Əgər hər kəs, sizin qrupunuzda olan hər kəs admin əmrlərindən istifadə edə biləcək (məsələn, /skip, /stop və s.)

4️⃣ **Təmiz rejimi:** Söhbətinizin təmiz və yaxşı qaldığından əmin olmaq üçün aktivləşdirildikdə botun mesajlarını 5 dəqiqədən sonra qrupunuzdan silir.
5️⃣**Təmizləmə əmri**: Aktivləşdirildikdə, Bot yerinə yetirilən əmrləri siləcək (/play, /pause, /shuffle, /stop və s.)dərhal.

6️⃣ **Play Parametrləri:**

/playmode - Qrupunuzun oyun parametrlərini təyin edə biləcəyiniz düymələri olan tam ifa parametrləri paneli əldə edin.

<u>Oyun rejimində seçimlər:</u>

1️⃣ **Axtarış Modu** [Birbaşa və ya Daxil] - Siz /play i verərkən axtarış rejiminizi dəyişir.

2️⃣ **Admin Əmrləri** [Hər kəs və ya Adminlər] - Əgər hər kəs, qrupunuzda olan hər kəs admin əmrlərindən istifadə edə biləcək (məsələn, /skip, /stop və s.)

3️⃣ **Oynatma növü** [Everyone or Admins] - If admins, only admins present in group can play music on voice chat."""

HELP_5 = """🔰**<u>SUDO İSTİFADƏÇİLƏRİNİ ƏLAVƏ EDİN və SİLİN :</u>**
/addsudo [İstifadəçi adı və ya istifadəçiyə cavab]
/delsudo [İstifadəçi adı və ya istifadəçiyə cavab]

🛃**<u>HEROKU:</u>**
/usage - Dyno İstifadəsi.

🌐**<u>KONFİQURASİYA VAR:</u>**
/get_var - Heroku və ya .env-dən konfiqurasiya dəyişənini əldə edin.
/del_var - Heroku və ya .env-də hər hansı dəyişəni silin.
/set_var [Var Adı] [Dəyər] - Heroku və ya .env-də Var təyin edin və ya yeniləyin. Var və onun dəyərini boşluqla ayırın.

🤖**<u>BOT ƏMRƏLƏRİ:</u>**
/reboot - Botu yeniləyin.
/update - Botu yeniləyin.
/speedtest - Server sürətlərini yoxlayın.
/maintenance [Etkinleştirme / Devre dışı]
/logger [aktivləşdirin / söndürün] - Bot axtarış edilmiş sorğuları qeyd qrupunda qeyd edir.
/get_log [Sətirlərin sayı] - Bot jurnalınızı heroku və ya vps-dən əldə edin. Hər ikisi üçün işləyir.
/autoend [aktiv / deaktiv edin] - Heç kim qulaq asmırsa, 3 dəqiqədən sonra yayımın avtomatik bitməsini aktivləşdirin.

📈**<u>İSTATİSTİK KOMUTLARI:</u>**
/activevoice - Botta aktif sesli sohbetleri kontrol edin.
/activevideo - Botta aktif görüntülü aramaları kontrol edin.
/stats - Bot İstatistiklerini Kontrol Edin.

⚠️**<u>KARA LİSTE SOHBET FONKSİYONU:</u>**
/blacklistchat [CHAT_ID] - Music Bot kullanarak herhangi bir sohbeti kara listeye alın.
/whitelistchat [CHAT_ID] - Kara listeye alınmış herhangi bir sohbeti Music Bot kullanarak beyaz listeye alın.
/blacklistedchat - Kara listeye alınmış tüm sohbetleri kontrol edin.

👤**<u>ENGELLENMİŞ FONKSİYON:</u>**
/block [Kullanıcı adı veya bir kullanıcıyı yanıtla] - Bir kullanıcının bot komutlarını kullanmasını engeller.
/unblock [Kullanıcı adı veya bir kullanıcıyı yanıtla] - Bir kullanıcıyı Bot'un Engellenenler Listesinden çıkarın.
/blockedusers - Engellenen Kullanıcı Listelerini Kontrol Edin.

👤**<u>GBAN FONKSİYONU:</u>**
/gban [Kullanıcı adı veya bir kullanıcıyı yanıtla] - Bir kullanıcıyı bot sunucusu sohbetinden yasaklayın ve botunuzu kullanmasını engelleyin.
/ungban [Kullanıcı adı veya bir kullanıcıyı yanıtla] - Bir kullanıcıyı Bot'un gbanlı Listesinden çıkarın ve onun botunuzu kullanmasına izin verin.
/gbannedusers - Gbanlı Kullanıcı Listelerini Kontrol Edin.

🎥**<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Söhbətlərin Sayı] - Eyni anda Video Zənglər üçün icazə verilən Söhbətlərin maksimum sayını təyin edin. Defolt olaraq 3 söhbət.
/videomode [yükləyin|m3u8] - Endirmə rejimi aktivdirsə, Bot videoları M3u8 formasında oynamaq əvəzinə endirəcək. Varsayılan olaraq M3u8-ə. Hər hansı sorğu m3u8 rejimində oxunmayanda yükləmə rejimindən istifadə edə bilərsiniz.

⚡️**<u>ÖZƏL BOT FUNKSİYASI:</u>**
/authorize [CHAT_ID] - Botunuzdan istifadə etmək üçün söhbətə icazə verin.
/unauthorize [CHAT_ID] - Söhbətin botunuzdan istifadəsinə icazə verməyin.
/authorized - Botunuzun bütün icazə verilən söhbətlərini yoxlayın.

🌐**<u>YAYIM FUNKSİYASI:</u>**
/broadcast [Mesaj və ya Mesaja Cavab] - İstənilən mesajı Botun Xidmət edilən Çatlarına yayımlayın.

<u>Yayım Seçimləri:</u>
**-pin** : Bu, mesajınızı sabitləyəcək.
**-pinloud** : Bu, mesajınızı yüksək səsli bildirişlə bağlayacaq.
**-user** : Bu, mesajınızı botunuzu işə salmış istifadəçilərə yayımlayacaq.
**-assistant** : Bu, mesajınızı botun köməkçi hesabından yayımlayacaq.
**-nobot** : Bu, botunuzu mesaj yayımlamamağa məcbur edəcək

**Misal:** `/broadcast -user -assistant -pin Salam Testi`

"""
