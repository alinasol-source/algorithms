import Naive as native
import RabinKarp as rabin_karp
import BoyerMoore as boyer_moore
import KMP as knuth_morris_pratt
import Aho as aho_corasick


def test_string_search_algorithm(text, pattern):
    # Naive search
    res = native.naive(text, pattern)
    print("Naive\ni:", res[0], "number of comparisons:", res[1])
    print('Time:', res[2])

    #Rabin_Karp
    res = rabin_karp.Rabin_Karp_Matcher(text, pattern)
    print("rabin_karp\ni:", res[0], "number of comparisons:", res[1])
    print('Time:', res[2])

    # Boyer_Moore
    res = boyer_moore.boyer(text, pattern)
    print("boyer_moore\ni:", res[0], "number of comparisons:", res[1])
    print('Time:', res[2])

    # Knuth_Morris_Pratt
    res = knuth_morris_pratt.KMP(text, pattern)
    print("knuth_morris_pratt\ni:", res[0], "number of comparisons:", res[1])
    print('Time:', res[2])

    # Aho_Corasick
    res = aho_corasick.Aho_Korasik(text, pattern)
    print("aho_corasick\ni:", res[0], "number of comparisons:", res[1])
    print('Time:', res[2])


if __name__ == '__main__':

    print('\nTESTS:')
    print("File: bad_t_1")
    f_text = open("benchmarks/bad_t_1.txt", "r")
    f_pattern = open("benchmarks/bad_w_1.txt", "r")
    test_string_search_algorithm(f_text.read(), f_pattern.read())
    print("\nFile: bad_t_2")
    f_text = open("benchmarks/bad_t_2.txt", "r")
    f_pattern = open("benchmarks/bad_w_2.txt", "r")
    test_string_search_algorithm(f_text.read(), f_pattern.read())
    print("\nFile: bad_t_3")
    f_text = open("benchmarks/bad_t_3.txt", "r")
    f_pattern = open("benchmarks/bad_w_3.txt", "r")
    test_string_search_algorithm(f_text.read(), f_pattern.read())
    print("\nFile: bad_t_4")
    f_text = open("benchmarks/bad_t_4.txt", "r")
    f_pattern = open("benchmarks/bad_w_4.txt", "r")
    test_string_search_algorithm(f_text.read(), f_pattern.read())

    print("\nFile: good_t_1")
    f_text = open("benchmarks/good_t_1.txt", "r", encoding="utf-8")
    f_pattern = open("benchmarks/good_w_1.txt", "r", encoding="utf-8")
    test_string_search_algorithm(f_text.read(), f_pattern.read())
    print("\nFile: good_t_2")
    f_text = open("benchmarks/good_t_2.txt", "r", encoding="utf-8")
    f_pattern = open("benchmarks/good_w_2.txt", "r", encoding="utf-8")
    test_string_search_algorithm(f_text.read(), f_pattern.read())
    print("\nFile: good_t_3")
    f_text = open("benchmarks/good_t_3.txt", "r", encoding="utf-8")
    f_pattern = open("benchmarks/good_w_3.txt", "r", encoding="utf-8")
    test_string_search_algorithm(f_text.read(), f_pattern.read())
    print("\nFile: good_t_4")
    f_text = open("benchmarks/good_t_4.txt", "r", encoding="utf-8")
    f_pattern = open("benchmarks/good_w_4.txt", "r", encoding="utf-8")
    test_string_search_algorithm(f_text.read(), f_pattern.read())