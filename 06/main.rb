
array = []
file = File.open("add/Add.asm", 'r')
file.each_line { |line| array << line}
file.close
puts array

binaryFile = File.new("out.hack", "w")
binaryFile.puts(array)
binaryFile.close
