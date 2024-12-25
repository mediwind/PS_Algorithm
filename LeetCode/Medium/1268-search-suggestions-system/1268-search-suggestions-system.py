class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        arr = list()
        products.sort()
        for i, c in enumerate(searchWord):
            products = [p for p in products if len(p) > i and p[i] == c]
            arr.append(products[:3])
        return arr