### 📄 File: `README.md` | 🏷️ Markdown

```markdown
# ⚡ Sentiric LLM Streaming Service

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Language](https://img.shields.io/badge/language-Python-blue.svg)]()
[![Engine](https://img.shields.io/badge/engine-StreamingAdapter-red.svg)]()

**Sentiric LLM Streaming Service**, LLM'lerden gelen metin çıktısını canlı olarak Agent'lara iletmek için optimize edilmiştir. Bu uzman servis, sesli diyaloglarda kritik olan düşük gecikmeli yanıtları sağlamak için ana LLM Gateway'in yükünü hafifletir.

## 🎯 Temel Sorumluluklar

*   **Akış İletimi:** LLM sağlayıcısından gelen sürekli veri akışını kesintisiz olarak tüketir ve yeniden paketler.
*   **Düşük Gecikme:** Yanıtların anında iletilmesini sağlayarak TTFT'yi (Time to First Token) en aza indirir.
*   **Protokol Dönüşümü:** Gerekirse gRPC Stream'i HTTP Stream'e veya tam tersine çevirir.

## 🛠️ Teknoloji Yığını

*   **Dil:** Python 3.11
*   **Web Çerçevesi:** FastAPI / Uvicorn (Asenkron I/O)
*   **İstemci:** httpx (Streaming API çağrıları için)

## 🔌 API Etkileşimleri

*   **Gelen (Sunucu):**
    *   `sentiric-llm-gateway-service` (HTTP POST Stream): LLM çıktısını başlatır.
*   **Giden (İstemci):**
    *   `sentiric-llm-gemini-service` / `sentiric-llm-ollama-service` (Hedef LLM'in kendi Streaming API'si).

---
## 🏛️ Anayasal Konum

Bu servis, [Sentiric Anayasası'nın](https://github.com/sentiric/sentiric-governance) **AI Engine Layer**'ında yer alan uzman bir bileşendir.