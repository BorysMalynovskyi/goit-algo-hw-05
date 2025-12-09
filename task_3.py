from pathlib import Path
from timeit import timeit

from boyer_moore import BoyerMooreSubstringSearch
from kmp import KMPSubstringSearch
from rabin_karp import RabinKarpSubstringSearch


ARTICLES = {
    "article_1.txt": {
        "existing": "Page",
        "missing": "missing_in_article_one",
    },
    "article_2.txt": {
        "existing": "NoSQL",
        "missing": "missing_in_article_two",
    },
}

ALGORITHMS = {
    "Boyer-Moore": BoyerMooreSubstringSearch,
    "KMP": KMPSubstringSearch,
    "Rabin-Karp": RabinKarpSubstringSearch,
}


def load_articles():
    base_path = Path(__file__).parent
    texts = {}
    for filename in ARTICLES:
        texts[filename] = (base_path / filename).read_text(
            encoding="utf-8", errors="ignore"
        )
    return texts


def benchmark_search(text, pattern, algorithm_cls, repeats=100):
    searcher = algorithm_cls(pattern)
    return timeit(lambda: searcher.search(text), number=repeats) / repeats


def run_benchmarks():
    texts = load_articles()
    results = {}

    for filename, substrings in ARTICLES.items():
        text = texts[filename]
        results[filename] = {}
        for label, substring in substrings.items():
            results[filename][label] = {}
            for alg_name, alg_cls in ALGORITHMS.items():
                avg_time = benchmark_search(text, substring, alg_cls)
                results[filename][label][alg_name] = avg_time
    return results


def summarize(results):
    print("Average time per run (seconds):")
    for filename, labels in results.items():
        print(f"\n{filename}:")
        for label, timings in labels.items():
            print(f"  {label}:")
            for alg, value in sorted(timings.items(), key=lambda x: x[1]):
                print(f"    {alg}: {value:.6f}")

    fastest_per_text = {}
    for filename, labels in results.items():
        combined = {}
        for timings in labels.values():
            for alg, value in timings.items():
                combined[alg] = combined.get(alg, 0) + value
        fastest_per_text[filename] = min(combined.items(), key=lambda x: x[1])[0]

    overall_totals = {}
    for labels in results.values():
        for timings in labels.values():
            for alg, value in timings.items():
                overall_totals[alg] = overall_totals.get(alg, 0) + value
    overall_fastest = min(overall_totals.items(), key=lambda x: x[1])[0]

    print("\nFastest per text:")
    for filename, alg in fastest_per_text.items():
        print(f"  {filename}: {alg}")

    print(f"\nOverall fastest: {overall_fastest}")


if __name__ == "__main__":
    benchmark_results = run_benchmarks()
    summarize(benchmark_results)
