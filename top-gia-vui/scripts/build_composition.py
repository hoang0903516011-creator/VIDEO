"""Build the seekable 30-second HyperFrames composition."""
from pathlib import Path
import json, html
R=Path(__file__).resolve().parents[1]
SCENES=[
 ('hook',0,4,0,0,'KHOAN!','Quên người bạn đồng hành!','yellow'),
 ('box',4,7,0,1,'KHUI LÔ KHĂN!','Tốp Gia đây rồi.','mint'),
 ('pack',7,9.35,0,2,'TƯỞNG ĐANG KHUI QUÀ!','Lấy một gói từ lô hàng.','peach'),
 ('wipe',9.35,11,0,3,'RÚT MỘT TỜ','Chuẩn bị sẵn bên mình.','cream'),
 ('work',11,14,0,4,'ĐI LÀM?','Có khăn!','mint'),
 ('play',14,17,1,0,'ĐI CHƠI?','Vẫn có khăn!','peach'),
 ('offer',17,24,1,1,'6 GÓI','150.000đ','yellow'),
 ('cta',24,30,1,2,'BẤM GIỎ HÀNG','ĐẶT MUA NGAY','mint'),
]
css=''
for w in [400,900]:
 css+=f'''@font-face{{font-family:BeVietnam;src:url(assets/be-vietnam-pro-vietnamese-{w}-normal.woff2);font-weight:{w};unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB;}}
 @font-face{{font-family:BeVietnam;src:url(assets/be-vietnam-pro-latin-{w}-normal.woff2);font-weight:{w};unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD;}}'''
css+='''
*{box-sizing:border-box;margin:0}html,body{width:1080px;height:1920px;overflow:hidden;background:#FFF9EF;color:#183F39;font-family:BeVietnam,sans-serif}#root{width:1080px;height:1920px;position:relative;overflow:hidden}.scene{position:absolute;inset:0;width:1080px;height:1920px;overflow:hidden;background:#FFF9EF}.scene:not(:first-child){opacity:0}.photo{position:absolute;inset:0;overflow:hidden}.photo-zoom{width:100%;height:100%;transform:scale(1.025)}.sprite{width:100%;height:100%;background-repeat:no-repeat}.sheet0{background-image:url(assets/storyboard.webp);background-size:300% 200%}.sheet1{background-image:url(assets/storyboard-extra.webp);background-size:300% 100%}.scene-content{position:relative;width:100%;height:100%;padding:78px 150px 255px 70px;display:flex;flex-direction:column;gap:24px;pointer-events:none}.brand{align-self:flex-start;background:#FFF9EF;padding:20px 28px;border-radius:24px;box-shadow:0 4px 20px #183f3918}.brand-name{font-weight:900;font-size:32px;letter-spacing:3px}.brand-detail{font-size:20px;line-height:1.7}.story-card{margin-top:auto;margin-bottom:200px;background:#FFF9EF;padding:32px 34px;border-radius:32px;box-shadow:0 10px 35px #183f3920;max-width:840px}.yellow{background:#F4D976}.mint{background:#BBDDCF}.peach{background:#F0B9A6}.cream{background:#FFF9EF}.headline{font-size:70px;line-height:1.16;font-weight:900;letter-spacing:-2px}.subline{font-size:40px;line-height:1.3;margin-top:16px}.hook .headline{font-size:112px}.pack .headline{font-size:62px}.wipe .headline{font-size:70px}.work .subline,.play .subline{font-size:64px;font-weight:900}.cta .headline{font-size:65px}.cta .subline{font-size:60px;font-weight:900}.seller{font-size:29px;font-weight:400;line-height:1.45;margin-top:16px}.arrow{position:absolute;right:170px;bottom:560px;width:85px;height:115px;stroke:#183F39;stroke-width:11;fill:none;stroke-linecap:round;stroke-linejoin:round}.caption{position:absolute;left:70px;top:1480px;width:840px;padding:24px 30px;border-radius:24px;background:#FFF9EF;color:#183F39;font-size:42px;line-height:1.35;font-weight:900;z-index:50;box-shadow:0 5px 25px #183f3918}.offer{background:#F4D976}.offer .photo{inset:auto;left:120px;top:70px;width:740px;height:1315.556px;border-radius:38px;overflow:hidden}.offer .photo-zoom{transform:scale(1.025)}.offer .brand{padding:16px 25px}.offer .story-card{margin-bottom:0;padding:28px 34px;border:3px solid #183F39}.offer .headline{font-size:64px}.offer .subline{font-size:128px;font-weight:900;letter-spacing:-5px;margin-top:0;line-height:1.2;font-variant-numeric:tabular-nums}.condition{font-size:30px;line-height:1.45;margin-top:16px}.date-chip{display:inline-block;background:#183F39;color:#FFF9EF;font-size:30px;padding:10px 20px;border-radius:16px;margin-top:12px}.badge{align-self:flex-start;padding:12px 22px;border-radius:50px;background:#F4D976;font-weight:900;font-size:24px;letter-spacing:2px}
'''
body='';js='window.__timelines=window.__timelines||{};const tl=gsap.timeline({paused:true});\n'
for n,(sid,start,end,sheet,panel,title,sub,color) in enumerate(SCENES):
 col=panel%3;row=panel//3
 pos=f'{col*50}% {row*100 if sheet==0 else 50}%'
 body+=f'''<section id="{sid}" class="scene {sid}" style="z-index:{n+1};opacity:{0 if n else 1}">
 <div class="photo" data-layout-allow-overflow><div class="photo-zoom"><div class="sprite sheet{sheet}" style="background-position:{pos}"></div></div></div>
 <div class="scene-content" data-layout-allow-overlap><div class="brand"><p class="brand-name">TỐP GIA</p><p class="brand-detail">KHĂN GIẤY ƯỚT · HÌNH MINH HỌA AI</p></div>
 <div class="story-card {color}"><h1 class="headline">{title}</h1><p class="subline">{sub}</p>'''
 if sid=='offer':body+='<p class="date-chip">20–31/10</p><p class="condition">Áp dụng khi mua qua giỏ hàng TikTok tài khoản <strong>Đồ Gia dụng tốt</strong>.</p>'
 if sid=='cta':body+='<p class="seller">TikTok · Đồ Gia dụng tốt</p>'
 body+='</div></div>'
 if sid=='cta':body+='<svg class="arrow" viewBox="0 0 85 115" data-layout-ignore><path d="M42 8V100 M12 70L42 101L72 70"/></svg>'
 body+='</section>\n'
 if n:
  js+=f'tl.set("#{sid}",{{opacity:1}},{start});tl.from("#{sid}",{{x:1080,duration:.28,ease:"power4.out",immediateRender:false}},{start});\n'
 if n:js+=f'tl.set("#{SCENES[n-1][0]}",{{opacity:0}},{start+.28});\n'
 off=.12 if n else .16
 js+=f'''tl.from("#{sid} .photo",{{opacity:0,scale:1.035,duration:.44,ease:"sine.out",immediateRender:false}},{start+off});
 tl.from("#{sid} .brand",{{opacity:0,x:-28,duration:.32,ease:"power2.out",immediateRender:false}},{start+off+.03});
 tl.from("#{sid} .story-card",{{opacity:0,y:52,rotation:{-2 if n%2==0 else 2},duration:.48,ease:"back.out(1.35)",immediateRender:false}},{start+off+.08});
 tl.from("#{sid} .headline",{{opacity:0,scale:.85,duration:.35,ease:"expo.out",immediateRender:false}},{start+off+.15});
 tl.from("#{sid} .subline",{{opacity:0,x:22,duration:.4,ease:"power3.out",immediateRender:false}},{start+off+.23});\n'''
 if sid=='offer':js+=f'tl.from("#offer .date-chip,#offer .condition",{{opacity:0,y:16,duration:.45,stagger:.12,ease:"sine.out",immediateRender:false}},{start+.65});'
 elif sid=='cta':js+='tl.from("#cta .seller,#cta .arrow",{opacity:0,scale:.7,duration:.45,stagger:.1,ease:"back.out(1.3)",immediateRender:false},24.7);tl.to("#cta .arrow",{y:22,duration:.45,repeat:9,yoyo:true,ease:"sine.inOut"},25);'
 # Vary ambient motion. Product display holds still so all six packs stay visible.
 if sid in ['hook','pack','wipe']:
  js+=f'tl.fromTo("#{sid} .photo-zoom",{{scale:1.025}},{{scale:{1.085 if sid!="wipe" else 1.10},duration:{end-start-.5},ease:"sine.inOut"}},{start+.45});\n'
 elif sid in ['work','play']:js+=f'tl.to("#{sid} .photo-zoom",{{x:{-12 if sid=="work" else 12},duration:{end-start-.5},ease:"sine.inOut"}},{start+.45});\n'
# Captions follow the generated utterance boundaries; offer uses its permanent price/date/conditions card.
for i,line in enumerate(json.loads((R/'voice-timing.json').read_text())):
 st,en=line['start'],line['end']
 if 17<=st<24:continue
 sceneend=next(s[2] for s in SCENES if s[1]<=st<s[2])
 stop=min(en+.2,sceneend-.02)
 body+=f'<p id="cap{i}" class="clip caption" data-start="{st}" data-duration="{round(stop-st,3)}" data-track-index="20">{html.escape(line["text"])}</p>\n'
 js+=f'tl.from("#cap{i}",{{opacity:0,y:10,duration:.13,ease:"power2.out",immediateRender:false}},{st});tl.to("#cap{i}",{{opacity:0,duration:.1,ease:"power2.in"}},{stop-.1});tl.set("#cap{i}",{{opacity:0}},{stop});\n'
body+='<audio id="narration" src="assets/narration.wav" data-start="0" data-duration="30" data-track-index="30" data-volume="1"></audio><audio id="music" src="assets/music-sfx.wav" data-start="0" data-duration="30" data-track-index="31" data-volume="0.65"></audio>'
js+='window.__timelines["topgia-fun"]=tl;'
R.joinpath('index.html').write_text(f'<!doctype html>\n<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=1080,height=1920"><script src="assets/gsap.min.js"></script><style>{css}</style></head><body><main id="root" data-composition-id="topgia-fun" data-start="0" data-duration="30" data-width="1080" data-height="1920">{body}</main><script>{js}</script></body></html>')
