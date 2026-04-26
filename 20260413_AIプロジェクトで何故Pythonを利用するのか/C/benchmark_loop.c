#include <stdio.h>
#include <time.h>

#define REPEAT 10
#define OUTPUT_FILE "benchmark_result.json"

static const long long LOOP_COUNTS[] = {
    10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000
};
#define NUM_PATTERNS (sizeof(LOOP_COUNTS) / sizeof(LOOP_COUNTS[0]))

int main(void) {
    size_t pattern_idx;
    int repeat_idx;
    double avg_times[NUM_PATTERNS];
    FILE *json_file;

    for (pattern_idx = 0; pattern_idx < NUM_PATTERNS; pattern_idx++) {
        double total_time = 0.0;

        for (repeat_idx = 0; repeat_idx < REPEAT; repeat_idx++) {
            clock_t time_start;
            clock_t time_end;
            long long simple_calc = 0;
            long long num_of_loop;

            /* 計測開始 */
            time_start = clock();

            /* 単純な処理を繰り返す */
            for (num_of_loop = 0; num_of_loop < LOOP_COUNTS[pattern_idx]; num_of_loop++) {
                simple_calc += num_of_loop;
            }

            /* 計測終了 */
            time_end = clock();
            total_time += (double)(time_end - time_start) / CLOCKS_PER_SEC;
        }

        avg_times[pattern_idx] = total_time / REPEAT;
        printf("ループ回数 %12lld: 平均処理時間 %.6f 秒\n",
               LOOP_COUNTS[pattern_idx], avg_times[pattern_idx]);
    }

    /* JSON出力 */
    json_file = fopen(OUTPUT_FILE, "w");
    if (json_file == NULL) {
        fprintf(stderr, "ファイルを開けませんでした: %s\n", OUTPUT_FILE);
        return 1;
    }

    fprintf(json_file, "{\n");
    fprintf(json_file, "  \"language\": \"C\",\n");
    fprintf(json_file, "  \"repeat\": %d,\n", REPEAT);
    fprintf(json_file, "  \"results\": [\n");

    for (pattern_idx = 0; pattern_idx < NUM_PATTERNS; pattern_idx++) {
        const char *comma = (pattern_idx < NUM_PATTERNS - 1) ? "," : "";
        fprintf(json_file, "    {\"loop_count\": %lld, \"avg_time_sec\": %.6f}%s\n",
                LOOP_COUNTS[pattern_idx], avg_times[pattern_idx], comma);
    }

    fprintf(json_file, "  ]\n");
    fprintf(json_file, "}\n");
    fclose(json_file);

    printf("%s を出力しました\n", OUTPUT_FILE);

    return 0;
}
