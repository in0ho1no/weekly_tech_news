#include <stdio.h>
#include <time.h>

#define MAX_LOOP 100000000

int main(void) {
    clock_t time_start;
    clock_t time_end;
    double time_taken;
    long long simple_calc = 0;
    long long num_of_loop = 0;

    /* 計測開始 */
    time_start = clock();

    /* 単純な処理を繰り返す */
    for (num_of_loop = 0; MAX_LOOP > num_of_loop; num_of_loop++) {
        simple_calc += num_of_loop;
    }

    /* 計測終了 */
    time_end = clock();

    /* 結果出力 */
    printf("結果: %lld\n", simple_calc);
    time_taken = (double)(time_end - time_start) / CLOCKS_PER_SEC;
    printf("処理時間: %f 秒\n", time_taken);

    return 0;
}
