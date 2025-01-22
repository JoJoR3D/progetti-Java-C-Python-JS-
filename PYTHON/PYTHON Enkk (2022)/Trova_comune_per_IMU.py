
#Per creare questa stringa ho copiato 30 file alla volta (di più non li copiava tutti) dalla cartella. 
#Ma la copia includeva tutto il percorso di ogni singolo file, quindi ho chiesto a Gemini se poteva ricavare, 
#dal percorso del file, solo il nome e metterlo tra doppie virgolette.
#Non posso ottenere il nome del  file dal percorso mediante un mio codice, poichè
#il percorso di windows include il carattere '\' che in python rappresenta il carattere escape, ovver backslash.
#quindi quando inserisco il percorso in una stringa mi ritorna errore perchè vi è il carattere '\'. 

list_string= ["179975_DIMUNIC-04sa24d527d.pdf",
"179987_DIMUNIC-04ce24d801d.pdf",
"180065_DIMUNIC-04av24d671d.pdf",
"177843_DIMUNIC-04na24f488d.pdf",
"178403_DIMUNIC-04na24i391d.pdf",
"178432_CIMUNIC-04na24i262d.pdf",
"178432_CIMUNIC-04na24i262dAM.pdf",
"178460_DIMUNIC-04ce24i247d.pdf",
"178683_DIMUNIC-04na24b696d.pdf",
"178780_DIMUNIC-04na24a068d.pdf",
"179050_DIMUNIC-04av24f559d.pdf",
"179071_DIMUNIC-04ce24d709d.pdf",
"179181_DIMUNIC-04bn24b239d.pdf",
"179205_DIMUNIC-04ce24h268d.pdf",
"179252_DIMUNIC-04av24i893d.pdf",
"179269_DIMUNIC-04ce24c097d.pdf",
"179311_DIMUNIC-04sa24g063d.pdf",
"179323_DIMUNIC-04bn24l254d.pdf",
"179356_DIMUNIC-04sa24c984d.pdf",
"179397_DIMUNIC-04ce24b935d.pdf",
"179441_DIMUNIC-04av24a347d.pdf",
"179507_DIMUNIC-04na24e557d.pdf",
"179509_DIMUNIC-04ce24m092d.pdf",
"179545_DIMUNIC-04na24a268d.pdf",
"179549_DIMUNIC-04bn24d693d.pdf",
"179583_DIMUNIC-04bn24c476d.pdf",
"179605_DIMUNIC-04bn24m093d.pdf",
"179817_DIMUNIC-04av24i280d.pdf",
"179851_DIMUNIC-04av24l589d.pdf",
"179900_DIMUNIC-04na24h072d.pdf",
"181718_DIMUNIC-04sa24g011d.pdf",
"180080_DIMUNIC-04av24a489d.pdf",
"180094_DIMUNIC-04ce24c291d.pdf",
"180149_DIMUNIC-04na24b980d.pdf",
"180150_DIMUNIC-04ce24i234d.pdf",
"180256_DIMUNIC-04na24i862d.pdf",
"180275_DIMUNIC-04bn24i145d.pdf",
"180433_DIMUNIC-04ce24f043d.pdf",
"180452_DIMUNIC-04bn24h953d.pdf",
"180481_DIMUNIC-04av24i281d.pdf",
"180525_DIMUNIC-04ce24g661d.pdf",
"180579_DIMUNIC-04na24f162d.pdf",
"180585_DIMUNIC-04ce24e791d.pdf",
"180592_DIMUNIC-04ce24c561d.pdf",
"180646_DIMUNIC-04av24h006d.pdf",
"180727_DIMUNIC-04na24b227d.pdf",
"180764_DIMUNIC-04av24l102d.pdf",
"180854_DIMUNIC-04na24g670d.pdf",
"180861_DIMUNIC-04na24e131d.pdf",
"180862_DIMUNIC-04av24f546d.pdf",
"180909_DIMUNIC-04sa24i307d.pdf",
"180942_DIMUNIC-04sa24g230d.pdf",
"180964_DIMUNIC-04bn24d230d.pdf",
"181149_DIMUNIC-04na24i978d.pdf",
"181151_DIMUNIC-04av24i034d.pdf",
"181384_DIMUNIC-04na24m280d.pdf",
"181566_DIMUNIC-04sa24d292d.pdf",
"181617_DIMUNIC-04ce24a106d.pdf",
"181708_DIMUNIC-04na24g964d.pdf",
"181709_DIMUNIC-04av24b866d.pdf",
"182764_DIMUNIC-04ce24m262d.pdf",
"181729_DIMUNIC-04sa24h800d.pdf",
"181804_DIMUNIC-04sa24a717d.pdf",
"181910_DIMUNIC-04na24g568d.pdf",
"182032_DIMUNIC-04ce24i993d.pdf",
"182033_DIMUNIC-04bn24b239d.pdf",
"182069_DIMUNIC-04sa24h977d.pdf",
"182114_DIMUNIC-04bn24f557d.pdf",
"182129_DIMUNIC-04av24e206d.pdf",
"182141_DIMUNIC-04av24a399d.pdf",
"182195_DIMUNIC-04bn24d693d.pdf",
"182219_CIMUNIC-04ce24m092dAM.pdf",
"182245_DIMUNIC-04sa24g538d.pdf",
"182246_CIMUNIC-04sa24b895d.pdf",
"182246_CIMUNIC-04sa24b895dAM.pdf",
"182255_DIMUNIC-04av24f762d.pdf",
"182356_DIMUNIC-04sa24f479d.pdf",
"182444_DIMUNIC-04na24e906d.pdf",
"182449_DIMUNIC-04na24e620d.pdf",
"182471_DIMUNIC-04ce24h423d.pdf",
"182472_CIMUNIC-04ce24h423d.pdf",
"182472_CIMUNIC-04ce24h423dAM.pdf",
"182481_DIMUNIC-04na24e224d.pdf",
"182504_DIMUNIC-04sa24g793d.pdf",
"182528_DIMUNIC-04na24b924d.pdf",
"182562_DIMUNIC-04sa24f912d.pdf",
"182582_DIMUNIC-04bn24g848d.pdf",
"182669_DIMUNIC-04sa24a186d.pdf",
"182675_DIMUNIC-04bn24g494d.pdf",
"182677_DIMUNIC-04av24f988d.pdf",
"183600_DIMUNIC-04ce24b779d.pdf",
"183608_DIMUNIC-04sa24h062d.pdf",
"182768_DIMUNIC-04av24i301d.pdf",
"182780_DIMUNIC-04av24i279d.pdf",
"182803_DIMUNIC-04ce24h939d.pdf",
"182804_DIMUNIC-04ce24h045d.pdf",
"182805_DIMUNIC-04sa24g226d.pdf",
"182840_DIMUNIC-04av24e161d.pdf",
"182855_DIMUNIC-04ce24a243d.pdf",
"182856_DIMUNIC-04sa24l860d.pdf",
"182859_DIMUNIC-04sa24h564d.pdf",
"182910_DIMUNIC-04bn24a328d.pdf",
"183043_DIMUNIC-04ce24d886d.pdf",
"183047_DIMUNIC-04ce24b667d.pdf",
"183052_DIMUNIC-04ce24d769d.pdf",
"183064_DIMUNIC-04ce24e784d.pdf",
"183103_DIMUNIC-04bn24l086d.pdf",
"183130_DIMUNIC-04sa24h703d.pdf",
"183146_DIMUNIC-04av24c105d.pdf",
"183158_DIMUNIC-04sa24i317d.pdf",
"183162_DIMUNIC-04sa24a091d.pdf",
"183164_DIMUNIC-04bn24c280d.pdf",
"183221_DIMUNIC-04ce24h459d.pdf",
"183292_DIMUNIC-04av24e605d.pdf",
"183361_DIMUNIC-04na24l460d.pdf",
"183405_DIMUNIC-04na24b076d.pdf",
"183453_DIMUNIC-04ce24g130d.pdf",
"183505_DIMUNIC-04av24f988d.pdf",
"183527_DIMUNIC-04sa24e026d.pdf",
"183575_DIMUNIC-04na24i262d.pdf",
"184294_DIMUNIC-04bn24c719d.pdf",
"184316_DIMUNIC-04ce24i056d.pdf",
"183626_DIMUNIC-04na24e054d.pdf",
"183662_DIMUNIC-04ce24e932d.pdf",
"183709_DIMUNIC-04sa24h943d.pdf",
"183710_DIMUNIC-04na24l845d.pdf",
"183727_DIMUNIC-04sa24g932d.pdf",
"183753_DIMUNIC-04av24c971d.pdf",
"183754_DIMUNIC-04av24c971d.pdf",
"183782_DIMUNIC-04sa24g939d.pdf",
"183785_CIMUNIC-04sa24g939d.pdf",
"183785_CIMUNIC-04sa24g939dAM.pdf",
"183794_DIMUNIC-04na24a617d.pdf",
"183824_DIMUNIC-04bn24b873d.pdf",
"183904_DIMUNIC-04av24i756d.pdf",
"183911_DIMUNIC-04sa24i483d.pdf",
"183915_DIMUNIC-04na24b759d.pdf",
"183932_DIMUNIC-04ce24i306d.pdf",
"183944_DIMUNIC-04av24e214d.pdf",
"183945_DIMUNIC-04sa24e767d.pdf",
"183964_DIMUNIC-04ce24b362d.pdf",
"184010_DIMUNIC-04av24c971d.pdf",
"184096_DIMUNIC-04na24i208d.pdf",
"184101_DIMUNIC-04av24f511d.pdf",
"184128_DIMUNIC-04na24i469d.pdf",
"184132_DIMUNIC-04av24e397d.pdf",
"184187_DIMUNIC-04ce24e158d.pdf",
"184237_DIMUNIC-04sa24a343d.pdf",
"184240_DIMUNIC-04sa24l377d.pdf",
"184255_DIMUNIC-04ce24i233d.pdf",
"184912_DIMUNIC-04sa24e839d.pdf",
"184915_DIMUNIC-04sa24b555d.pdf",
"184919_DIMUNIC-04sa24h644d.pdf",
"185045_DIMUNIC-04sa24f426d.pdf",
"184356_DIMUNIC-04ce24f203d.pdf",
"184387_DIMUNIC-04bn24c284d.pdf",
"184404_DIMUNIC-04av24a580d.pdf",
"184405_DIMUNIC-04ce24b715d.pdf",
"184412_DIMUNIC-04na24l142d.pdf",
"184444_DIMUNIC-04ce24f352d.pdf",
"184480_DIMUNIC-04na24c129d.pdf",
"184488_DIMUNIC-04sa24c259d.pdf",
"184508_DIMUNIC-04sa24i253d.pdf",
"184523_DIMUNIC-04na24b905d.pdf",
"184527_DIMUNIC-04na24i262d.pdf",
"184528_DIMUNIC-04na24b905d.pdf",
"184529_DIMUNIC-04av24m130d.pdf",
"184542_DIMUNIC-04na24b371d.pdf",
"184548_DIMUNIC-04bn24c106d.pdf",
"184621_DIMUNIC-04na24a064d.pdf",
"184662_DIMUNIC-04av24a566d.pdf",
"184663_DIMUNIC-04ce24a579d.pdf",
"184711_DIMUNIC-04na24l245d.pdf",
"184723_DIMUNIC-04sa24h683d.pdf",
"184739_DIMUNIC-04sa24a674d.pdf",
"184767_DIMUNIC-04av24e605d.pdf",
"184768_DIMUNIC-04sa24a484d.pdf",
"184771_DIMUNIC-04bn24d644d.pdf",
"184811_DIMUNIC-04ce24e173d.pdf",
"184847_DIMUNIC-04av24f506d.pdf",
"184880_DIMUNIC-04sa24c470d.pdf",
"184882_DIMUNIC-04av24e891d.pdf",
"184885_DIMUNIC-04bn24d650d.pdf",
"184886_CIMUNIC-04bn24d650d.pdf",
"184886_CIMUNIC-04bn24d650dAM.pdf",
"184908_DIMUNIC-04na24g812d.pdf"
]


# Per info su come Lavorare con file PDF in Python mediante libreria pypdf,
# vedi link:
# https://www.geeksforgeeks.org/working-with-pdf-files-in-python/


# Ho dovuto importare la libreria pypdf mediante il comando: pip install pypdf
# importing required classes 
from pypdf import PdfReader 


#scorro una alla volta tutti i file presenti in list_string
for file in list_string:    
    stringa= "C:/Users/Giuse/OneDrive/Desktop/Aliquota_IMU_Campania_2024" + "/" + file
    flag=0

    # creating a pdf reader object 
    reader = PdfReader(stringa) 
  
    # printing number of pages in pdf file 
    #print(len(reader.pages)) 
  
    # creating a page object 
    page = reader.pages[0] 
  
    # extracting text from page : page.extract_text()
    for x in page.extract_text().split("\n"):   # .split("\n") in questo modo 'x' prende (punta) una stringa ad ogni a capo.
        #print(x)
        if "Stabia" in x:                       # Se nel file che sta esaminando trova la stringa "Stabia" mi ritorna il nome del file e interrompe il ciclo
            print(f"\nFILE PER IMU: {file}")
            flag=1
            break
    
    if flag == 1:
        break