import pandas as pd

from akshara.varnakaarya import get_vinyaasa, get_shabda

from pratyaahaara import expand_pratyahaara
from varna import avasaana

# from vinyaasa import get_shabda, get_vinyaasa
from sutra import *


def vaakya_sandhi(sentence: str):

    prakriya = pd.DataFrame(columns=["स्थिति", "सूत्र"])
    sandhi_summary = pd.DataFrame(columns=["पद समूह", "सूत्राणि", "संधि-कृत रूप"])

    dd = []

    flag = 0
    temp = ""

    # print(mm)

    mm = sentence.split(" ")

    for ii in range(len(mm) - 1):

        primary = mm[ii]

        if flag == 1:
            flag = 0
            primary = temp

        if primary[-1] == "ः":
            primary = get_shabda(get_vinyaasa(primary[:-1] + "स्"))

        if primary in avasaana:
            continue

        secondary = mm[ii + 1]

        if secondary in avasaana:
            s = primary
        else:
            s = primary + " " + secondary
            sv = get_vinyaasa(secondary)

        df = pd.DataFrame(columns=["स्थिति", "सूत्र"])
        row = {"स्थिति": s, "सूत्र": "-"}
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)

        ss = get_vinyaasa(s)
        pv = get_vinyaasa(primary)

        if pv[-1] in expand_pratyahaara("अच्"):
            if secondary in avasaana:
                pass
            elif sv[0] in expand_pratyahaara("हल्"):
                pass
            else:
                if pv[-1] in expand_pratyahaara("एङ्") and sv[0] == "अ":
                    df = एङः_पदान्तादति(df)
                elif (pv[-1] == sv[0] and pv[-1] in expand_pratyahaara("अक्")) or (
                    set((pv[-1], sv[0]))
                    in [
                        set(("अ", "आ")),
                        set(("इ", "ई")),
                        set(("उ", "ऊ")),
                        set(("ऋ", "ॠ")),
                        set(("ऋ", "ऌ")),
                        set(("ॠ", "ऌ")),
                    ]
                ):
                    df = अकः_सवर्णे_दीर्घः(df)
                elif pv[-1] in ["अ", "आ"] and sv[0] in expand_pratyahaara("एच्"):
                    df = वृद्धिरेचि(df)
                elif pv[-1] in ["अ", "आ"] and sv[0] in expand_pratyahaara("अक्"):
                    df = आद्गुणः(df)
                elif pv[-1] in expand_pratyahaara("एच्") and sv[0] in expand_pratyahaara(
                    "अच्"
                ):
                    df = एचोऽयवायावः(df)
                elif pv[-1] in expand_pratyahaara("इक्") and sv[0] in expand_pratyahaara(
                    "अच्"
                ):
                    df = इको_यणचि(df)
        else:
            if (
                (mm[ii] == "सस्" or mm[ii] == "एषस्")
                and sv[0] in expand_pratyahaara("हल्")
                and secondary not in avasaana
            ):
                df = एतत्तदोः_सुलोपोऽकोरनञ्समासे_हलि(df)
            elif pv[-1] == "स्":
                df = ससजुषो_रुः(df)
                if secondary in avasaana:
                    df = खरवसानयोर्विसर्जनीयः(df)
                else:
                    if sv[0] in expand_pratyahaara("खर्"):
                        df = खरवसानयोर्विसर्जनीयः(df)
                    else:
                        if pv[-2] == "अ":
                            if sv[0] == "अ":
                                df = अतो_रोरप्लुतादप्लुते(df)
                            elif sv[0] in expand_pratyahaara("हश्"):
                                df = हशि_च(df)
                            else:
                                df = भोभगोअघोअपूर्वस्य_योऽशि(df)
                        elif pv[-2] == "आ":
                            df = भोभगोअघोअपूर्वस्य_योऽशि(df)

            else:
                if pv[-1] in expand_pratyahaara("झल्"):
                    df = झलां_जशोऽन्ते(df)
                elif pv[-1] == "र्" and (
                    secondary in avasaana or sv[0] in expand_pratyahaara("खर्")
                ):
                    df = खरवसानयोर्विसर्जनीयः(df)
                elif secondary in avasaana:
                    pass
                elif pv[-1] == "म्" and secondary not in avasaana:
                    if sv[0] in expand_pratyahaara("हल्"):
                        df = मोऽनुस्वारः(df)

                elif pv[-1] == "न्" and sv[0] in expand_pratyahaara("छव्"):
                    df = नश्छव्यप्रशान्(df)
                elif pv[-1] == "न्" and sv[0] == "ल्":
                    df = तोर्लि(df)
                elif pv[-1] == "न्" and sv[0] in ["श्", "च्", "छ्", "ज्", "झ्", "ञ्"]:
                    df = स्तोः_श्चुना_श्चुः(df)

                elif pv[-1] in expand_pratyahaara("हल्") and sv[0] in expand_pratyahaara(
                    "अच्"
                ):

                    if pv[-1] in expand_pratyahaara("ङम्") and pv[-2] in [
                        "अ",
                        "इ",
                        "उ",
                        "ऋ",
                        "ऌ",
                    ]:

                        df = ङमो_ह्रस्वादचि_ङमुण्नित्यम्(df)

        r = get_sthiti(df)

        if " " in r:
            # print(r.split(' ')[0], end=' ')
            dd.extend(get_vinyaasa(r.split(" ")[0]))
            dd.append(" ")
        else:
            if secondary in avasaana:
                # print(r, secondary)
                dd.extend(get_vinyaasa(r))
                dd.append(" ")
                dd.append(secondary)
            else:
                flag = 1
                temp = r

        # prakriya = prakriya.append(df, ignore_index=True)
        prakriya = pd.concat([prakriya, df], ignore_index=True)

        sutra_list = list(df["सूत्र"])
        sutra_series = " ".join(sutra_list)

        row = {"पद समूह": s, "सूत्राणि": sutra_series, "संधि-कृत रूप": r}
        # sandhi_summary = sandhi_summary.append(row, ignore_index=True)
        sandhi_summary = pd.concat(
            [sandhi_summary, pd.DataFrame([row])], ignore_index=True
        )

    # Handle the last word if it wasn't processed in the main loop
    if flag == 1:
        # If there's a pending word from the last iteration
        dd.extend(get_vinyaasa(temp))
        dd.append(" ")
    elif len(mm) > 0:
        # Process the last word if it wasn't handled
        last_word = mm[-1]
        if last_word not in avasaana and not any(
            last_word.endswith(av) for av in avasaana if av != " "
        ):
            # If the last word doesn't end with punctuation, add it
            dd.extend(get_vinyaasa(last_word))
            dd.append(" ")
        elif any(last_word.endswith(av) for av in avasaana if av != " "):
            # If the last word ends with punctuation, separate it
            for av in avasaana:
                if av != " " and last_word.endswith(av):
                    word_part = last_word[: -len(av)]
                    if word_part:
                        dd.extend(get_vinyaasa(word_part))
                        dd.append(" ")
                    dd.append(av)
                    break

    ee = [dd[0]]

    for i in range(1, len(dd) - 1):

        if (
            dd[i] == " "
            and dd[i - 1] in expand_pratyahaara("हल्")
            and dd[i + 1] not in avasaana
        ):
            pass
        else:
            ee.append(dd[i])

    ee.append(dd[-1])

    # ii = ee.index("।")
    # ee1 = ee[: ii + 1]
    # ee2 = ee[ii + 1 :]
    # print(get_shabda(ee1))
    # print(get_shabda(ee2))

    ee = get_shabda(ee)
    # print(ee)

    # qaz.write(get_shabda(ee1) + "\n")
    # qaz.write(get_shabda(ee2) + "\n\n")

    # print(prakriya)
    # print(sandhi_summary)

    prakriya.to_csv("prakriya.csv", index=False)
    sandhi_summary.to_csv("sandhi_summary.csv", index=False)

    # qaz.close()

    return [ee, sandhi_summary, prakriya]


if __name__ == "__main__":

    vaakya_sandhi("अत्र आगतः अस्मि शिवः अहम् ।")
