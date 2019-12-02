import linecache

FILE = 'input.txt'

input_list = {}

lastrow = sum(1 for j in open(FILE))  # ファイル内の最終行の番号を取得
m = int(linecache.getline(FILE, lastrow))  # ファイル内の最終行のデータを取得

# データ整形
for j in range(1, lastrow):
    i, s = linecache.getline(FILE, j).rstrip('\n').split(':')  # 一行取得し改行コードを削除、整数と文字列を分割
    i = int(i)

    # mがiの倍数の場合は辞書に登録
    if not m % i:
        input_list[i] = s

# ソートし文字列を並べて出力
if input_list:
    for j in sorted(input_list.keys()):  # 辞書のキーでソート
        print(input_list[j], end="")
# 登録された文字列が無い場合はmを出力
else:
    print(m)
