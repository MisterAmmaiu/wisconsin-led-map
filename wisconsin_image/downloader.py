import urllib.request
import urllib.parse

### Global Variables ###

START_X = -10350185.0
START_Y =   5975650.0
END_X   =  -9600185.0
END_Y   =   5229650.0

STEP_SIZE = 10
STEP_TOTL = STEP_SIZE**2

STEP_X = abs(START_X-END_X) / STEP_SIZE
STEP_Y = abs(START_Y-END_Y) / STEP_SIZE

RES_X = RES_Y = "1000"

OUTPUT_FOLDER = "output/"



### Functions ###

# This function takes a given x and y position, translates
# them into the correct bounding box coordinates, and places
# these coordinates into the API url which is then returned
def getImageURL(posX, posY):
    minX = round(posX, 9)
    maxY = round(posY, 9)
    maxX = round(posX + STEP_X, 9)
    minY = round(posY - STEP_Y, 9)
    coordString = str(minX)+","+str(minY)+","+str(maxX)+","+str(maxY)
    coordStringCoded = urllib.parse.quote(coordString)
    url = "https://dnrmaps.wi.gov/arcgis_image/rest/services/DW_Imagery/EN_Image_Basemap_Latest_Leaf_Off/ImageServer/exportImage?f=image&bbox="+coordStringCoded+"&bboxSR=102100&size="+RES_X+"%2C"+RES_Y+"&imageSR=102100&time=&format=png&pixelType=UNKNOWN&noData=&noDataInterpretation=esriNoDataMatchAny&interpolation=+RSP_BilinearInterpolation&compression=&compressionQuality=&bandIds=&sliceId=&mosaicRule=%7B%22ascending%22%3Atrue%2C%22mosaicMethod%22%3A%22esriMosaicNorthwest%22%2C%22mosaicOperation%22%3A%22MT_FIRST%22%7D&renderingRule=&adjustAspectRatio=true&validateExtent=false&lercVersion=1&compressionTolerance=&f=html"
    return url



### MAIN EXECUTION ###

print("Downloading wisconsin...")
posY = START_Y
itrY = 0
# This loop will download the specifying grid (default 10x10) of Wisconsin
# working row by row from the topmost row to the bottommost row. Each cell
# will be outputted as an image with the filename x_y.png, where x is the
# column index and y is the row index, starting from the top-left corner
while (posY > END_Y):
    itrX = 0
    posX = START_X
    while (posX < END_X):
        # Get image
        print("Downloading "+str(itrY*STEP_SIZE + itrX)+"/"+str(STEP_TOTL))
        img_url = getImageURL(posX, posY)
        img_name = str(itrX)+"_"+str(itrY)+".png"
        urllib.request.urlretrieve(img_url, OUTPUT_FOLDER+img_name)
        # Iterate x position, iterator
        posX += STEP_X
        itrX += 1
    # Iterate y position, iterator
    posY -= STEP_Y
    itrY += 1

