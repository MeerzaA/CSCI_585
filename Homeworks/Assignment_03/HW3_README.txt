MEERZA AHMED CSCI 585 HW3 | README- 11/3/2023

I put each part of the assignment in its own folder, this ReadMe will help any TA or the professor nevigate my submission. Note that every file has all materials needed for that question so there is no need to jump around. 

Please read what I wrote for each question, before opening the file, it will help you make sense of what you are seeing.  

Q1: The assignment stated that "[if you don't want to show your full face, that's ok, include just a part :)]". So I wrote my initials on my hand and just made sure to include my hand in every picture so that you can know it was me. I also checked with the professor after taking the pictures to make sure if it was okay to do it this way, and he said it was okay. My pictures are in the 13_Selfies folder, I also included screen shots of the lon/lat in the 13_LOC_ScreenShots folder. You can ignore the 13_Location_Notes file, I just made it to organize my lon/lat and location names.  

Q2: We weren't asked to submit anything from this part, I made a kml file with my 13 locations called 13_locations.kml and also placed my lon/lat locations in text files in four folders called department_buildings, Eateries, libraries, and waterworks since this part asked me to. If you open the kml file it will bring out all 13 locations I visited on campus amd location to my home. Note that I live far from campus so you might have to zoom out to see it, or you can directly locate it in google earth by checking the points in the left panel. 

Q3: All this part wanted us to do was load the kml in google earth and take a screen shot, I included the screen shot along with the same kml from part 2.  

Q4: We were asked to download either postgres or Oracle in this part. Since there was nothing to do in part 4 you can ignore this folder.

Q5: This was the longest part so there is a lot in this folder. 

For the CovexHull I made a table in postgres that contained spatial data, than I ran ST_CovexHull on my table to create the polygon, I noted the points from my query results and made a kml file that contained my 13 locations along with the polygon coordinates (CovexHull_Mapped.kml). Finally I took a screenshot of the kml file visualized in google earth (CovexHull_Mapped_ScreenCap). All my SQL code is in CovexHull_SQL.txt, CovexHull_SQL_Results.png is a screen cap of what my ST_Covex Hull query returned. 

For the nearest neigibor I ran a ST_Distance query on the same table I made for the CovexHull. You can find the qeury in Nearest_Neighbor_SQL.txt and the query results in Nearest_Neighbor_SQL_Results.png. I than took the locations the query generated and made 4 kml line segments, which you can see in the Nearest_Neighbor_Mapped_ScreemCap.png. If you want to see the kml visualized in google earth or read the code you can refer to Nearest_Neighbor_Mapped.kml 

Note that the assignment asked for both the CovexHull, and Nearest Neighbor to be in one kml, but on Piazza it was clearified that it wasn't nessessary to do it in this way. Also note that I kept the placemarkers intact in the kml files for CovexHull and Nearest Neighbor.  

Q6: For this part all we needed to do was adjust the OL.HTML file so that it worked with our locations and kept the coordinates in cache. We also needed to place our 13 locations on the map with the addMarker() function. My array with my 13 locations is at the top along with the "localStorage.setItem" function, and my loop to place all 13 locations on the map is at the bottom. I orignally did this in jsFiddle but later decided to do it locally, so that is why I have 2 files in this folder. jsFiddle.txt has the link to my jsFiddle project, and 13_LOC_Online is the same exact code but in a HTML file you can run locally. 

Note that I live far from campus, so you will need to zoom out a lot to see the other locations. 

Q7: For part 7 I wrote my SpiroGraph calculation in python, you can find my code in Spirograph.py, I used tommy trojan as my center which you can probably see from the Tommyt_x and Tommyt_y variables. I did some testing in javascript to make this work, I included that code in SpiroGraph.html but you can ignore this file. 

The kml file of the spirograph is called Spiro.kml in this file you will see the spirograph made up of points in side of USC's campus. I tried to be resonable with the scale so I didn't make it bigger than the campus.On Piazza someone said that the spirograph HAD to be made out of points so that what I did, I wanted to do this with lines but that was not what we were asked to do. Also note that my spirograph python code is for my machine, so it won't work if you run it. If you want to run it on your machine, you will need to delete the path in kml.save() method, change it to what ever is best for you. The mygeodata.zip is the shape file that I made to visualize the data in ARCgis, you can see the results in the Spirograph_ArcGis_Vis.png Note that the Spirograph doesnt look like a perfect spiral, this is because my monitor is a Ultrawide and I have a 21:9 ratio, the normal ratios are usually 16:9. I am assuming the streatched aspect ratio is why my results seem off, but is logically correct. 
