import pandas as pd

from akshara.varnakaarya import get_vinyaasa, get_shabda

from pratyaahaara import expand_pratyahaara
from varna import *

# from vinyaasa import get_shabda, get_vinyaasa


def get_sthiti(df):
    return list(df["स्थिति"])[-1]


def remove_avasaana(s):

    f = 0
    for ii in range(len(s)):
        if s[ii] == " ":
            f = ii

    del s[f]

    return s


def aadesh(s, ii, aa):

    del s[ii]
    s[ii:ii] = get_vinyaasa(aa)

    return s


def pre_processing(df):
    return get_vinyaasa(list(df["स्थिति"])[-1])


def post_processing(df, s, name, number):

    s = get_shabda(s)
    t = "[[" + name + " (" + number + ")]]"
    row = {"स्थिति": s, "सूत्र": t}
    # df = df.append(row, ignore_index=True)
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)

    return df


def तस्य_लोपः(df, ii):

    s = pre_processing(df)

    del s[ii]

    df = post_processing(df, s, "तस्य लोपः", "1.3.9")

    return df


def इको_यणचि(df):

    s = pre_processing(df)

    s = remove_avasaana(s)

    for ii in range(len(s) - 1):

        if s[ii] in expand_pratyahaara("इक्") and s[ii + 1] in expand_pratyahaara("अच्"):
            if s[ii] == "इ" or s[ii] == "ई":
                s = aadesh(s, ii, "य्")
            elif s[ii] == "उ" or s[ii] == "ऊ":
                s = aadesh(s, ii, "व्")
            elif s[ii] == "ऋ" or s[ii] == "ॠ":
                s = aadesh(s, ii, "र्")
            elif s[ii] == "ऌ":
                s = aadesh(s, ii, "ल्")

    df = post_processing(df, s, "इको यणचि", "6.1.77")

    return df


def एचोऽयवायावः(df):

    s = pre_processing(df)

    for ii in range(len(s) - 1):

        if (
            s[ii] in expand_pratyahaara("एच्") and s[ii + 1] in expand_pratyahaara("अच्")
        ) or (
            s[ii] in expand_pratyahaara("एच्")
            and s[ii + 1] == " "
            and s[ii + 2] in expand_pratyahaara("अच्")
        ):
            if s[ii] == "ए":
                del s[ii]
                s[ii:ii] = get_vinyaasa("अय्")
            elif s[ii] == "ओ":
                del s[ii]
                s[ii:ii] = get_vinyaasa("अव्")
            elif s[ii] == "ऐ":
                del s[ii]
                s[ii:ii] = get_vinyaasa("आय्")
            elif s[ii] == "औ":
                del s[ii]
                s[ii:ii] = get_vinyaasa("आव्")

    df = post_processing(df, s, "एचोऽयवायावः", "6.1.78")

    if " " in s:
        df = लोपः_शाकल्यस्य(df)

    return df


def आद्गुणः(df):

    s = pre_processing(df)

    # print(s)

    for ii in range(len(s) - 1):

        if (s[ii] in ["अ", "आ"] and s[ii + 1] in expand_pratyahaara("अच्")) or (
            s[ii] in ["अ", "आ"]
            and s[ii + 1] == " "
            and s[ii + 2] in expand_pratyahaara("अच्")
        ):
            break

    if s[ii + 1] == " ":
        del s[ii + 1]

    temp = s[ii + 1]
    del s[ii + 1]

    if temp in ["इ", "ई"]:
        aa = "ए"
    if temp in ["उ", "ऊ"]:
        aa = "ओ"
    if temp in ["ऋ", "ॠ"]:
        aa = "अर्"
    if temp in ["ऌ"]:
        aa = "अल्"

    s = aadesh(s, ii, aa)

    df = post_processing(df, s, "आद्गुणः", "6.1.87")

    return df


def वृद्धिरेचि(df):

    s = pre_processing(df)

    for ii in range(len(s) - 1):

        if (s[ii] in ["अ", "आ"] and s[ii + 1] in expand_pratyahaara("एच्")) or (
            s[ii] in ["अ", "आ"]
            and s[ii + 1] == " "
            and s[ii + 2] in expand_pratyahaara("एच्")
        ):
            break

    if s[ii + 1] == " ":
        del s[ii + 1]

    temp = s[ii + 1]
    del s[ii + 1]

    if temp in ["ए", "ऐ"]:
        aa = "ऐ"
    if temp in ["ओ", "औ"]:
        aa = "औ"

    s = aadesh(s, ii, aa)

    df = post_processing(df, s, "वृद्धिरेचि", "6.1.88")

    return df


def अकः_सवर्णे_दीर्घः(df):

    s = pre_processing(df)

    for ii in range(len(s) - 1):

        if (
            s[ii] in expand_pratyahaara("अक्") and s[ii + 1] in expand_pratyahaara("अक्")
        ) or (
            s[ii] in expand_pratyahaara("अक्")
            and s[ii + 1] == " "
            and s[ii + 2] in expand_pratyahaara("अक्")
        ):
            break

    if s[ii + 1] == " ":
        del s[ii + 1]

    temp = s[ii + 1]
    del s[ii + 1]

    if temp in ["अ", "आ"] and s[ii] in ["अ", "आ"]:
        aa = "आ"
    if temp in ["इ", "ई"] and s[ii] in ["इ", "ई"]:
        aa = "ई"
    if temp in ["उ", "ऊ"] and s[ii] in ["उ", "ऊ"]:
        aa = "ऊ"
    if temp in ["ऋ", "ॠ", "ऌ"] and s[ii] in ["ऋ", "ॠ", "ऌ"]:
        aa = "ॠ"

    aadesh(s, ii, aa)

    df = post_processing(df, s, "अकः सवर्णे दीर्घः", "6.1.101")

    return df


def एङः_पदान्तादति(df):

    s = pre_processing(df)

    ii = s.index(" ")

    if s[ii - 1] in expand_pratyahaara("एङ्") and s[ii + 1] == "अ":
        del s[ii]
        aadesh(s, ii, "ऽ")

    df = post_processing(df, s, "एङः पदान्तादति", "6.1.109")

    return df


def अतो_रोरप्लुतादप्लुते(df):

    s = pre_processing(df)

    if " " in s:

        ii = s.index(" ")
        if s[ii - 2] == "अ" and s[ii + 1] == "अ" and s[ii - 1] == "र्":
            aadesh(s, ii - 1, " उ")

    # print(s)

    df = post_processing(df, s, "अतो रोरप्लुतादप्लुते", "6.1.113")

    df = आद्गुणः(df)
    df = एङः_पदान्तादति(df)

    return df


def हशि_च(df):

    s = pre_processing(df)

    if " " in s:

        ii = s.index(" ")
        if (
            s[ii - 2] == "अ"
            and s[ii + 1] in expand_pratyahaara("हश्")
            and s[ii - 1] == "र्"
        ):
            aadesh(s, ii - 1, " उ")

    df = post_processing(df, s, "हशि च", "6.1.114")

    df = आद्गुणः(df)

    return df


def एतत्तदोः_सुलोपोऽकोरनञ्समासे_हलि(df):

    s = pre_processing(df)

    ii = s.index(" ")

    if s[ii - 1] == "स्" and s[ii + 1] in expand_pratyahaara("हल्"):
        del s[ii - 1]

    df = post_processing(df, s, "एतत्तदोः सुलोपोऽकोरनञ्समासे हलि", "6.1.132")

    return df


def झलां_जशोऽन्ते(df):

    s = pre_processing(df)

    if " " in s:

        ii = s.index(" ")

        if s[ii - 1] in expand_pratyahaara("झल्"):

            if s[ii - 1] in ["क्", "ख्", "ग्", "घ्"]:
                aa = "ग्"
            if s[ii - 1] in ["ट्", "ठ्", "ड्", "ढ्"]:
                aa = "ड्"
            if s[ii - 1] in ["त्", "थ्", "द्", "ध्"]:
                aa = "द्"
            if s[ii - 1] in ["प्", "फ्", "ब्", "भ्"]:
                aa = "ब्"
            if s[ii - 1] == "ष्":
                aa = "ड्"

            s = aadesh(s, ii - 1, aa)

    elif s[len(s) - 1] in expand_pratyahaara("झल्"):

        ii = len(s)

        if s[ii - 1] in ["क्", "ख्", "ग्", "घ्"]:
            aa = "ग्"
        if s[ii - 1] in ["ट्", "ठ्", "ड्", "ढ्"]:
            aa = "ड्"
        if s[ii - 1] in ["त्", "थ्", "द्", "ध्"]:
            aa = "द्"
        if s[ii - 1] in ["प्", "फ्", "ब्", "भ्"]:
            aa = "ब्"
        if s[ii - 1] == "ष्":
            aa = "ड्"

        s = aadesh(s, ii - 1, aa)

    df = post_processing(df, s, "झलां जशोऽन्ते", "8.2.39")

    if " " in s:

        ii = s.index(" ")

        l1 = ["स्", "त्", "थ्", "द्", "ध्", "न्"]
        l2 = ["श्", "च्", "छ्", "ज्", "झ्", "ञ्"]
        l3 = ["ष्", "ट्", "ठ्", "ड्", "ढ्", "ण्"]

        if (s[ii - 1] in l1 and s[ii + 1] in l2) or (
            s[ii - 1] in l2 and s[ii + 1] in l1
        ):
            df = स्तोः_श्चुना_श्चुः(df)
        elif (s[ii - 1] in l1 and s[ii + 1] in l3) or (
            s[ii - 1] in l3 and s[ii + 1] in l1
        ):
            df = ष्टुना_ष्टुः(df)

    s = pre_processing(df)

    if " " in s:

        ii = s.index(" ")

        if s[ii - 1] in expand_pratyahaara("यर्") and s[ii + 1] in expand_pratyahaara(
            "ञम्"
        ):
            df = यरोऽनुनासिकेऽनुनासिको_वा(df)

        if s[ii + 1] in expand_pratyahaara("खर्"):
            df = खरि_च(df)

        if s[ii + 1] == "ल्":
            df = तोर्लि(df)

        if s[ii - 1] in expand_pratyahaara("झय्") and s[ii + 1] == "ह्":
            df = झयो_होऽन्यतरस्याम्(df)

    elif " " not in s:
        df = वाऽवसाने(df)

    return df


def ससजुषो_रुः(df):

    s = pre_processing(df)

    if " " in s and s[s.index(" ") - 1] == "स्":
        ii = s.index(" ") - 1
    elif s[-1] == "स्":
        ii = len(s) - 1

    s = aadesh(s, ii, "रुँ")

    df = post_processing(df, s, "ससजुषो रुः", "8.2.66")

    df = तस्य_लोपः(df, ii + 1)

    return df


def नश्छव्यप्रशान्(df):

    s = pre_processing(df)

    ii = s.index(" ")

    if s[ii - 1] == "न्" and s[ii + 1] in expand_pratyahaara("छव्"):
        s = aadesh(s, ii - 1, "रुँ")
        s[ii - 1 : ii - 1] = "ं"

    df = post_processing(df, s, "नश्छव्यप्रशान्", "8.3.7")

    df = तस्य_लोपः(df, ii + 1)
    df = खरवसानयोर्विसर्जनीयः(df)

    return df


def खरवसानयोर्विसर्जनीयः(df):

    s = pre_processing(df)

    if " " in s:
        ii = s.index(" ")
        if s[ii - 1] == "र्" and s[ii + 1] in expand_pratyahaara("खर्"):
            aadesh(s, ii - 1, "ः")
    elif s[-1] == "र्":
        aadesh(s, len(s) - 1, "ः")

    df = post_processing(df, s, "खरवसानयोर्विसर्जनीयः", "8.3.15")

    if " " in s:
        ii = s.index(" ")

        if s[ii + 2] in expand_pratyahaara("शर्"):
            df = शर्परे_विसर्जनीयः(df)
        elif s[ii + 1] in expand_pratyahaara("शर्"):
            df = वा_शरि(df)
        elif s[ii + 1] in ["क्", "ख्", "प्", "फ्"]:
            df = कुप्वोः_कपौ_च(df)
        else:
            df = विसर्जनीयस्य_सः(df)

    return df


def भोभगोअघोअपूर्वस्य_योऽशि(df):

    s = pre_processing(df)

    if " " in s:
        ii = s.index(" ")
        if (
            s[ii - 1] == "र्"
            and s[ii + 1] in expand_pratyahaara("अश्")
            and (
                s[ii - 2] in ["अ", "आ"]
                or get_shabda(s[ii - 3 : ii]) == "भोर्"
                or get_shabda(s[ii - 5 : ii]) in ["भगोर्", "अघोर्"]
            )
        ):
            aadesh(s, ii - 1, "य्")

    df = post_processing(df, s, "भोभगोअघोअपूर्वस्य योऽशि", "8.3.17")

    if s[ii + 1] in expand_pratyahaara("हल्"):
        df = हलि_सर्वेषाम्(df)
    elif s[ii - 2] == "ओ":
        df = ओतो_गार्ग्यस्य(df)
    else:
        df = लोपः_शाकल्यस्य(df)

    return df


def लोपः_शाकल्यस्य(df):

    s = pre_processing(df)

    if " " in s:
        ii = s.index(" ")
        if s[ii - 1] in ["य्", "व्"] and s[ii + 1] in expand_pratyahaara("अच्"):
            del s[ii - 1]

    df = post_processing(df, s, "लोपः शाकल्यस्य", "8.3.19")

    return df


def ओतो_गार्ग्यस्य(df):

    s = pre_processing(df)

    if " " in s:
        ii = s.index(" ")
        if s[ii - 1] in ["य्", "व्"] and s[ii + 1] in expand_pratyahaara("अश्"):
            # print(s[ii-1])
            del s[ii - 1]

    df = post_processing(df, s, "ओतो गार्ग्यस्य", "8.3.20")

    return df


def हलि_सर्वेषाम्(df):

    s = pre_processing(df)

    if " " in s:
        ii = s.index(" ")
        if s[ii - 1] in ["य्", "व्"] and s[ii + 1] in expand_pratyahaara("हल्"):
            del s[ii - 1]

    df = post_processing(df, s, "हलि सर्वेषाम्", "8.3.22")

    return df


def मोऽनुस्वारः(df):

    s = pre_processing(df)

    ii = s.index(" ")
    if s[ii - 1] == "म्" and s[ii + 1] in expand_pratyahaara("हल्"):
        s = aadesh(s, ii - 1, "ं")

    df = post_processing(df, s, "मोऽनुस्वारः", "8.3.23")

    return df


def ङमो_ह्रस्वादचि_ङमुण्नित्यम्(df):

    s = pre_processing(df)

    ii = s.index(" ")
    if (
        s[ii - 2] in ["अ", "इ", "उ", "ऋ", "ऌ"]
        and s[ii - 1] in expand_pratyahaara("ङम्")
        and s[ii + 1] in expand_pratyahaara("अच्")
    ):
        s.insert(ii - 1, s[ii - 1])

    df = post_processing(df, s, "ङमो ह्रस्वादचि ङमुण्नित्यम्", "8.3.32")

    return df


def विसर्जनीयस्य_सः(df):

    s = pre_processing(df)

    if " " in s:
        ii = s.index(" ")
        if s[ii - 1] == "ः" and s[ii + 1] in expand_pratyahaara("छव्"):
            aadesh(s, ii - 1, "स्")

    df = post_processing(df, s, "विसर्जनीयस्य सः", "8.3.34")

    if s[ii + 1] in ["च्", "छ्"]:
        df = स्तोः_श्चुना_श्चुः(df)

    return df


def शर्परे_विसर्जनीयः(df):

    s = pre_processing(df)

    df = post_processing(df, s, "शर्परे विसर्जनीयः", "8.3.35")

    return df


def वा_शरि(df):

    s = pre_processing(df)

    df = post_processing(df, s, "वा शरि", "8.3.36")

    return df


def कुप्वोः_कपौ_च(df):

    s = pre_processing(df)

    df = post_processing(df, s, "कुप्वोः ≍क≍पौ च", "8.3.37")

    return df


def स्तोः_श्चुना_श्चुः(df):

    s = pre_processing(df)

    ii = s.index(" ")

    l1 = ["स्", "त्", "थ्", "द्", "ध्", "न्"]
    l2 = ["श्", "च्", "छ्", "ज्", "झ्", "ञ्"]

    dd = dict(zip(l1, l2))

    if s[ii - 1] in l1 and s[ii + 1] in l2:
        aa = dd[s[ii - 1]]
        jj = ii - 1
    if s[ii - 1] in l2 and s[ii + 1] in l1:
        aa = dd[s[ii + 1]]
        jj = ii + 1

    s = aadesh(s, jj, aa)

    df = post_processing(df, s, "स्तोः श्चुना श्चुः", "8.4.40")

    return df


def ष्टुना_ष्टुः(df):

    s = pre_processing(df)

    ii = s.index(" ")

    l1 = ["स्", "त्", "थ्", "द्", "ध्", "न्"]
    l2 = ["ष्", "ट्", "ठ्", "ड्", "ढ्", "ण्"]

    dd = dict(zip(l1, l2))

    if s[ii - 1] in l1 and s[ii + 1] in l2:
        aa = dd[s[ii - 1]]
        jj = ii - 1
    if s[ii - 1] in l2 and s[ii + 1] in l1:
        aa = dd[s[ii + 1]]
        jj = ii + 1

    s = aadesh(s, jj, aa)

    df = post_processing(df, s, "ष्टुना ष्टुः", "8.4.41")

    return df


def यरोऽनुनासिकेऽनुनासिको_वा(df):

    s = pre_processing(df)

    ii = s.index(" ")

    if s[ii - 1] in expand_pratyahaara("यर्") and s[ii + 1] in expand_pratyahaara("ञम्"):
        if s[ii - 1] == "ग्":
            s = aadesh(s, ii - 1, "ङ्")
        if s[ii - 1] == "ज्":
            s = aadesh(s, ii - 1, "ञ्")
        if s[ii - 1] == "ड्":
            s = aadesh(s, ii - 1, "ण्")
        if s[ii - 1] == "द्":
            s = aadesh(s, ii - 1, "न्")
        if s[ii - 1] == "ब्":
            s = aadesh(s, ii - 1, "म्")

    df = post_processing(df, s, "यरोऽनुनासिकेऽनुनासिको वा", "8.4.45")

    return df


def खरि_च(df):

    s = pre_processing(df)

    ii = s.index(" ")

    if s[ii - 1] in expand_pratyahaara("झल्") and s[ii + 1] in expand_pratyahaara("खर्"):

        if s[ii - 1] in ["क्", "ख्", "ग्", "घ्"]:
            aa = "क्"
        if s[ii - 1] in ["च्", "छ्", "ज्", "झ्"]:
            aa = "च्"
        if s[ii - 1] in ["ट्", "ठ्", "ड्", "ढ्"]:
            aa = "ट्"
        if s[ii - 1] in ["त्", "थ्", "द्", "ध्"]:
            aa = "त्"
        if s[ii - 1] in ["प्", "फ्", "ब्", "भ्"]:
            aa = "प्"

    s = aadesh(s, ii - 1, aa)

    df = post_processing(df, s, "खरि च", "8.4.55")

    if (
        s[ii - 1] in expand_pratyahaara("झय्")
        and s[ii + 1] == "श्"
        and s[ii + 2] in expand_pratyahaara("अम्")
    ):
        df = शशछोऽटि(df)

    return df


def वाऽवसाने(df):

    s = pre_processing(df)

    ii = len(s)

    if s[ii - 1] in expand_pratyahaara("झल्"):

        if s[ii - 1] in ["क्", "ख्", "ग्", "घ्"]:
            aa = "क्"
        if s[ii - 1] in ["ट्", "ठ्", "ड्", "ढ्"]:
            aa = "ट्"
        if s[ii - 1] in ["त्", "थ्", "द्", "ध्"]:
            aa = "त्"
        if s[ii - 1] in ["प्", "फ्", "ब्", "भ्"]:
            aa = "प्"

    s = aadesh(s, ii - 1, aa)

    df = post_processing(df, s, "वाऽवसाने", "8.4.56")

    return df


def तोर्लि(df):

    s = pre_processing(df)

    ii = s.index(" ")

    if s[ii + 1] == "ल्":
        if s[ii - 1] == "न्":
            s = aadesh(s, ii - 1, "ल्ँ")
        if s[ii - 1] == "द्":
            s = aadesh(s, ii - 1, "ल्")

    df = post_processing(df, s, "तोर्लि", "8.4.60")

    return df


def झयो_होऽन्यतरस्याम्(df):

    s = pre_processing(df)

    ii = s.index(" ")
    if s[ii - 1] in expand_pratyahaara("झय्") and s[ii + 1] == "ह्":
        if s[ii - 1] == "ग्":
            aa = "घ्"
        if s[ii - 1] == "ज्":
            aa = "झ्"
        if s[ii - 1] == "ड्":
            aa = "ढ्"
        if s[ii - 1] == "द्":
            aa = "ध्"
        if s[ii - 1] == "ब्":
            aa = "भ्"

        s = aadesh(s, ii + 1, aa)
        del s[ii]

    df = post_processing(df, s, "झयो होऽन्यतरस्याम्", "8.4.62")

    return df


def शशछोऽटि(df):

    s = pre_processing(df)

    ii = s.index(" ")

    if (
        s[ii - 1] in expand_pratyahaara("झय्")
        and s[ii + 1] == "श्"
        and s[ii + 2] in expand_pratyahaara("अम्")
    ):
        s = aadesh(s, ii + 1, "छ्")
        del s[ii]

    df = post_processing(df, s, "शशछोऽटि", "8.4.63")

    return df


if __name__ == "__main__":

    df = pd.DataFrame(columns=["स्थिति", "सूत्र"])

    word1 = "समवेतास्"
    word2 = "जपि"
    # word1 = 'भगोस्'
    # word2 = 'अपि'

    v1 = get_vinyaasa(word1)
    v2 = get_vinyaasa(word2)

    word3 = word1 + " " + word2

    row = {"स्थिति": word3, "सूत्र": "-"}
    df = df.append(row, ignore_index=True)

    v3 = get_vinyaasa(word3)

    df = ससजुषो_रुः(df)

    s = pre_processing(df)
    if " " in s:
        ii = s.index(" ")

        if s[ii + 1] in expand_pratyahaara("खर्"):
            df = खरवसानयोर्विसर्जनीयः(df)
        else:
            if s[ii - 2] == "अ":
                if s[ii + 1] == "अ":
                    df = अतो_रोरप्लुतादप्लुते(df)
                elif s[ii + 1] in expand_pratyahaara("हश्"):
                    df = हशि_च(df)
                else:
                    df = भोभगोअघोअपूर्वस्य_योऽशि(df)
            elif s[ii - 2] == "आ":
                df = भोभगोअघोअपूर्वस्य_योऽशि(df)
    else:
        df = खरवसानयोर्विसर्जनीयः(df)

    print(df)
    # print(get_vinyaasa(list(df['स्थिति'])[-1]))
