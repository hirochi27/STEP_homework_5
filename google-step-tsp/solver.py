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
    now_city = cities[0]
    now_city_index = 0


    visited_list = []
    answer_list = []
    answer_list.append(0)

    cities_count = len(cities)


    visited_list.append(now_city_index)


    #貪欲法
    #ここはN^2
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

            #(差、index)のタプルをリストに追加
            diff_list.append((diff_xy, index))


        #visited_listのやつだけNoneのままにしたい
        #一番差の小さい都市を次に行く都市に決定
        next_city = min(diff_list)

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


    #2-opt

    #二つ都市の間を逆順にする
    #ここの計算量N＾3?
    flag = True
    while flag == True:
        flag = False
        for index in range(len(answer_list)-1): #answer_list＝citiesにおけるindex
            goal_index = index + 2
            while goal_index < len(answer_list):
                #goal/start_index = citiesにおけるindex
                start_city_index = answer_list[index]
                goal_city_index = answer_list[goal_index] #最後の一周で、最初に戻したい

                start_next = answer_list[index + 1]
                goal_next = answer_list[(goal_index + 1) % len(answer_list)]

                #距離の差を計算
                start_diff_x = abs(cities[start_city_index][0] - cities[start_next][0])
                start_diff_y = abs(cities[start_city_index][1] - cities[start_next][1])

                goal_diff_x = abs(cities[goal_city_index][0] - cities[goal_next][0])
                goal_diff_y = abs(cities[goal_city_index][1] - cities[goal_next][1])

                diff_xy = start_diff_x + start_diff_y + goal_diff_x + goal_diff_y

                #2optした後の距離の差を計算
                opt_s_diff_x = abs(cities[start_city_index][0] - cities[goal_city_index ][0])
                opt_s_diff_y = abs(cities[start_city_index][1] - cities[goal_city_index ][1])

                opt_g_diff_x = abs(cities[start_next][0] - cities[goal_next][0])
                opt_g_diff_y = abs(cities[start_next][1] - cities[goal_next][1])

                opt_diff_xy = opt_s_diff_x + opt_s_diff_y + opt_g_diff_x + opt_g_diff_y

                if opt_diff_xy < diff_xy:
                    answer_list[index+ 1 : goal_index + 1] = answer_list[index + 1 : goal_index + 1][::-1]
                    flag = True #入れ替えがあった場合は繰り返す
                
                goal_index += 1
            

    return answer_list


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
