###
#
#  Sort integer arguments (ascending) 
#
###

# Initialize an empty array to store sorted integers
result = []

# Iterate through each argument passed in from the command line
ARGV.each do |arg|
    # Skip if the argument is not an integer
    next unless arg =~ /^-?[0-9]+$/

    # Convert the argument to an integer
    i_arg = arg.to_i

    # Find the right position to insert the integer
    is_inserted = false
    i = 0
    l = result.size
    while !is_inserted && i < l do
        if result[i] < i_arg
            i += 1
        else
            result.insert(i, i_arg)
            is_inserted = true
            break
        end
    end
    
    # If the integer wasn't inserted in the loop, add it to the end
    result << i_arg unless is_inserted
end

# Print the sorted integers in ascending order
puts result
