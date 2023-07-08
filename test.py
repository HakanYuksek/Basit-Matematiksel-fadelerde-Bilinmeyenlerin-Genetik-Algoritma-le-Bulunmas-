import genetic_algorithm

test_samples = {"a + b + 2*c = 10":0,
                "a + b - 2*c = 10":0,
                "a + 2*b - c * d = 20":0,
                "a * ( b + c ) = 50":0,
                "a + b / c = 10":0,
                "a + 2*b - 3*c - 4*d = 20 ":0,
                "a*b*c + d + 2 = 75":0,
                "a * ( b + c ) - d / e = 20":0,
                "a * b + c - 2*d + 7 = 20":0,
                "2*a + 5*b + 7*c + d / c + ( 7 + e) = 20":0}

i = 1
for key in test_samples:
    num_of_success = 0
    print("-----------------------------------"+str(i)+"---------------------------------------")
    for each in range(10):
        result,variables,generation_num = genetic_algorithm.run(key,25,20,"roulette_wheel","order_based",500)

        if generation_num < 300:
            num_of_success += 1
    i += 1

    test_samples[key] = num_of_success

print("Success for all tests")
print("----------------------------")
for key in test_samples:
    str1 = key + " başarı--->"+str(test_samples[key])
    print(str1)
        
