#100 sayının toplamının karesi ile karelerinin toplamı arasındaki fark
print("100 sayının toplamının karesi ile karelerinin toplamı arasındaki fark:",((100 *101 // 2) ** 2) - (sum(map(lambda n: n ** 2, range(1,101)))))
