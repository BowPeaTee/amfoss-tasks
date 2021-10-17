1. mkdir Coordinates-Location  
   cd Coordinates-Location/

2. mkdir North  
   cd North/  
	- i. echo "9°" > NDegree  
	- ii. echo "5’" > NMinutes.txt  
	- iii. echo "38.1\"" > NSeconds.txt  
	- iv. cat *.txt > NorthCoordinate.txt  
	- v. mv NorthCoordinate.txt North.txt  
	mv North.txt  ~/Desktop/Coordinates-Location
	   
3. cd ..

4. mkdir East  
   cd East/  
	- i) echo "76°" > EDegree.txt  
	- ii) echo "29'" > EMinutes.txt  
	- iii) echo "30.8\"" > ESeconds.txt  
	- iv) cat *.txt > EastCoordinate.txt  
	- v) mv EastCoordinate.txt East.txt  
	   mv East.txt ~/Desktop/Coordinates-Location/

5. cd ..  
   cat North.txt East.txt > Location-Coordinate.txt
  
![map ss](/task-02/mapss.png)
