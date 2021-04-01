#!/usr/bin/python3
# Import Modules
try:
    import os,sys,time,random,urllib.request,itertools,threading,platform,readline
except Exception as F:
    exit("\x1b[1;31m   [!] \x1b[0;32m%s"%(F)+"\x1b[0;39m")
# Color
A = "\x1b[1;32m"
B = "\x1b[1;31m"
C = "\x1b[1;33m"
D = "\x1b[1;36m"
E = "\x1b[0;39m"
rand = (A,B,C,D)
R = random.choice(rand)
W = "\x1b[1;39m"
# Adaptor
name = platform.system()
if name == "Windows":
    clr = "cls"
else:
    clr = "clear"
if sys.version_info[0] != 3:
    exit(B+"   [!] "+A+"This tool work only on python3!"+E)
else:
    pass
# Banner
BR = R+"""
        __        __            _           ____
        \ \      / /__  _ __ __| |         |  _ \  _____      ___ __
         \ \ /\ / / _ \| '__/ _` |  _____  | | | |/ _ \ \ /\ / / '_ \ 
          \ V  V / (_) | | | (_| | |_____| | |_| | (_) \ V  V /| | | |
           \_/\_/ \___/|_|  \__,_|         |____/ \___/ \_/\_/ |_| |_|
"""
# Wordlist
choose = (f"""
\t {B}[01]{A}  Moby           {B}[14]{A}     French         {B}[27]{A}     Places
\t {B}[02]{A}  Afrikaans      {B}[15]{A}     German         {B}[28]{A}     Polish
\t {B}[03]{A}  American       {B}[16]{A}     Hindi          {B}[29]{A}     Random
\t {B}[04]{A}  Aussie         {B}[17]{A}     Hungarian      {B}[30]{A}     Religion
\t {B}[05]{A}  Chinese        {B}[18]{A}     Italian        {B}[31]{A}     Russian
\t {B}[06]{A}  Computer       {B}[19]{A}     Japanese       {B}[32]{A}     Science
\t {B}[07]{A}  Croatian       {B}[20]{A}     Latin          {B}[33]{A}     Spanish
\t {B}[08]{A}  Czech          {B}[21]{A}     Literature     {B}[34]{A}     Swahili
\t {B}[09]{A}  Danish         {B}[22]{A}     MovieTV        {B}[35]{A}     Swedish
\t {B}[10]{A}  Databases      {B}[23]{A}     Music          {B}[36]{A}     Turkish
\t {B}[11]{A}  Dictionaries   {B}[24]{A}     Names          {B}[37]{A}     Yiddish
\t {B}[12]{A}  Dutch          {B}[25]{A}     Net            {B}[38]{A}     Indonesian
\t {B}[13]{A}  Finnish        {B}[26]{A}     Norwegian      {B}[00]{A}     Exit\n"""+E)
def mkdir_if_not_exists(dire):
    if os.path.isdir(dire) == False:
        os.mkdir(dire)
def load():
    for i in itertools.cycle(["|","/","-","\\"]):
        sys.stdout.write(B+"\r   [+] "+A+"Downloading file \x1b[1;39m"+i)
        sys.stdout.flush()
        time.sleep(0.1)
def download_http(url,tgt):
    done = False
    loading = threading.Thread(target=load)
    loading.daemon = True
    loading.start()
    webFile = urllib.request.urlopen(url)
    localFile = open(tgt,"wb")
    localFile.write(webFile.read())
    webFile.close()
    localFile.close()
    done = True
    if done == True:
        print()
        sys.stdout.write(B+"\r   [+] "+A+"Succes file saved as "+C+tgt+E+"\n")
    else:
        pass
    done = None
def indonesia(filedown):
    url = "https://raw.githubusercontent.com/H-TCM/Hash/main/wordlist.txt"
    dire = "dictionaries/indonesian/"
    tgt = dire+"wordlist.txt"
    mkdir_if_not_exists("dictionaries/")
    mkdir_if_not_exists(dire)
    download_http(url,tgt)
def download_wordlist_http(filedown):
    mkdir_if_not_exists("dictionaries/")
    list = {
        1: (
            "Moby",
            (
                "mhyph.tar.gz",
                "mlang.tar.gz",
                "moby.tar.gz",
                "mpos.tar.gz",
                "mpron.tar.gz",
                "mthes.tar.gz",
                "mwords.tar.gz",
            ),
        ),
        2: ("afrikaans",("afr_dbf.zip",)),
        3: ("american",("dic-0294.tar.gz",)),
        4: ("aussie",("oz.gz",)),
        5: ("chinese",("chinese.gz",)),
        6: (
            "computer",
            (
                "Domains.gz",
                "Dosref.gz",
                "Ftpsites.gz",
                "Jargon.gz",
                "common-passwords.txt.gz",
                "etc-hosts.gz",
                "foldoc.gz",
                "language-list.gz",
                "unix.gz",
            ),
        ),
        7: ("croatian",("croatian.gz",)),
        8: ("czech",("czech-wordlist-ascii-cstug-novak.gz",)),
        9: ("danish",("danish.words.gz","dansk.zip")),
        10: (
            "databases",
            ("acronyms.gz","att800.gz","computer-companies.gz","world_heritage.gz"),
        ),
        11: (
            "dictionaries",
            (
                "Antworth.gz",
                "CRL.words.gz",
                "Roget.words.gz",
                "Unabr.dict.gz",
                "Unix.dict.gz",
                "englex-dict.gz",
                "knuth_britsh.gz",
                "knuth_words.gz",
                "pocket-dic.gz",
                "shakesp-glossary.gz",
                "special.eng.gz",
                "words-english.gz",
            ),
        ),
        12: ("dutch",("words.dutch.gz",)),
        13: (
            "finnish",
            ("finnish.gz","firstnames.finnish.gz","words.finnish.FAQ.gz"),
        ),
        14: ("french",("dico.gz",)),
        15: ("german",("deutsch.dic.gz","germanl.gz","words.german.gz")),
        16: ("hindi",("hindu-names.gz",)),
        17: ("hungarian",("hungarian.gz",)),
        18: ("italian",("words.italian.gz",)),
        19: ("japanese",("words.japanese.gz",)),
        20: ("latin",("wordlist.aug.gz",)),
        21: (
            "literature",
            (
                "LCarrol.gz",
                "Paradise.Lost.gz",
                "aeneid.gz",
                "arthur.gz",
                "cartoon.gz",
                "cartoons-olivier.gz",
                "charlemagne.gz",
                "fable.gz",
                "iliad.gz",
                "myths-legends.gz",
                "odyssey.gz",
                "sf.gz",
                "shakespeare.gz",
                "tolkien.words.gz",
            ),
        ),
        22: ("movieTV",("Movies.gz","Python.gz","Trek.gz")),
        23: (
            "music",
            (
                "music-classical.gz",
                "music-country.gz",
                "music-jazz.gz",
                "music-other.gz",
                "music-rock.gz",
                "music-shows.gz",
                "rock-groups.gz",
            ),
        ),
        24: (
            "names",
            (
                "ASSurnames.gz",
                "Congress.gz",
                "Family-Names.gz",
                "Given-Names.gz",
                "actor-givenname.gz",
                "actor-surname.gz",
                "cis-givenname.gz",
                "cis-surname.gz",
                "crl-names.gz",
                "famous.gz",
                "fast-names.gz",
                "female-names-kantr.gz",
                "female-names.gz",
                "givennames-ol.gz",
                "male-names-kantr.gz",
                "male-names.gz",
                "movie-characters.gz",
                "names.french.gz",
                "names.hp.gz",
                "other-names.gz",
                "shakesp-names.gz",
                "surnames-ol.gz",
                "surnames.finnish.gz",
                "usenet-names.gz",
            ),
        ),
        25: (
            "net",
            (
                "hosts-txt.gz",
                "inet-machines.gz",
                "usenet-loginids.gz",
                "usenet-machines.gz",
                "uunet-sites.gz",
            ),
        ),
        26: ("norwegian",("words.norwegian.gz",)),
        27: (
            "places",
            (
                "Colleges.gz",
                "US-counties.gz",
                "World.factbook.gz",
                "Zipcodes.gz",
                "places.gz",
            ),
        ),
        28: ("polish",("words.polish.gz",)),
        29: (
            "random",
            (
                "Ethnologue.gz",
                "abbr.gz",
                "chars.gz",
                "dogs.gz",
                "drugs.gz",
                "junk.gz",
                "numbers.gz",
                "phrases.gz",
                "sports.gz",
                "statistics.gz",
            ),
        ),
        30: ("religion",("Koran.gz","kjbible.gz","norse.gz")),
        31: ("russian",("russian.lst.gz","russian_words.koi8.gz")),
        32: (
            "science",
            (
                "Acr-diagnosis.gz",
                "Algae.gz",
                "Bacteria.gz",
                "Fungi.gz",
                "Microalgae.gz",
                "Viruses.gz",
                "asteroids.gz",
                "biology.gz",
                "tech.gz",
            ),
        ),
        33: ("spanish",("words.spanish.gz",)),
        34: ("swahili",("swahili.gz",)),
        35: ("swedish",("words.swedish.gz",)),
        36: ("turkish",("turkish.dict.gz",)),
        37: ("yiddish",("yiddish.gz",)),
    }
    intfiledown = int(filedown)
    if intfiledown in list:
        dire = "dictionaries/"+list[intfiledown][0]+"/"
        mkdir_if_not_exists(dire)
        files_to_download = list[intfiledown][1]
        for fi in files_to_download:
            url = "http://ftp.funet.fi/pub/unix/security/passwd/crack/dictionaries/"+list[intfiledown][0]+"/"+fi
            tgt = dire+fi
            download_http(url,tgt)
    else:
        print(B+"   [!] "+A+"Exiting "+E+"...")
def menu():
    try:
        os.system(clr)
        print(BR)
        print(C+"\t\t[!] "+D+"Here is a list of avaiable word list: "+E)
        print(choose)
        filedown = input(C+"   [!] "+D+"Enter number: "+E)
        while int(filedown) == 38:
            indonesia(filedown)
        while int(filedown) == 0:
            exit(B+"\n   [!] "+A+"Exiting "+E+"...")
        while int(filedown) > 38 or int(filedown) < 0:
            print(B+"   [!] "+A+"Wrong choice."+E)
            filedown = input(C+"   [!] "+D+"Enter number: "+E)
        filedown = str(filedown)
        download_wordlist_http(filedown)
        return filedown
    except (KeyboardInterrupt,EOFError):
        exit(B+"\n   [!] "+A+"Exiting "+E+"...")
    except Exception as F:
        exit(B+"\n   [!] "+A+"%s"%(F)+E)
if __name__ == "__main__":
    menu()
else:
    pass
