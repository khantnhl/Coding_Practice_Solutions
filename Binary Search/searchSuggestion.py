def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

    # do binary search for each prefix
    products.sort() # lexicographically sorted
    cur = ''
    result = []
    for ch in searchWord:
        cur += ch
        idx = bisect.bisect_left(products, cur)
        result.append([word for word in products[idx:idx+3] if word.startswith(cur)])
    return result

# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]