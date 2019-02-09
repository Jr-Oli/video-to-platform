#----------------
#This file takes the CAHV files obtained from voodoo and puts the Cx, Cy, Cz coordinates
#into a new file. It assumes you have tracked every frame [step == 1].
#If this is not the case change the increment in the while loop on line 34.
#Created 5 Feb. 2019 J. Oli.
#---------------

#create a file named frameCoords.txt and write the following text, if it already exists overwrite it
outFile1 = File.new("frameCoords.txt", "w")
    outFile1.puts "This file contains the Cx, Cy, and Cz positions of the cameras found in the CAHV files 353-517"
	outFile1.puts "**Note** multiple sets of CAHV files were tracked in voodoo, but at different times."
	outFile1.puts "This means the xyz coordinates do not seemlessly relate to each other between all sets."
    outFile1.puts "Look out for large inconsistent jumps in coordinates."
	outFile1.puts ""
outFile1.close


#set frame num equal to the first frame in the image sequence
framenum = 353
#this assumes all cahv file names are of the format "frame###.cam 
cahvfilename = "frame" + framenum.to_s + ".cam"

#append to the file we created above
outFile2 = File.new("frameCoords.txt", "a")
    
    while File.exist?(cahvfilename) do
	    #read each line of the cahv file into an array 
        cahvtextArray = File.readlines(cahvfilename)
		#indicate in the file frameCoords what cahv file we are pulling coordinates from
		outFile2.puts cahvfilename + " : "
		#append lines 7 and 8 -which are 6 and 7 in the array- to the file frameCoords.txt These lines contain the x y z coordinates
		outFile2.puts cahvtextArray[6]
		outFile2.puts cahvtextArray[7]
		outFile2.puts ""
		framenum += 1
        cahvfilename = "frame" + framenum.to_s + ".cam"
    end
outFile2.close

puts "file has finished running"