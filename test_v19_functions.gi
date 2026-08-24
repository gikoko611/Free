function square(x)
    return x * x
end

function add(a, b)
    return a + b
end

say square(6)
say add(10, 20)

nums = [1, 2, 3, 4]

for x in nums
    if x == 3
        break
    end
    say x
end
