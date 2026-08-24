function square(x)
    return x*x
end

say square(6)

function outer(x)
    return square(x)+1
end

say outer(4)

function count(n)
    if n == 0
        return 0
    else
        return count(n-1)+1
    end
end

say count(5)

d = [1,2,3]
say d[2]
