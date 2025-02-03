import time
import statistics
from typing import Any, Callable
import numpy as np
from py3langid.langid import LanguageIdentifier, MODEL_FILE
import gc


def into_us(ns: float) -> float:
    return round(ns / 1000, 3)


# NOTE: code from claude
class Benchmark:
    def __init__(self, func: Callable[[], Any], iters=10000):
        self.func = func
        self.iters = iters

    def run(self) -> dict[str, float]:
        times = []
        gc.disable()
        for _ in range(self.iters):
            start = time.perf_counter_ns()
            self.func()
            end = time.perf_counter_ns()
            times.append(end - start)
        gc.enable()

        return {
            "mean (µs)": into_us(statistics.mean(times)),
            "median (µs)": into_us(statistics.median(times)),
            "std_dev (µs)": into_us(statistics.stdev(times)),
            "slope (µs)": into_us(self._calculate_complexity_slope(times)),
        }

    def _calculate_complexity_slope(self, times) -> float:
        # Simple linear regression to estimate computational complexity
        cumulative_times = np.cumsum(times)
        input_sizes = np.arange(1, len(times) + 1)
        slope, _ = np.polyfit(input_sizes, cumulative_times, 1)
        return slope.item()


if __name__ == "__main__":
    li = LanguageIdentifier.from_pickled_model(MODEL_FILE)
    for lang, filename in (
        ("en", "en.txt"),
        ("zh", "zh.txt"),
        ("jp", "jp.txt"),
    ):
        with open(filename, "r") as f:
            text = f.read()
        bench = Benchmark(lambda: li.classify(text))
        results = bench.run()
        print(
            f"|`py3langid`|{lang}|{results['mean (µs)']:.3f} µs|{results['median (µs)']:.3f} µs|{results['mean (µs)']:.3f} µs|{results['std_dev (µs)']:.3f} µs|"
        )
