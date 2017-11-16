import requests


#IF YOU WANT TO CHANGE THE SAVING DIRECTORY, MAKE SURE YOU HAVE CREATED IT.

counter = 1
saving_directory = "D:\\test\\"

class Download_stuff:
    def __init__(self):
        pass

    #THIS METHOD MAKES THE DOWNLOAD FROM THE CONTENT
    def download_content(self, url, directory, name_index):
        global counter

        content = requests.get(url).content
        content_name = name_index + url.split("/")[-1]#LAST PART OF THE LINK, THEREFORE THE NAME

        print("Downloading the {} image: ".format(counter))
        f = open(directory+content_name, "wb")
        f.write(content)
        f.close()
        print("Done!")
        counter +=1

class Ahnegao():
    def __init__(self):
        pass

    def looking_for_post(self, url, post_name):



        code = requests.get(url).content
        code = str(code, "utf-8")
        for row in code.split(" "):
            if "html" in row and post_name in row:
                row = row.split("\"")[1]
                break
        if "index" not in row:
            print(row)
            return row


    def get_content(self, extension_file, url):

        downl = Download_stuff()

        content = requests.get(url).content
        content = str(content, "utf-8")

        content_list = []

        for i in content.split(" "):
            if extension_file in i and "http" in i and extension_file in i and "<" not in i:
                content_url = i.split("\"")[-1]
                if "x" not in content_url:
                    if content_url != "":
                        content_list.append(content_url)

        for i in content_list:
            downl.download_content(i, saving_directory, i.split("/")[-3]+i.split("/")[-2])

    def going_trhough_pages(self, stop):

        post_link = []
        #This could be any post you like, I chose the coletanea de images aleatorias to make the download
        post_name = "coletanea-de-ima"
        for i in range(1,stop):
            print("looking for page "+str(i))
            link = self.looking_for_post("https://www.ahnegao.com.br/page/{}".format(i), post_name)
            if link != None:
                if link not in post_link:
                    post_link.append(link)
        for links in post_link:
            print(links)
            self.get_content("img", links)


class Devian_art():
    def __init__(self):
        pass
    def going_through_pages(self,stop):
        downl = Download_stuff
        url = "https://www.deviantart.com/customization/wallpaper/popular-all-time/?offset="

        content_url = []
        print("Retrieving links... It may take few minutes...")
        for i in range(stop):
            content = requests.get(url+str(i)).content
            content = str(content, "utf-8")
            print("link: "+str(i+1)+ " retrieved")




            for i in content.split(" "):
                if ".jpg" in i and "http" in i and "data-meta" in i:
                    content_link = i.split("\"")[-2]#JUST RETRIEVING THE LINK OUT OF I
                    if content_link not in content_url:
                        content_url.append(content_link)
                    break

        for i in content_url:
            print(i)
            downl.download_content(i, i, saving_directory, i.split("/")[-3])


#TESTING THE CODE.

#b = Ahnegao()
#b.going_trhough_pages(15)#Looking for a post  on the first 50 pages and making the download

#c = Devian_art()
#c.going_through_pages(10)#Retrieving the 5 first images link.
