eto_tuple = (
    "子",
    "丑",
    "寅",
    "卯",
    "辰",
    "巳",
    "午",
    "未",
    "申",
    "酉",
    "戌",
    "亥"
)

year_str = input("あなたの生まれ年を西暦４桁で入力してください")
year = int(year_str)
number_of_eto =(year + 8) % 12
eto_name = eto_tuple[number_of_eto]
print("あなたの干支は", eto_name, "です")
