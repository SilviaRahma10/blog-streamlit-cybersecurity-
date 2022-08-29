import streamlit as st
import pandas as pd
from PIL import Image
# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Headline Project Malware & Virus (Ransomware)
def main_page():
    st.sidebar.markdown("###### MALWARE & VIRUS (RANSOMWARE)")
    with st.container():
        st.markdown('---')
        st.markdown\
             ("<h1 style='text-align: center; color: #728FCE;'>MALWARE & VIRUS</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: #728FCE;'>(RANSOMWARE)</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: #728FCE;'>🦠⚠️🖥️</h1>", unsafe_allow_html=True)
        st.markdown('---')
        st.markdown("<h3 style='text-align: center; color: #728FCE;'>Headline Project</h3>", unsafe_allow_html=True)
        st.markdown('- Virus dan Worm'
            '\n- Perbedaan Spyware, Adware dan **Ransomware**'
            '\n>>1. **Penjelasan tentang Ransomware**'
            '\n>>2. **Macam-Macam image.pngRansomware**'
            '\n- Mitigasi/Pertahanan : Antimalware')
    

# Virus dan Worm
def page1():
    st.sidebar.markdown('- Virus'
                    '\n- Worm'
                    '\n- Persamaan Virus dan Worm'
                    '\n- Perbedaan Virus dan Worm')
    st.markdown('---')
    st.markdown("<h1 style='text-align: center; color: #728FCE;'>PERBEDAAN VIRUS & WORM</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #728FCE;'>🦠🪱</h1>", unsafe_allow_html=True)
    st.markdown('---')
    
    # VIRUS
    st.write('## 1. Virus')
    st.write('###### *Konsep* :')
    st.write(" - Virus dirancang untuk menyebar dari satu sistem ke sistem yang lain")
    st.write(" - Virus biasanya merusak file pada suatu sistem")
    st.write("###### *Penyebaran* :")
    st.write(" - Media storage non-permanen")
    st.write(" - Email")
    st.write(" - File Public")
    st.markdown("![Alt Text](https://media.giphy.com/media/IO88K7ZUY2ZHODAzso/giphy.gif)")
    # WORM
    st.write('\n## 2. Worm')
    st.write('###### *Konsep* :')
    st.write(" - Jenis malware yang mampu berproduksi secara cepat dari sistem yang terinfeksi ke sistem lain ")
    st.write(" 2. Memanfatkan kelonggaran  LAN, WAN, Internet")
    st.write("###### *Penyebaran* :")
    st.write(" - Media Komunikasi ")
    st.write(" - Media storage permanen/non permanen")
    # PERSAMAAN
    st.write('\n## 3. Persamaan Virus dan Worm')
    st.write(" - Malware yang dapat menular")
    st.write(" - Tujuannya mengubah cara sebuah sistem beroperasi")
    st.write(" - Bisa menyebar dengan cepat setelah sebuah sistem terinfeksi")
    # PERBEDAAN
    st.write('\n## 4. Perbedaan Virus dan Worm')
    st.write("*VIRUS :*")
    st.write(" - Virus memerlukan file untuk melampirkan diri ")
    st.write("*WORM :*")
    st.write(" - Worm tidak bergantung pada file untuk melampirkan diri ")

# Perbedaan Spyware, Adware dan Ransomware
def page2():
    st.sidebar.markdown('- Definisi Malware'
                    '\n- Jenis-Jenis Malware'
                    '\n>>1. Worm'
                    '\n>>2. Spyware'
                    '\n>>3. Adware'
                    '\n>>4. Ransomware')
    st.markdown('---')
    st.markdown("<h1 style='text-align: center; color: #728FCE;'>MALWARE</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #728FCE;'>⚠️</h1>", unsafe_allow_html=True)
    st.markdown('---')
    # Definisi Malware
    st.write("## - Definisi Malware")
    st.write("Perangkat lunak yang dibuat dengan tujuan memasuki dan terkadang merusak sistem komputer, jaringan, atau server tanpa diketahui oleh pemiliknya. Istilah malware diambil dari gabungan potongan dua kata yaitu malicious “berniat jahat” dan software “perangkat lunak”. Tujuannya tentu untuk merusak atau mencuri data dari perangkat yang dimasuki.")
    # Jenis-jenis Malware
    st.write("## - Jenis-Jenis Malware")
    # Worm
    st.write("#### 1. Worm")
    st.write('###### *Konsep* :')
    st.write("- Jenis malware yang mampu berproduksi secara cepat dari sistem yang terinfeksi ke sistem lain ")
    st.write("- Memanfatkan kelonggaran  LAN, WAN, Internet")
    st.write("###### *Ciri Sistem yang diserang :*")
    st.write("- Banyak file, folder atau aplikasi asing yang muncul dalam sistem")
    st.write("- Hilangnya file yang disimpan dalam sistem")
    # Spyware
    st.write("#### 2. Spyware")
    st.write('###### *Konsep* :')
    st.write("- Jenis malware yang bertujuan untuk melacak dan merekam aktivitas pemilik sistem")
    st.write("###### *Ciri Sistem yang diserang :*")
    st.write("- Homepage dari browser berubah")
    st.write("- Mikrofon dan kamera otomatis terhubung")
    st.write("- Sistem berjalan sangat lambat")
    # Adware
    st.write("#### 3. Adware")
    st.write('###### *Konsep* :')
    st.write("- Jenis malware yang bertujuan untuk menampilkan iklan pada pemilik sistem untuk mendapat keuntungan  iklan illegal")
    st.write("- Software yang berjalan pada sistem")
    st.write("###### *Ciri Sistem yang diserang :*")
    st.write("- Muncul Pop-up iklan")
    st.write("- Sering teralihkan otomatis ke situs tertentu")
    st.write("- Durasi mengakses situs secara online semakin lama")
    # Ransomware
    st.write("#### 4. Ransomware")
    st.write("Ransomware bekerja dengan mengenkripsi semua file yang ada pada sistem, proses deskripsi hanya bisa dilakukan oleh peretas")
    image = Image.open('C:\Streamlit\Picture1.jpg')
    st.image(image, caption='https://www.secureops.com/wp-content/uploads/2021/06/Ransomware-Infographic-SecureOps.pdf')
    st.write('###### *Konsep* :')
    st.write("- Jenis malware yang bertujuan khusus dan sulit diremediasi")
    st.write("- Disalurkan melalui rekayasa social dan terinstall pada computer ")
    st.write("- Tersisip pada file download secara ilegal")
    st.write("###### *Ciri Sistem yang diserang :*")
    st.write("- Terdapat dokumen yang tiba-tiba terkunci atau hilang.")
    st.write("- Aplikasi tidak berjalan dengan semestinya")
    st.write("- Durasi mengakses situs secara online semakin lama")
    # Top 3 Ransomware
    st.write("###### *Top 3 Ransomware :*")
    image = Image.open('C:\Streamlit\Picture2.jpg')
    st.image(image)
    col1, col2, col3 = st. columns(3)
    col1.metric("Email Phishing", " 90%", "of all data breaches")
    col2.metric("Remote Desktop Protocol", " 60%", "of all ransomware attacks")
    col3.metric("Software Vulnerabilities", " 60%", "off all breanches involved unpactched vulnerabilities")
    # Jenis Ransomware
    st.write("###### *Jenis-jenis Ransomware :*")
    image = Image.open('C:\Streamlit\Picture3.jpg')
    st.image(image, caption='Walaupun ada jenis Ransomware baru seperti Black basta. Ada 3 Ransomware yang ditemukan % tinggi yaitu LockBit, Conti, dan AlphV, yang merupakan 60 persen dari semua pelanggaran yang diketahui dalam analisis kami.')
    # Cara Kerja Ransomware
    st.write("###### *Cara Kerja Ransomware :*")
    image = Image.open('C:\Streamlit\Picture4.jpg')
    st.image(image)
    image = Image.open('C:\Streamlit\Picture5.jpg')
    st.image(image)
    # Persentase Ransomware
    st.write("###### *Persentase Ransomware (by Country) :*")
    image = Image.open('C:\Streamlit\Picture6.jpg')
    st.image(image)

# Mitigasi/Pertahanan : Antimalware
def page3():
    st.sidebar.markdown('- Endpoint Security'
                    '\n- Signature Based Detection'
                    '\n- Behaviour Based Detection'
                    '\n- Sandboxing')
    st.markdown('---')
    st.markdown("<h1 style='text-align: center; color: #728FCE;'>ANTI MALWARE</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #728FCE;'>🔐</h1>", unsafe_allow_html=True)
    st.markdown('---')
    # Endpoint Security
    st.write("## Endpoint Security")
    st.write("- Mendeteksi malware tingkat lanjut dan menawarkan perlindungan"
            "\n - Memindai semua data yang masuk"
            "\n - Memindai sistem pada komputer")
    image = Image.open('C:\Streamlit\Picture7.jpg')
    st.image(image)
    # Signature Based Detection
    st.write("## Signature Based Detection")
    st.write("- Mendeteksi malware yang menginfeksi seperti keylogger atau adware"
            "- Menggunakan satu set komponen perangkat lunak dan ciri khas masing-masing malware untuk mengidentifikasi perangkat lunak berbahaya")
    # Behaviour Based Detection
    st.write("## Behaviour Based Detection")
    st.write("- Membantu Security Engineer mengidetifikasi, menganalisa dan melakukan blokir pada malware dengan menggunakan pendekatan aktif.")
    # Sandboxing
    st.write("## Sandboxing")
    st.write("- Mengisolasi file yang berpotensi bahaya"
            "- Digunakan untuk menyaring file yang berpotensi berbahaya dan menghapusnya sebelum merusak.")
    link = '[Sandboxing Tools](https://www.hybrid-analysis.com/)'
    st.markdown(link, unsafe_allow_html=True)

page_names_to_funcs = {
    "Headline Project": main_page,
    "Perbedaan Virus & Worm ": page1,
    "Malware": page2,
    "Anti Malware": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()