class Integer
    def fact
        (1..self).reduce(:*) || 1
    end
end

def work(n)
    for x in 3..n
        if x.to_s.split(//).map{|x| x.to_i.fact}.reduce(:+) == x
            puts x
        end
    end    
end