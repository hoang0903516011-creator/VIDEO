# Tốp Gia — bản vui nhộn, có nhân vật và unbox

Video dọc **30 giây, 1080×1920, 30fps**. Có giọng đọc tiếng Việt tổng hợp, nhạc và hiệu ứng âm thanh tự tạo, phụ đề theo thời điểm từng câu.

## Video

- [Full HD](renders/top-gia-vui-30s.mp4)
- [Bản nhẹ 720p](renders/top-gia-vui-30s-mobile.mp4)

Video là **ảnh AI có chuyển động đồ họa**, không phải footage người diễn chuyển động hoặc avatar nhép môi. Nhân vật là người hư cấu; bao bì là ảnh minh họa theo tham chiếu. Có nhãn “HÌNH MINH HỌA AI” trong video.

## Nội dung

| Thời gian | Cảnh |
| --- | --- |
| 0–4s | Nhân vật chuẩn bị đi, được đưa gói khăn và nhắc “Khoan!” |
| 4–7s | Mở thùng chứa nhiều gói khăn |
| 7–9,35s | Lấy một gói từ lô hàng |
| 9,35–11s | Mở nắp và rút khăn |
| 11–14s | Đi làm, bỏ khăn vào túi cạnh laptop |
| 14–17s | Đi chơi, mang theo khăn |
| 17–24s | Trưng bày 6 gói, hiện giá và điều kiện |
| 24–30s | Cầm sản phẩm, chỉ giỏ hàng, câu kết vui |

Ưu đãi do chủ dự án cung cấp: **6 gói • 150.000đ**, từ **20–31/10**, mua qua giỏ hàng TikTok tài khoản **Đồ Gia dụng tốt**. Không tự thêm phần trăm giảm giá, giá gốc hay công dụng sản phẩm.

## Dựng và kiểm tra

Node.js >=22, FFmpeg và Chrome/Chromium. Chạy trong thư mục `top-gia-vui`:

```sh
npm run check
npm run render -- --output renders/top-gia-vui-30s.mp4 --fps 30 --workers 2
```

Trong cloud hiện tại, thêm `XDG_CACHE_HOME=/workspace/.cache npm_config_cache=/workspace/.cache/npm HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium` trước lệnh để dùng các đường dẫn có quyền ghi.

`index.html` là nguồn HyperFrames. `scripts/build_composition.py` tạo lại HTML từ bố cục và `voice-timing.json` bằng Python chuẩn. Hai ảnh storyboard WebP là các ảnh AI nhiều khung, được chọn khung bằng CSS background; ảnh được mã hóa lossless từ PNG. Không cần cài mô hình giọng đọc để render lại vì `assets/narration.wav` đã có sẵn.

Để tạo lại giọng đọc, cài `sherpa-onnx==1.13.8`, `soundfile`, `numpy`; tải mô hình Vietnamese Piper từ [sherpa-onnx releases](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-vi_VN-vais1000-medium.tar.bz2), rồi chạy:

```sh
python scripts/generate_voice.py /path/to/vits-piper-vi_VN-vais1000-medium
python scripts/generate_music.py
python scripts/build_composition.py
```

Giọng đọc: Piper `vi_VN-vais1000-medium`, thực thi bằng sherpa-onnx. Model card đi kèm trong `assets/VOICE-MODEL-CARD.txt`; bộ dữ liệu VAIS-1000 theo [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), nguồn [VAIS-1000 Vietnamese Speech Synthesis Corpus](https://ieee-dataport.org/documents/vais-1000-vietnamese-speech-synthesis-corpus). Phông Be Vietnam Pro: xem `assets/FONT-LICENSE.txt`. GSAP: phần license trong đầu tệp `assets/gsap.min.js`.

Bố cục có chồng cảnh trong 0,28 giây chuyển cảnh; các vùng nội dung đã đánh dấu chồng có chủ đích. Khung giá giữ đứng yên để xem đủ sáu gói.

## Kết quả kiểm tra

`npm run check`: lint, runtime, bố cục và chuyển động không có lỗi/cảnh báo; 26/26 lượt kiểm tra tương phản đạt. MP4 Full HD có H.264 + AAC, 1080×1920, 30fps, thời lượng 30 giây; đã giải mã kiểm tra toàn bộ tệp. Khung ưu đãi được xem lại từ chính MP4 đã xuất.
