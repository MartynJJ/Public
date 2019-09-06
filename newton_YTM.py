def set_lamb(y):
    return 1/(1+(y/2))

def f_y(price, coupon, time, est_yield = None, face = 100.0):
    if est_yield == None:
        est_yield = coupon
    lamb = set_lamb(est_yield)
    lamb2T = lamb ** (2 * time)
    return 100*(lamb2T+(coupon/2)*lamb*(1-lamb2T)/(1-lamb)) - price

def f_y_prime(coupon, time, est_yield = None, face = 100):
    lamb = set_lamb(est_yield)
    lamb2T = lamb**(2*time)
    lamb2Tm1 = lamb**(2* time- 1)
    return 100*(2 * time * lamb2Tm1 + (-2 * time * lamb2Tm1 + 2 * \
     time * lamb2T - lamb2T + 1)/((1 - lamb) ** 2))

def calc_yield(price, coupon, time, error = 10**-10, give_count = False):
    _error = 1
    count = 0
    guess = coupon
    while _error > error:
        count += 1
        guess -= abs(f_y(price, coupon, T, guess)/f_y_prime(coupon, T, guess))
        _error = abs(f_y(price, coupon, T, guess))
    if give_count:
        return guess, count
    else:
        return guess

price = 103.7704725
coupon = 0.04
tau = 0.7362637362637363
T = (5.5+0.7362637362637363)

pred_yield = calc_yield(price, coupon, T, give_count=True)
print(pred_yield)
