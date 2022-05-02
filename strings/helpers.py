#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**<u>Yönetici Komutları:</u>**

**c** stands for channel play.

/pause ve ya /cpause - Çalan müziği duraklatın.
/resume ve ya /cresume- Duraklatılan müziği devam ettirin.
/mute ve ya /cmute- Çalan müziğin sesini kapatın.
/unmute ve ya /cunmute- Sessize alınan müziğin sesini açın.
/skip ve ya /cskip- Çalmakta olan müziği atla.
/stop ve ya /cstop- Çalan müziği durdurun.
/shuffle ve ya /cshuffle- Sıraya alınmış çalma listesini rastgele karıştırır.
/seek ve ya /cseek - İleri Müziği sürenize göre arayın.
/seekback ve ya /cseekback - Geriye Müziği sürenize göre arayın.
/restart - Sohbetiniz için botu yeniden başlatın.


✅<u>**Spesifik Atlama:**</u>
/skip or /cskip [Sayı(örnek: 3)]
    - Müziği belirtilen sıraya alınmış numaraya atlar. Örnek: /skip 3, müziği sıraya alınan üçüncü müziğe atlar ve sıradaki 1 ve 2 müziği yok sayar.

✅<u>**Döngü Oynat:**</u>
/loop or /cloop [etkin/devre dışı] veya [1-10 arası sayılar]
    - Etkinleştirildiğinde, bot sesli sohbette çalmakta olan müziği 1-10 kez döngüye alır. Varsayılan olarak 10 kez.
    
✅<u>**Auth Users:**</u>
Auth Users can use admin commands without admin rights in your chat.

/auth [Username] - Add a user to AUTH LIST of the group.
/unauth [Username] - Remove a user from AUTH LIST of the group.
/authusers - Check AUTH LIST of the group."""


HELP_2 = """✅<u>**Play Commands:**</u>

Available Commands = play , vplay , cplay

ForcePlay Commands = playforce , vplayforce , cplayforce

**c** stands for channel play.
**v** stands for video play.
**force** stands for force play.

/play or /vplay or /cplay  - Bot will start playing your given query on voice chat or Stream live links on voice chats.

/playforce or /vplayforce or /cplayforce -  **Force Play** stops the current playing track on voice chat and starts playing the searched track instantly without disturbing/clearing queue.

/channelplay [Chat username or id] or [Disable] - Connect channel to a group and stream music on channel's voice chat from your group.


✅**<u>Bot's Server Playlists:</u>**
/playlist  - Check Your Saved Playlist On Servers.
/deleteplaylist - Delete any saved music in your playlist
/play  - Start playing Your Saved Playlist from Servers."""


HELP_3 = """✅<u>**Bot Commands:**</u>

/stats - Get Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat etc etc.

/sudolist - Check Sudo Users of Yukki Music Bot

/lyrics [Music Name] - Searches Lyrics for the particular Music on web.

/song [Track Name] or [YT Link] - Download any track from youtube in mp3 or mp4 formats.

/player -  Get a interactive Playing Panel.

**c** stands for channel play.

/queue or /cqueue- Check Queue List of Music."""

HELP_4 = """✅<u>**Extra  Commands:**</u>
/start - Start the Music Bot.
/help  - Get Commands Helper Menu with detailed explanations of commands.
/ping- Ping the Bot and check Ram, Cpu etc stats of Bot.

✅<u>**Group Settings:**</u>
/settings - Get a complete group's settings with inline buttons

🔗 **Options in Settings:**

1️⃣ You can set **Audio Quality** you want to stream on voice chat.

2️⃣ You can set **Video Quality** you want to stream on voice chat.

3️⃣ **Auth Users**:- You can change admin commands mode from here to everyone or admins only. If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)

4️⃣ **Clean Mode:** When enabled deletes the bot's messages after 5 mins from your group to make sure your chat remains clean and good.

5️⃣ **Command Clean** : When activated, Bot will delete its executed commands (/play, /pause, /shuffle, /stop etc) immediately.

6️⃣ **Play Settings:**

/playmode - Get a complete play settings panel with buttons where you can set your group's play settings. 

<u>Options in playmode:</u>

1️⃣ **Search Mode** [Direct or Inline] - Changes your search mode while you give /play mode. 

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
