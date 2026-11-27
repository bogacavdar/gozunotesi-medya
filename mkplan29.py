import json,shutil,os
M=json.load(open('/home/claude/gunluk29/metin.json'));X=json.load(open('/home/claude/yeni3/paylas29.json'))
AD={'koc':('Koç','♈','koçburcu','koç'),'boga':('Boğa','♉','boğaburcu','boğa'),'ikizler':('İkizler','♊','ikizlerburcu','ikizler'),'yengec':('Yengeç','♋','yengeçburcu','yengeç'),'aslan':('Aslan','♌','aslanburcu','aslan'),'basak':('Başak','♍','başakburcu','başak'),'terazi':('Terazi','♎','teraziburcu','terazi'),'akrep':('Akrep','♏','akrepburcu','akrep'),'yay':('Yay','♐','yayburcu','yay'),'oglak':('Oğlak','♑','oğlakburcu','oğlak'),'kova':('Kova','♒','kovaburcu','kova'),'balik':('Balık','♓','balıkburcu','balık')}
GUN='29 Kasım Pazar';G='29 KASIM PAZAR'
SIRA=list(AD);P=[];V='/home/claude/gozunotesi-medya/v'
for no,b in enumerate(SIRA,1):
  L=M[b];ad,em,ht,lo=AD[b];saat=f"09:{(no-1)*5:02d}";base=f"2026-11-29_{saat.replace(':','')}_{b}_gunluk"
  d=f'/mnt/user-data/outputs/g29d/{no:02d}_{b}'
  tags=[f"{lo} burcu",f"{lo} burcu günlük",f"{lo} burcu bugün",f"{lo} burcu 29 kasım","29 kasım burç yorumları","günlük burç yorumları","bugün burçları neler bekliyor",f"{lo} burcu özellikleri",f"{lo} kadını","astroloji","burç yorumu","shorts"]
  P.append(dict(saat=saat,klasor=f'{no:02d}_{b}',video=f'{b}_gunluk.mp4',kapak=f'{b}_gunluk_instagram_kapak.jpg',src=f'{d}/{b}_gunluk.mp4',srck=f'{d}/{b}_gunluk_instagram_kapak.jpg',base=base,
   ig=f"{L[0]} {em}\n{ad} burcu {GUN} günlük yorumu\n{L[5]}\nEğlence amaçlıdır.\n#shortstory #astroloji #{ht} #günlükburç #gözünötesi",
   yt_baslik=f"{ad} Burcu Günlük Yorum {GUN} {em}",yt_aciklama=f"{L[0]}\n{ad} burcu için {GUN} günlük yorumu. {L[1]} {L[3]}\n{L[5]}\n\nEğlence amaçlıdır.\n\n#{ht} #günlükburç #burçyorumu #gözünötesi #shorts",yt_etiket=', '.join(tags)))
for saat,kl,k in [("15:00","13_gokyuzu_merkur_golge","merkur_golge"),("18:00","14_uyum_yengec_balik","yengec_balik"),("21:00","15_matris_kader_matrisi_2","kader_matrisi_2")]:
  x=X[k];d=f'/mnt/user-data/outputs/y3/{k}'
  P.append(dict(saat=saat,klasor=kl,video=f'{k}.mp4',kapak=f'{k}_instagram_kapak.jpg',src=f'{d}/{k}.mp4',srck=f'{d}/{k}_instagram_kapak.jpg',base=f"2026-11-29_{saat.replace(':','')}_{k}",ig=x['ig'],yt_baslik=x['yt_baslik'],yt_aciklama=x['yt_aciklama'],yt_etiket=x['yt_etiket']))
for p in P:
  shutil.copy(p['src'],f"{V}/{p['base']}.mp4");shutil.copy(p['srck'],f"{V}/{p['base']}.jpg")
for p in P: p.pop('src');p.pop('srck')
json.dump(P,open('/home/claude/gozunotesi-medya/plan_2026-11-29.json','w'),ensure_ascii=False,indent=1)
import html
S=[]
for p in P:
  S.append(f'<section><h2>{p["saat"]} · {p["video"][:-4]}</h2><video controls preload="none" playsinline poster="v/{p["base"]}.jpg" src="v/{p["base"]}.mp4"></video><pre>{html.escape(p["ig"])}</pre></section>')
H=f'<!DOCTYPE html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>29 Kasım Pazar · İnceleme</title><style>body{{font-family:system-ui;background:#0b1230;color:#f3e6c0;margin:0;padding:12px}}section{{margin:0 0 28px}}video{{width:100%;max-width:420px;border-radius:12px;background:#000}}pre{{white-space:pre-wrap;font-size:14px;color:#ddd}}h2{{font-size:18px;color:#e8c46a}}</style></head><body><h1>29 Kasım Pazar · 15 video</h1>{"".join(S)}</body></html>'
open('/home/claude/gozunotesi-medya/29kasim.html','w').write(H);print(len(P))
