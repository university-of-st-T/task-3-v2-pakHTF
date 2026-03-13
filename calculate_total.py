def calculate_total(prices, *discounts, **options):
    res=0
    for i in prices:
        res+=i
    for j in discounts:
        res*=(1-j/100)
    if options:
        if "tax" in options:
            res*=(1+options["tax"]/100)
        if "round_to" in options:
            res=round(res,options["round_to"])
    return res
