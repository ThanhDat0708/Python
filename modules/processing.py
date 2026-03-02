def tim_sv_diem_max(lst_sv):
    list_sv_max = lst_sv[0]
    for sv in lst_sv:
        if sv["diem"] > list_sv_max["diem"]:
            list_sv_max = sv
    return list_sv_max
def tim_sv_diem_min(lst_sv):
    list_sv_min = lst_sv[0]
    for sv in lst_sv:
        if sv["diem"] < list_sv_min["diem"]:
            list_sv_min = sv
    return list_sv_min