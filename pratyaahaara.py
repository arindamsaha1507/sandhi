from varna import maaheshwar_suutra, vyanjana, vyanjana_with_akaara


def expand_pratyahaara(p):

    assert len(p) == 3
    assert p[2] == "्"

    start = p[0]
    stop = p[1] + p[2]

    i = maaheshwar_suutra.index(start)
    j = maaheshwar_suutra.index(stop)

    r = maaheshwar_suutra[i:j]

    it = [x for x in r if x in vyanjana]
    for ii in it:
        r.remove(ii)

    rr = [x + "्" if x in vyanjana_with_akaara else x for x in r]

    if "अ" in rr:
        rr.append("आ")
    if "इ" in rr:
        rr.append("ई")
    if "उ" in rr:
        rr.append("ऊ")

    return rr


if __name__ == "__main__":
    x = expand_pratyahaara("उश्")
    print(x)
