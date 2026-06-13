#!/usr/bin/env python3

import sys

from common import print_tour, read_input


#cities　＝　座標のタプルのリスト
#戻り値は訪問順のindex

#今いる都市を保存する関数　now_city
#next_cityに次に行きたい都市を入れる
#now_cityから一番座標が近い都市をnext_cityに入れる

#座標の近さは絶対値で計測

#最初の座標をstartとして保存（最後に戻ってくるために）
#既に訪れたところは別管理

#最初に座標順に並べてみるとか？？

#一番近い座標を見つけたらnow_listを変更→次の座標を計算
#繰り返す

def solve(cities):
    # Build a trivial solution.
    # Visit the cities in the order they appear in the input.

    #差を入れとく表
    diff_list = []

    #最初の町だけ、now_cityにいれとく
    start_city = cities[0]
    now_city = start_city
    now_city_index = 0


    visited_list = []
    answer_list = []
    answer_list.append(0)

    cities_count = len(cities)


    visited_list.append(now_city_index)

    flag = True
    while flag == True:
        #一番近くの都市を見つけるために、座標毎の差を計算する
        for index in range(len(cities)):

            #今いる都市の差は計算しない
            if index in visited_list:
                continue


            #距離の差を計算
            diff_x = abs(cities[index][0] - now_city[0])
            diff_y = abs(cities[index][1] - now_city[1])
            diff_xy = diff_x + diff_y
            # print(f"diff_x:{diff_x}")
            # print(diff_y)
            # print(diff_xy)

            #(差、index)のタプルのリストを作る
            diff_list.append((diff_xy, index))


        #visited_listのやつだけNoneのままにしたい
        #一番差の小さい都市を次に行く都市に決定
        next_city = min(diff_list)
        # print(f"next_city : {next_city}")

        #全ての差をリセット
        diff_list.clear()


        #戻り値のリストに追加
        answer_list.append(next_city[1])
        # print(answer_list)


        #今の都市を次に進める
        now_city = cities[next_city[1]]
        now_city_index = next_city[1]
        # print(f"now_city_index: {now_city_index}")

        #進めた先の都市を、visitedに追加
        visited_list.append(now_city_index)


        #全ての都市に訪れたら、while文を抜ける
        if len(visited_list) == cities_count:
            flag = False


        # diff_list.sort()
        # for index in diff_list:
        #     return_list.append(diff_list[index][1])

    return answer_list


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
