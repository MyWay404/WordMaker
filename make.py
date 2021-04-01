#!/usr/bin/python3
# Import Modules
try:
    import os,sys,time,random,threading,platform,readline,configparser,functools
except Exception as F:
    exit("\x1b[1;31m   [!] \x1b[0;32m%s"%(F)+"\x1b[0;39m")
# Color
A = "\x1b[1;32m"
B = "\x1b[1;31m"
C = "\x1b[1;33m"
D = "\x1b[1;36m"
E = "\x1b[0;39m"
rand = (A,B,C,D)
W = random.choice(rand)
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
BR = W+"""
	      __        __            _ _ _     _
	      \ \      / /__  _ __ __| | (_)___| |_
	       \ \ /\ / / _ \| '__/ _` | | / __| __|
	        \ V  V / (_) | | | (_| | | \__ \ |_
	         \_/\_/ \___/|_|  \__,_|_|_|___/\__|
"""+E
# Create wordlist
CONFIG = {}
def informations():
    os.system(clr)
    print(BR)
    profile = {}
    print("   "+"\x1b[1;39m-"*64+E)
    print(B+"   [!] "+A+"Insert the information about the victim to make a dictionary")
    print(B+"   [!] "+A+"If you don't know all the info,just hit enter when asked! ;)\r\n")
    name = input(C+"   [+] "+D+"First Name: "+E)
    while len(name) == 0 or name == " " or name == "  " or name == "   ":
        print(B+"   [!] "+A+"You must enter a name at least!")
        name = input(C+"   [+] "+D+"Name: "+E)
    profile["name"] = str(name)
    profile["surname"] = input(C+"   [+] "+D+"Surname: "+E)
    profile["nick"] = input(C+"   [+] "+D+"Nickname: "+E)
    birthdate = input(C+"   [+] "+D+"Birthdate (DDMMYYYY): "+E)
    while len(birthdate) != 0 and len(birthdate) != 8:
        print(B+"   [!] "+A+"You must enter 8 digits for birthday!")
        birthdate = input(C+"   [+] "+D+"Birthdate (DDMMYYYY): "+E)
    profile["birthdate"] = str(birthdate)
    print("\r\n")
    profile["wife"] = input(C+"   [+] "+D+"Partners) name: "+E)
    profile["wifen"] = input(C+"   [+] "+D+"Partners) nickname: "+E)
    wifeb = input(C+"   [+] "+D+"Partners) birthdate (DDMMYYYY): "+E)
    while len(wifeb) != 0 and len(wifeb) != 8:
        print(B+"   [!] "+A+"You must enter 8 digits for birthday!")
        wifeb = input(C+"   [+] "+D+"Partners birthdate (DDMMYYYY): "+E)
    profile["wifeb"] = str(wifeb)
    print("\r\n")
    profile["kid"] = input(C+"   [+] "+D+"Child's name: "+E)
    profile["kidn"] = input(C+"   [+] "+D+"Child's nickname: "+E)
    kidb = input(C+"   [+] "+D+"Child's birthdate (DDMMYYYY): "+E)
    while len(kidb) != 0 and len(kidb) != 8:
        print(B+"   [!] "+A+"You must enter 8 digits for birthday!")
        kidb = input(C+"   [+] "+D+"Child's birthdate (DDMMYYYY): "+E)
    profile["kidb"] = str(kidb)
    print("\r\n")
    profile["pet"] = input(C+"   [+] "+D+"Pet's name: "+E)
    profile["company"] = input(C+"   [+] "+D+"Company name: "+E)
    print("\r\n")
    profile["words"] = [""]
    words1 = input(C+"   [+] "+D+"Do you want to add some key words about the victim? Y/[N]: "+E)
    words2 = ""
    if words1.lower() == "y":
        print(B+"   [+] "+A+"Please enter the words,separated by comma."+E)
        words2 = input(C+"   [+] "+D+"[i.e. hacker,juice,black],spaces will be removed: "+E).replace(" ","")
    profile["words"] = words2.split(",")
    profile["spechars1"] = input(C+"   [+] "+D+"Do you want to add special chars at the end of words? Y/[N]: "+E)
    profile["randnum"] = input(C+"   [+] "+D+"Do you want to add some random numbers at the end of words? Y/[N]:"+E)
    profile["leetmode"] = input(C+"   [+] "+D+"Leet mode? (i.e. leet = 1337) Y/[N]: "+E)
    print("\r\n")
    generate(profile)
def read_config(file):
    if os.path.isfile(file) == True:
        config = configparser.ConfigParser()
        config.read(file)
        CONFIG["global"] = {
            "years": config.get("years","years").split(","),
            "chars": config.get("specialchars","chars").split(","),
            "numfrom": config.getint("nums","from"),
            "numto": config.getint("nums","to"),
            "wcfrom": config.getint("nums","wcfrom"),
            "wcto": config.getint("nums","wcto")
        }
        leet = functools.partial(config.get,"leet")
        leetc = {}
        letters = {"a","i","e","t","o","s","g","z"}
        for letter in letters:
            leetc[letter] = config.get("leet",letter)
        CONFIG["LEET"] = leetc
        return True
    else:
        print(B+"   [!] "+A+"Configuration file "+C+file+A+" not found!\n"+B+"   [!] "+A+"Exiting "+E+"...")
        sys.exit()
        return False
def make_leet(x):
    for letter,leetletter in CONFIG["LEET"].items():
        x = x.replace(letter,leetletter)
    return x
def concats(seq,start,stop):
    for mystr in seq:
        for num in range(start,stop):
            yield mystr+str(num)
def komb(seq,start,special=""):
    for mystr in seq:
        for mystr1 in start:
            yield mystr+special+mystr1
def generate(profile):
    chars = CONFIG["global"]["chars"]
    years = CONFIG["global"]["years"]
    numfrom = CONFIG["global"]["numfrom"]
    numto = CONFIG["global"]["numto"]
    profile["spechars"] = []
    if profile["spechars1"].lower() == "y":
        for spec1 in chars:
            profile["spechars"].append(spec1)
            for spec2 in chars:
                profile["spechars"].append(spec1+spec2)
                for spec3 in chars:
                    profile["spechars"].append(spec1+spec2+spec3)
    print(B+"   [!] "+A+"Now making a dictionary"+E+" ...")
    birthdate_yy = profile["birthdate"][-2:]
    birthdate_yyy = profile["birthdate"][-3:]
    birthdate_yyyy = profile["birthdate"][-4:]
    birthdate_xd = profile["birthdate"][1:2]
    birthdate_xm = profile["birthdate"][3:4]
    birthdate_dd = profile["birthdate"][:2]
    birthdate_mm = profile["birthdate"][2:4]
    wifeb_yy = profile["wifeb"][-2:]
    wifeb_yyy = profile["wifeb"][-3:]
    wifeb_yyyy = profile["wifeb"][-4:]
    wifeb_xd = profile["wifeb"][1:2]
    wifeb_xm = profile["wifeb"][3:4]
    wifeb_dd = profile["wifeb"][:2]
    wifeb_mm = profile["wifeb"][2:4]
    kidb_yy = profile["kidb"][-2:]
    kidb_yyy = profile["kidb"][-3:]
    kidb_yyyy = profile["kidb"][-4:]
    kidb_xd = profile["kidb"][1:2]
    kidb_xm = profile["kidb"][3:4]
    kidb_dd = profile["kidb"][:2]
    kidb_mm = profile["kidb"][2:4]
    nameup = profile["name"].title()
    surnameup = profile["surname"].title()
    nickup = profile["nick"].title()
    wifeup = profile["wife"].title()
    wifenup = profile["wifen"].title()
    kidup = profile["kid"].title()
    kidnup = profile["kidn"].title()
    petup = profile["pet"].title()
    companyup = profile["company"].title()
    wordsup = []
    wordsup = list(map(str.title,profile["words"]))
    word = profile["words"]+wordsup
    rev_name = profile["name"][::-1]
    rev_nameup = nameup[::-1]
    rev_nick = profile["nick"][::-1]
    rev_nickup = nickup[::-1]
    rev_wife = profile["wife"][::-1]
    rev_wifeup = wifeup[::-1]
    rev_kid = profile["kid"][::-1]
    rev_kidup = kidup[::-1]
    reverse = [
        rev_name,
        rev_nameup,
        rev_nick,
        rev_nickup,
        rev_wife,
        rev_wifeup,
        rev_kid,
        rev_kidup,
    ]
    rev_n = [rev_name,rev_nameup,rev_nick,rev_nickup]
    rev_w = [rev_wife,rev_wifeup]
    rev_k = [rev_kid,rev_kidup]
    bds = [
        birthdate_yy,
        birthdate_yyy,
        birthdate_yyyy,
        birthdate_xd,
        birthdate_xm,
        birthdate_dd,
        birthdate_mm,
    ]
    bdss = []
    for bds1 in bds:
        bdss.append(bds1)
        for bds2 in bds:
            if bds.index(bds1) != bds.index(bds2):
                bdss.append(bds1+bds2)
                for bds3 in bds:
                    if (
                        bds.index(bds1) != bds.index(bds2)
                        and bds.index(bds2) != bds.index(bds3)
                        and bds.index(bds1) != bds.index(bds3)
                    ):
                        bdss.append(bds1+bds2+bds3)
    wbds = [wifeb_yy,wifeb_yyy,wifeb_yyyy,wifeb_xd,wifeb_xm,wifeb_dd,wifeb_mm]
    wbdss = []
    for wbds1 in wbds:
        wbdss.append(wbds1)
        for wbds2 in wbds:
            if wbds.index(wbds1) != wbds.index(wbds2):
                wbdss.append(wbds1+wbds2)
                for wbds3 in wbds:
                    if (
                        wbds.index(wbds1) != wbds.index(wbds2)
                        and wbds.index(wbds2) != wbds.index(wbds3)
                        and wbds.index(wbds1) != wbds.index(wbds3)
                    ):
                        wbdss.append(wbds1+wbds2+wbds3)
    kbds = [kidb_yy,kidb_yyy,kidb_yyyy,kidb_xd,kidb_xm,kidb_dd,kidb_mm]
    kbdss = []
    for kbds1 in kbds:
        kbdss.append(kbds1)
        for kbds2 in kbds:
            if kbds.index(kbds1) != kbds.index(kbds2):
                kbdss.append(kbds1+kbds2)
                for kbds3 in kbds:
                    if (
                        kbds.index(kbds1) != kbds.index(kbds2)
                        and kbds.index(kbds2) != kbds.index(kbds3)
                        and kbds.index(kbds1) != kbds.index(kbds3)
                    ):
                        kbdss.append(kbds1+kbds2+kbds3)
    kombinaac = [profile["pet"],petup,profile["company"],companyup]
    kombina = [
        profile["name"],
        profile["surname"],
        profile["nick"],
        nameup,
        surnameup,
        nickup,
    ]
    kombinaw = [
        profile["wife"],
        profile["wifen"],
        wifeup,
        wifenup,
        profile["surname"],
        surnameup,
    ]
    kombinak = [
        profile["kid"],
        profile["kidn"],
        kidup,
        kidnup,
        profile["surname"],
        surnameup,
    ]
    kombinaa = []
    for kombina1 in kombina:
        kombinaa.append(kombina1)
        for kombina2 in kombina:
            if kombina.index(kombina1) != kombina.index(kombina2) and kombina.index(
                kombina1.title()
            ) != kombina.index(kombina2.title()):
                kombinaa.append(kombina1+kombina2)
    kombinaaw = []
    for kombina1 in kombinaw:
        kombinaaw.append(kombina1)
        for kombina2 in kombinaw:
            if kombinaw.index(kombina1) != kombinaw.index(kombina2) and kombinaw.index(
                kombina1.title()
            ) != kombinaw.index(kombina2.title()):
                kombinaaw.append(kombina1+kombina2)
    kombinaak = []
    for kombina1 in kombinak:
        kombinaak.append(kombina1)
        for kombina2 in kombinak:
            if kombinak.index(kombina1) != kombinak.index(kombina2) and kombinak.index(
                kombina1.title()
            ) != kombinak.index(kombina2.title()):
                kombinaak.append(kombina1+kombina2)
    kombi = {}
    kombi[1] = list(komb(kombinaa,bdss))
    kombi[1] += list(komb(kombinaa,bdss,"_"))
    kombi[2] = list(komb(kombinaaw,wbdss))
    kombi[2] += list(komb(kombinaaw,wbdss,"_"))
    kombi[3] = list(komb(kombinaak,kbdss))
    kombi[3] += list(komb(kombinaak,kbdss,"_"))
    kombi[4] = list(komb(kombinaa,years))
    kombi[4] += list(komb(kombinaa,years,"_"))
    kombi[5] = list(komb(kombinaac,years))
    kombi[5] += list(komb(kombinaac,years,"_"))
    kombi[6] = list(komb(kombinaaw,years))
    kombi[6] += list(komb(kombinaaw,years,"_"))
    kombi[7] = list(komb(kombinaak,years))
    kombi[7] += list(komb(kombinaak,years,"_"))
    kombi[8] = list(komb(word,bdss))
    kombi[8] += list(komb(word,bdss,"_"))
    kombi[9] = list(komb(word,wbdss))
    kombi[9] += list(komb(word,wbdss,"_"))
    kombi[10] = list(komb(word,kbdss))
    kombi[10] += list(komb(word,kbdss,"_"))
    kombi[11] = list(komb(word,years))
    kombi[11] += list(komb(word,years,"_"))
    kombi[12] = [""]
    kombi[13] = [""]
    kombi[14] = [""]
    kombi[15] = [""]
    kombi[16] = [""]
    kombi[21] = [""]
    if profile["randnum"].lower() == "y":
        kombi[12] = list(concats(word,numfrom,numto))
        kombi[13] = list(concats(kombinaa,numfrom,numto))
        kombi[14] = list(concats(kombinaac,numfrom,numto))
        kombi[15] = list(concats(kombinaaw,numfrom,numto))
        kombi[16] = list(concats(kombinaak,numfrom,numto))
        kombi[21] = list(concats(reverse,numfrom,numto))
    kombi[17] = list(komb(reverse,years))
    kombi[17] += list(komb(reverse,years,"_"))
    kombi[18] = list(komb(rev_w,wbdss))
    kombi[18] += list(komb(rev_w,wbdss,"_"))
    kombi[19] = list(komb(rev_k,kbdss))
    kombi[19] += list(komb(rev_k,kbdss,"_"))
    kombi[20] = list(komb(rev_n,bdss))
    kombi[20] += list(komb(rev_n,bdss,"_"))
    komb001 = [""]
    komb002 = [""]
    komb003 = [""]
    komb004 = [""]
    komb005 = [""]
    komb006 = [""]
    if len(profile["spechars"]) > 0:
        komb001 = list(komb(kombinaa,profile["spechars"]))
        komb002 = list(komb(kombinaac,profile["spechars"]))
        komb003 = list(komb(kombinaaw,profile["spechars"]))
        komb004 = list(komb(kombinaak,profile["spechars"]))
        komb005 = list(komb(word,profile["spechars"]))
        komb006 = list(komb(reverse,profile["spechars"]))
    print(B+"   [!] "+A+"Sorting list and removing duplicates "+E+"...")
    komb_unique = {}
    for i in range(1,22):
        komb_unique[i] = list(dict.fromkeys(kombi[i]).keys())
    komb_unique01 = list(dict.fromkeys(kombinaa).keys())
    komb_unique02 = list(dict.fromkeys(kombinaac).keys())
    komb_unique03 = list(dict.fromkeys(kombinaaw).keys())
    komb_unique04 = list(dict.fromkeys(kombinaak).keys())
    komb_unique05 = list(dict.fromkeys(word).keys())
    komb_unique07 = list(dict.fromkeys(komb001).keys())
    komb_unique08 = list(dict.fromkeys(komb002).keys())
    komb_unique09 = list(dict.fromkeys(komb003).keys())
    komb_unique010 = list(dict.fromkeys(komb004).keys())
    komb_unique011 = list(dict.fromkeys(komb005).keys())
    komb_unique012 = list(dict.fromkeys(komb006).keys())
    uniqlist = (
        bdss
       +wbdss
       +kbdss
       +reverse
       +komb_unique01
       +komb_unique02
       +komb_unique03
       +komb_unique04
       +komb_unique05
    )
    for i in range(1,21):
        uniqlist += komb_unique[i]
    uniqlist += (
        komb_unique07
       +komb_unique08
       +komb_unique09
       +komb_unique010
       +komb_unique011
       +komb_unique012
    )
    unique_lista = list(dict.fromkeys(uniqlist).keys())
    unique_leet = []
    if profile["leetmode"].lower() == "y":
        for (
            x
        ) in (
            unique_lista
        ):
            x = make_leet(x)
            unique_leet.append(x)
    unique_list = unique_lista+unique_leet
    unique_list_finished = []
    unique_list_finished = [
        x
        for x in unique_list
        if len(x) > 5 and len(x) < 12
    ]
    print_to_file(profile["name"]+".txt",unique_list_finished)
def print_to_file(filename,unique_list_finished):
    f = open(filename.lower(),"w")
    unique_list_finished.sort()
    f.write(os.linesep.join(unique_list_finished))
    f.close()
    f = open(filename.lower(),"r")
    lines = 0
    for line in f:
        lines += 1
    f.close()
    print(B+"   [!] "+A+"Saving dictionary to "+C+filename.lower()+A+",counting "+C+str(lines)+A+" words."+E)
    print("\r\n")
    print(B+"\n   [!] "+A+"Now load your pistolero with "+C+filename.lower()+A+" and shoot! Good luck!"+E)
if __name__ == "__main__":
    try:
        read_config(os.path.join(os.path.dirname(os.path.realpath(__file__)),"make.cfg"))
        informations()
    except KeyboardInterrupt:
        exit(B+"\n   [!] "+A+"Keyboard Interrupt."+E)
    except Exception as F:
        exit(B+"\n   [!] "+A+"%s"%(F)+E)
else:
    pass
