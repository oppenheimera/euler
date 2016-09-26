start = Time.now

def check(m)
    ary = []
    for n in 2..m
        if n.to_s.split(//).map {|n| n.to_i**5} .reduce(:+) == n
            puts n
            ary.push(n)
        end
    end
    return ary.reduce(:+)
end

ans = check(2 * 10**5).to_s
elapsed = (Time.now - start).to_s

puts "Found answer #{ans} in #{elapsed} seconds"