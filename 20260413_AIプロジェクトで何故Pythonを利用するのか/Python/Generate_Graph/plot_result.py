import json
import os

import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['Yu Gothic', 'Meiryo', 'MS Gothic']
plt.rcParams['axes.unicode_minus'] = False

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(SCRIPT_DIR, 'input')
OUTPUT_DIR = os.path.join(SCRIPT_DIR, 'output')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'benchmark_result.png')
MARKER = 'o'


def load_results():
    datasets = []
    for filename in sorted(os.listdir(INPUT_DIR)):
        if not filename.endswith('.json'):
            continue
        file_path = os.path.join(INPUT_DIR, filename)
        with open(file_path, encoding='utf-8') as file:
            datasets.append(json.load(file))
    return datasets


def main():
    datasets = load_results()
    if not datasets:
        print(f'JSONファイルが見つかりません: {INPUT_DIR}')
        return

    fig, ax = plt.subplots(figsize=(8, 5))

    for data in datasets:
        loop_counts = [entry['loop_count'] for entry in data['results']]
        avg_times = [entry['avg_time_sec'] for entry in data['results']]
        ax.plot(loop_counts, avg_times, marker=MARKER, label=data['language'])

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('ループ回数')
    ax.set_ylabel('平均処理時間 (秒)')
    ax.set_title('処理時間比較 (C vs Python)')
    ax.legend()
    ax.grid(True, which='both', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=150)
    print(f'{OUTPUT_FILE} を出力しました')


if __name__ == '__main__':
    main()
