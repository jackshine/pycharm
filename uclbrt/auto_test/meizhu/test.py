def get_list_min_num(build_num_list):
    temp = build_num_list[0]
    for i in build_num_list:
        if temp > i:
            temp = i
    return temp


def generate_num(min_num, build_num_list):
    # 查找楼栋编号的最小值
    num = min_num + 1
    if num not in build_num_list:
        return num
    elif num == 255:
        raise '超出范围'
    else:
        return generate_num(num, build_num_list)


if __name__ == "__main__":
    list = [255,254,253]
    temp = get_list_min_num(list)
    num = generate_num(temp,list)
    print(num)
