import auto_test_tools as att


'''

Write a function that takes as input a list which is used as
a mask of N elements with values 0 or 1. The function should
then compute the integer output defined by

     x = \sum_{i=1}^N  2^{i-1} mask(i)

Use a loop for computing the output value.

Test your procedure on each of the input examples below

  mask := <0 0 0 0>;
  mask := <0 0 0 1>;
  mask := <0 0 1 0>;
  mask := <0 0 1 1>;
  mask := <0 1 0 0>;
  mask := <0 1 0 1>;
  mask := <0 1 1 0>;
  mask := <0 1 1 1>;
  mask := <1 0 0 0>;

The notation <...> is a bit-pattern with least significant
bit at the right-most position and most significant bit
at the left-most position.

ADVICE: Submit your solution even if your code is
not running or your score is less than 100%

'''

def opret_nummer(mask: list) -> int:
    Resultat = 0  
    N = len(mask)  
    for i in range(N):
        Resultat += 2 ** i * mask[i]
    return Resultat



att.start()
att.begin_task('Opgave 1')

mask_0 = [0, 0, 0, 0]
mask_1 = [1, 0, 0, 0]
mask_2 = [0, 1, 0, 0]
mask_3 = [1, 1, 0, 0]
mask_4 = [0, 0, 1, 0]
mask_5 = [1, 0, 1, 0]
mask_6 = [0, 1, 1, 0]
mask_7 = [1, 1, 1, 0]
mask_8 = [0, 0, 0, 1]
mask_9 = [1, 0, 0, 1]
mask_10 = [0, 1, 0, 1]
mask_11 = [1, 1, 0, 1]
mask_12 = [0, 0, 1, 1]
mask_13 = [1, 0, 1, 1]
mask_14 = [0, 1, 1, 1]
mask_15 = [1, 1, 1, 1]

tst_0 = opret_nummer(mask_0)
tst_1 = opret_nummer(mask_1)
tst_2 = opret_nummer(mask_2)
tst_3 = opret_nummer(mask_3)
tst_4 = opret_nummer(mask_4)
tst_5 = opret_nummer(mask_5)
tst_6 = opret_nummer(mask_6)
tst_7 = opret_nummer(mask_7)
tst_8 = opret_nummer(mask_8)
tst_9 = opret_nummer(mask_9)
tst_10 = opret_nummer(mask_10)
tst_11 = opret_nummer(mask_11)
tst_12 = opret_nummer(mask_12)
tst_13 = opret_nummer(mask_13)
tst_14 = opret_nummer(mask_14)
tst_15 = opret_nummer(mask_15)

att.is_equal(tst_0, 0, att.get_linenumber(), ' mask 0 failed')
att.is_equal(tst_1, 1, att.get_linenumber(), ' mask 1 failed')
att.is_equal(tst_2, 2, att.get_linenumber(), ' mask 2 failed')
att.is_equal(tst_3, 3, att.get_linenumber(), ' mask 3 failed')
att.is_equal(tst_4, 4, att.get_linenumber(), ' mask 4 failed')
att.is_equal(tst_5, 5, att.get_linenumber(), ' mask 5 failed')
att.is_equal(tst_6, 6, att.get_linenumber(), ' mask 6 failed')
att.is_equal(tst_7, 7, att.get_linenumber(), ' mask 7 failed')
att.is_equal(tst_8, 8, att.get_linenumber(), ' mask 8 failed')
att.is_equal(tst_9, 9, att.get_linenumber(), ' mask 9 failed')
att.is_equal(tst_10, 10, att.get_linenumber(), ' mask 10 failed')
att.is_equal(tst_11, 11, att.get_linenumber(), ' mask 11 failed')
att.is_equal(tst_12, 12, att.get_linenumber(), ' mask 12 failed')
att.is_equal(tst_13, 13, att.get_linenumber(), ' mask 13 failed')
att.is_equal(tst_14, 14, att.get_linenumber(), ' mask 14 failed')
att.is_equal(tst_15, 15, att.get_linenumber(), ' mask 15 failed')

att.end_task()

att.stop()

