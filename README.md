# goit-algo-hw-05

## Substring Search Benchmark

Benchmarked Boyer-Moore, KMP, and Rabin-Karp on `article_1.txt` and `article_2.txt` using `timeit` for both a present substring and a missing substring.

### Methodology
- Environment: Python `timeit`, 100 repetitions per measurement, average wall-clock seconds per run.
- Data: `article_1.txt`, `article_2.txt` (UTF-8 read, errors ignored).
- Substrings: one known-present and one absent per text (`Page` / `missing_in_article_one`; `NoSQL` / `missing_in_article_two`).
- Algorithms: Boyer-Moore (bad character heuristic), Knuth-Morris-Pratt, Rabin-Karp (rolling hash).
- Metric: Lower average time is better. Also report fastest algorithm per text and overall.

### article_1.txt
- Existing (`Page`): Boyer-Moore 0.000001; KMP 0.000001; Rabin-Karp 0.000003.
- Missing (`missing_in_article_one`): Boyer-Moore 0.000131; KMP 0.000895; Rabin-Karp 0.002109.
- Fastest overall for this text: Boyer-Moore.

### article_2.txt
- Existing (`NoSQL`): Boyer-Moore 0.000139; KMP 0.000234; Rabin-Karp 0.000584.
- Missing (`missing_in_article_two`): Boyer-Moore 0.000189; KMP 0.001218; Rabin-Karp 0.002964.
- Fastest overall for this text: Boyer-Moore.

### Overall conclusion
- Boyer-Moore was fastest on both texts and across both substring types overall.
- KMP tracked closely on very short hits but lagged on misses; Rabin-Karp trailed in all cases with this hash/modulus setup.
- For large texts with rare matches, Boyer-Moore’s skipping provides the best throughput in this experiment. KMP remains a solid, hash-free alternative; Rabin-Karp may improve with tuned modulus/base or multi-pattern use cases.
