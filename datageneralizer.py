import csv

with open('data.csv', 'r', encoding="utf8") as data:
    data_read = data.readlines()

x = csv.reader(data_read)
data_array = list(x)
with open("data_compressed.csv", "w", newline="") as datafile:#open a csv file to write to
    w = csv.writer(datafile)#set w equal to write
    w.writerow(["ID", "Artist", "Low Estimation Price", "High Estimation Price", "Hammer Price", "Size", "Medium"])#write the label row
    for i in data_array:
        id = i[0]
        Artist = i[1]
        Low = i[2]
        if(Low == "N/A"):
            Low = 0
        else:
            Low = round(float(Low), 2)
        High = i[3]
        if(High == "N/A"):
            High = 0
        else:
            High = round(float(High), 2)
        hammer = i[4]
        if(hammer == "Not Sold"):
            if(Low == 0):
                hammer = High
            else:
                hammer = ((Low+High)/2.0)
            hammer = round(hammer, 2)
        else:
            hammer = round(float(hammer), 2)
        size = i[5]
        medium = i[6]
        if(medium.find("Lithograph") >= 0):
            medium = "Lithograph"
        elif(medium.find("Etching") >= 0):
            medium = "Etching"
        elif(medium.find("Linocut") >= 0):
            medium = "Linocut"
        elif(medium.find("Screenprint") >= 0):
            medium = "Screenprint"
        elif((medium.find("Aquatint") >= 0) or (medium.find("aquatint") >= 0)):
            medium = "Aquatint"
        elif(medium.find("Print") >= 0):
            medium = "Print"
        elif(medium.find("Gicleé print") >= 0):
            medium = "Gicleé print"
        elif(medium.find("Woodcut") >= 0):
            medium = "Woodcut"
        elif(medium.find("Photolithography") >= 0):
            medium = "Photolithography"
        elif(medium.find("Photographic print") >= 0):
            medium = "Photographic print"
        elif(medium.find("Lino block") >= 0):
            medium = "Lino block"
        elif(medium.find("Watercolor") >= 0):
            medium = "Watercolor"
        elif(medium.find("Acrylic yarn") >= 0):
            medium = "Acrylic yarn"
        elif(medium.find("Mixed Media") >= 0):
            medium = "Mixed Media"
        elif(medium.find("Oil") >= 0):
            medium = "Oil"
        elif(medium.find("Pastel") >= 0):
            medium = "Pastel"
        elif(medium.find("Charcoal") >= 0):
            medium = "Charcoal"
        elif(medium.find("Pen") >= 0):
            medium = "Pen"
        elif(medium.find("Monotype") >= 0):
            medium = "Monotype"
        elif(medium.find("Pencil") >= 0):
            medium = "Pencil"
        elif(medium.find("Ink") >= 0):
            medium = "Ink"
        elif((medium.find("Acrylic") >= 0) & (medium.find("yarn") < 0)):#not to get confused with Acrylic yard
            medium = "Acrylic"
        elif((medium.find("Gouache") >= 0)):
            medium = "Gouache"
        elif((medium.find("Wood ") >= 0)):#space at end on purpose due to cases with woodcut
            medium = "Wood "
        elif((medium.find("Bronze") >= 0)):
            medium = "Bronze"
        elif((medium.find("Copper") >= 0)):
            medium = "Copper"
        elif((medium.find("Brass") >= 0)):
            medium = "Brass"
        elif((medium.find("Enamel") >= 0)):
            medium = "Enamel paint"
        elif((medium.find("Ceramic") >= 0)):
            medium = "Ceramic"
        elif(medium.find("Silkscreen") >= 0):
            medium = "Silkscreen"
        elif(medium.find("Offset") >= 0):
            medium = "Offset"
        elif(medium.find("Crayon") >= 0):
            medium = "Crayon"
        elif(medium.find("crayon") >= 0):
            medium = "Crayon"
        elif(medium.find("Serigraph") >= 0):
            medium = "Serigraph"
        elif(medium.find("Engraving") >= 0):
            medium = "Engraving"
        elif(medium.find("Airbrush") >= 0):
            medium = "Airbrush"
        elif(medium.find("Photograph") >= 0):
            medium = "Photograph"
        elif(medium.find("charcoal") >= 0):
            medium = "Charcoal"
        elif(medium.find("print") >= 0):
            medium = "Print"
        elif(medium.find("mixed media") >= 0):
            medium = "Mixed Media"
        elif(medium.find("pencil") >= 0):
            medium = "Pencil"
        elif(medium.find("ceramic") >= 0):
            medium = "Ceramic"
        elif(medium.find("Tapestry") >= 0):
            medium = "Tapestry"
        elif(medium.find("Glass mosaique") >= 0):
            medium = "Glass mosaique"
        elif(medium.find("canvas") >= 0):
            medium = "canvas"
        elif(medium.find("Clay") >= 0):
            medium = "Clay"
            
        w.writerow([id, Artist, Low, High, hammer, size, medium])
    


        

        
        

