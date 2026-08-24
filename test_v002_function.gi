function add(a, b)
    return a + b
end

x = add(10, 5)
say x

function square(n)
    return n * n
end

say square(6)

x = 100

function scope_test()
    x = 50
    return x
end

say scope_test()
say x
