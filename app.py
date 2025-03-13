import streamlit as st
import pandas as pd
import io
import zipfile
from datetime import datetime

def convert_xlsx_to_csv(xlsx_file):
    # Excel dosyasını oku
    df = pd.read_excel(xlsx_file)
    # CSV'ye dönüştür
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    return csv_buffer.getvalue()

def main():
    st.title("Excel (XLSX) to CSV Dönüştürücü")
    st.write("Birden fazla Excel dosyasını CSV formatına dönüştürün")

    # Dosya yükleme
    uploaded_files = st.file_uploader(
        "Excel dosyalarını seçin (birden fazla seçilebilir)",
        type=["xlsx"],
        accept_multiple_files=True
    )

    if uploaded_files:
        st.write(f"{len(uploaded_files)} dosya yüklendi")

        if st.button("CSV'ye Dönüştür"):
            # Zip dosyası oluştur
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for uploaded_file in uploaded_files:
                    try:
                        # Excel dosyasını CSV'ye dönüştür
                        csv_content = convert_xlsx_to_csv(uploaded_file)
                        
                        # Dosya adını .xlsx'ten .csv'ye değiştir
                        csv_filename = uploaded_file.name.rsplit('.', 1)[0] + '.csv'
                        
                        # CSV'yi zip dosyasına ekle
                        zip_file.writestr(csv_filename, csv_content)
                    except Exception as e:
                        st.error(f"Hata: {uploaded_file.name} dosyası dönüştürülemedi - {str(e)}")

            # Zip dosyasını indir
            zip_buffer.seek(0)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            st.download_button(
                label="Dönüştürülen CSV Dosyalarını İndir",
                data=zip_buffer.getvalue(),
                file_name=f"converted_csv_files_{timestamp}.zip",
                mime="application/zip"
            )

            st.success("Dönüştürme tamamlandı! Zip dosyasını indirebilirsiniz.")

if __name__ == "__main__":
    main() 