import time

MAX_LOOP = 100000000


def main():
    # 計測開始
    time_start = time.process_time()

    # 単純な処理を繰り返す
    simple_calc = 0
    for num_of_loop in range(MAX_LOOP):
        simple_calc += num_of_loop

    # 計測終了
    time_end = time.process_time()

    # 結果出力
    print("結果:", simple_calc)
    print("処理時間:", time_end - time_start, "秒")


if __name__ == "__main__":
    main()
