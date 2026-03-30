import unittest
from Lab5_Classes import Numbers, ECG

class TestNumbers(unittest.TestCase):

    def setUp(self):
        self.num = Numbers()

    # 4.1
    def test_factorial_positive(self):
        self.assertEqual(self.num.factorial(8), 40320)

    def test_factorial_zero(self):
        self.assertEqual(self.num.factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            self.num.factorial(-4)

    # 42
    def test_add_to_sum(self):
        self.num.addToSum(5)
        self.assertEqual(self.num.sum, 5)
    
    def test_subtract_from_sum(self):
        self.num.addToSum(10)
        self.num.subtractFromSum(5)
        self.assertEqual(self.num.sum, 5)

    # 4.3
    def test_stringOfNumber_valid(self):
        self.assertEqual(self.num.stringOfNumber(9), "nine")

    def test_stringOfNumber_invalid(self):
        with self.assertRaises(TypeError):
            self.num.stringOfNumber(9.9)

        with self.assertRaises(ValueError):
            self.num.stringOfNumber(19)


class TestECG(unittest.TestCase):

    def setUp(self):
        self.ecg_obj = ECG()
        self.ecg = [0.1, 0.2, 1.2, 0.3, 0.1, 1.5, 0.2]

    # 5.1
    def test_detect_peaks_standard(self):
        self.assertEqual(self.ecg_obj.detect_peaks(self.ecg, 1.0), [2, 5])

    def test_detect_peaks_no_peaks(self):
        self.assertEqual(self.ecg_obj.detect_peaks(self.ecg, 10), [])

    #5.2
    def test_remove_baseline_standard(self):
        result = self.ecg_obj.remove_baseline(self.ecg)
        mean = sum(result) / len(result)
        self.assertAlmostEqual(mean, 0.0, places=5)

    def test_remove_baseline_empty_signal(self):
        with self.assertRaises(ValueError):
            self.ecg_obj.remove_baseline([])


    # 5.3
    def test_normalize_standard(self):
        result = self.ecg_obj.normalize(self.ecg)
        self.assertEqual(max(result), 1.0)

    def test_normalize_empty_signal(self):
        with self.assertRaises(ValueError):
            self.ecg_obj.normalize([])

    def test_normalize_constant_zero(self):
        self.assertEqual(self.ecg_obj.normalize([0, 0, 0]), [0, 0, 0])


    # 6.1
    def test_count_peaks_standard(self):
        self.assertEqual(self.ecg_obj.count_peaks(self.ecg, 1.0), 2)

    def test_count_peaks_none(self):
        self.assertEqual(self.ecg_obj.count_peaks(self.ecg, 10), 0)

    # 6.2
    def test_rr_intervals_standard(self):
        self.assertEqual(self.ecg_obj.rr_intervals([0, 3], 1), [3.0])

    def test_rr_intervals_multiple_intervals(self):
        self.assertEqual(self.ecg_obj.rr_intervals([2, 5, 10], 2), [1.5, 2.5])
    
    def test_rr_intervals_invalid(self):
        with self.assertRaises(ValueError):
            self.ecg_obj.rr_intervals([0, 3], 0)

    # 6.3
    def test_is_signal_valid_standard(self):
        self.assertTrue(self.ecg_obj.is_signal_valid(self.ecg))

    def test_is_signal_valid_not_list(self):
        self.assertFalse(self.ecg_obj.is_signal_valid("0, 1, 2"))

    def test_is_signal_valid_empty(self):
        self.assertFalse(self.ecg_obj.is_signal_valid([]))

    def test_is_signal_valid_non_numeric(self):
        self.assertFalse(self.ecg_obj.is_signal_valid(["0", "1", "2"]))

    # 7
    def test_heart_rate_standard(self):
        peaks = [0, 3, 6]
        fs = 1
        expected_hr = 60 / ((3 + 3) / 2) 
        self.assertAlmostEqual(self.ecg_obj.heart_rate(peaks, fs), expected_hr)

    def test_heart_rate_not_enough_peaks(self):
        peaks = [0]
        fs = 1
        with self.assertRaises(ValueError):
            self.ecg_obj.heart_rate(peaks, fs)

    def test_heart_rate_invalid_signal_type(self):
        peaks = "0, 1, 2" 
        fs = 1
        with self.assertRaises(ValueError):
            self.ecg_obj.heart_rate(peaks, fs)

    def test_heart_rate_invalid_signal_non_numeric(self):
        peaks = ["0", "1", "2"]  
        fs = 1
        with self.assertRaises(ValueError):
            self.ecg_obj.heart_rate(peaks, fs)

if __name__ == "__main__":
    unittest.main()