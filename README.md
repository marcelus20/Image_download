# Image_download
This project shows how you can make a download using the python language

Due to the fact that many websites use different system regarding the URL patterns, the code written in this project retrieves images from two specific websites, the Ahnegao and the DeviantArt wallpapers site.
The first website we will be talking about is the Ahnegao blog. 
There is a post on this website called "Coletanea de imagens aleatorias" which is where the images will be downloaded. 

The first pattern we want to have a look at is the homepage URL, https://www.ahnegao.com.br/page/1.
The URL has a pattern at the end of it, the number. The algorithm looks at the URL that ends with that number and checks if that page has the desired post, if not, the number increments in 1. 
When it finds it, it retrieves the link and goes to the next page until it's retrieved all the links to the desired post across the pages. 
When all the links to the post are collected, it gets all the Images URL and makes the download to the directory you have chosen. 

For the DevianArt on the other hand, the patterns of the link changes, on the link
https://www.deviantart.com/customization/wallpaper/popular-all-time/?offset=0 the increment goes to the very end and each number at the end represents the image itself that is being displayed in that website list. 
So, for DevianArt class, the methods will be less complex and we will need just to go through the above link changing the end of it only.

There is an independent method called download_content(URL) that carries out the download. 
The other classes call this method through an instance at the very last step of the process of getting from the General URL to the image URL.

If you test this code, just clear the comment (#) at the very beginning of the last lines.


