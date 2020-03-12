toy = "elmo"
quote = "elmo is the hottest of the season! elmo will be on every kid's wishlist!"

if toy in quote:
    print("inside")

count1 = quote.count(toy)
print("count:", count1)

quote2 = "elm"
count2 = quote2.count(toy)
print("count2:", count2)

res = [(3, "asd"), (4, "asd"), (5, "sasdf"), (6, "sdagdf"), (7, "gfh")]
print("res:", res)
print("res[0][1]:", res[0][1])
