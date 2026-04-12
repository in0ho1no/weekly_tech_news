import json
import time

LOOP_COUNTS = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
REPEAT = 10
OUTPUT_FILE = "benchmark_result.json"


def main():
    results = []

    for max_loop in LOOP_COUNTS:
        total_time = 0.0

        for _ in range(REPEAT):
            # 計測開始
            time_start = time.process_time()

            # 単純な処理を繰り返す
            simple_calc = 0
            for num_of_loop in range(max_loop):
                simple_calc += num_of_loop

            # 計測終了
            time_end = time.process_time()
            total_time += time_end - time_start

        avg_time = total_time / REPEAT
        print(f"ループ回数 {max_loop:>12}: 平均処理時間 {avg_time:.6f} 秒")
        results.append({"loop_count": max_loop, "avg_time_sec": avg_time})

    output = {
        "language": "Python",
        "repeat": REPEAT,
        "results": results,
    }
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(output, file, indent=2, ensure_ascii=False)
    print(f"{OUTPUT_FILE} を出力しました")


if __name__ == "__main__":
    main()
