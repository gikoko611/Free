function greet(name)
    say name
end

greet("GI")

function empty()
    say "EMPTY"
end

empty()

function nested(a)
    function inner(b)
        return b * 2
    end

    return inner(a)
end

say nested(5)
