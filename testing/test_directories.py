import unittest
from app.directories import load_wordlist, fuzz_directories

class TestDirectoryFuzzing(unittest.TestCase):
    
    def test_load_wordlist(self):
        wordlist = load_wordlist('config/wordlists/dir_wordlist.txt')
        self.assertTrue(len(wordlist) > 0)  # Ensure the wordlist is loaded

    def test_fuzz_directories(self):
        # Test with a local server or a mock HTTP server
        url = "http://localhost:8000"
        wordlist = ["admin", "login"]
        found_dirs = fuzz_directories(url, wordlist)
        self.assertIsInstance(found_dirs, list)

if __name__ == "__main__":
    unittest.main()
