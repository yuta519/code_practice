const isAnagram = (s, t) => {
  const cache = {};

  // loop s anagram
  for (const char of s) {
    cache[char] ? cache[char]++ : (cache[char] = 1);
  }
  console.log(cache);

  // loop t "nagaram"
  for (const char of t) {
    // n
    // { a: 3, n: 1, g: 1, r: 1, m: 1 }
    if (!cache[char]) return false;
    cache[char]--;
  }

  for (const char of Object.keys(cache)) {
    if (cache[char] !== 0) return false;
  }

  return true;
};

console.log(isAnagram("anagram", "nagaram"));
