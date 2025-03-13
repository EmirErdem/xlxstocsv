# Excel to CSV Converter

Bu Streamlit uygulaması, birden fazla Excel (XLSX) dosyasını aynı anda CSV formatına dönüştürmenize olanak sağlar.

## Özellikler

- Çoklu XLSX dosya yükleme desteği
- Toplu dönüştürme işlemi
- Dönüştürülen dosyaları ZIP formatında indirme
- Kullanıcı dostu arayüz
- Hata yönetimi ve bilgilendirme

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/[kullanıcı-adınız]/excel-to-csv-converter.git
cd excel-to-csv-converter
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım

1. Uygulamayı başlatın:
```bash
streamlit run app.py
```

2. Tarayıcınızda `http://localhost:8501` adresine gidin
3. "Browse files" butonunu kullanarak XLSX dosyalarınızı yükleyin
4. "CSV'ye Dönüştür" butonuna tıklayın
5. Dönüştürme işlemi tamamlandığında ZIP dosyasını indirin

## Gereksinimler

- Python 3.7+
- streamlit==1.32.0
- pandas==2.2.1
- openpyxl==3.1.2
- zipfile36==0.1.3 