yeartax_ = int(input())

basketshoes = yeartax_ - (yeartax_ * 0.40 )
basketclothes = basketshoes - (basketshoes * 0.20)
basketball = basketclothes / 4
accesories = basketball / 5

priceforall = yeartax_ + basketshoes + basketclothes + basketball + accesories  # cost for all
print(priceforall)  # printing