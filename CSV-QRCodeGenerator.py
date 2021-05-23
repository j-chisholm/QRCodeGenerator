import csv
import qrcode
import os
import shutil
import time

#Enter the name of the CSV file here
CSVFILE = ""

#Enter the column number for the list of items to generate QR Codes for
COLNUMBER = 0 #Defaulted to 0

#Enter the name of the heading of the column, this value is used to
#prevent the code from making a QR Code for the heading name
HEADINGNAME = ""

QRFOLDER = "QRCodes" #Name of the folder to store the QR Codes
QREXTENSION = 'JPEG' #File extension of the QR Code

#Check if the proper csv file exists
if os.path.isfile(CSVFILE):

    #Make the QRCodes folder if it has not already been made
    if os.path.exists(QRFOLDER):
        #Delete preexisting folder and any qrcodes within
        shutil.rmtree(QRFOLDER)
        #Remake the folders
        os.makedirs(QRFOLDER)
    else:
        #Make the folder if it doesn't exist
        os.makedirs(QRFOLDER)

    #Open the csv file
    with open(CSVFILE) as CSVFILE:
        inventoryReader = csv.reader(CSVFILE, delimiter=",", quotechar='"')

        #Make a qrcode for each item
        for row in inventoryReader:
            item = str(row[COLNUMBER])

            #Skip the heading of the column
            if (item.upper() == HEADINGNAME):
                continue

            #Construct QRCode path
            qrCodePath = str(QRFOLDER + '\\' + item + ".jpg")

            #Make the QRCode 
            qrCode = qrcode.make(item)

            #Save QRCode to QRFolder
            qrCode.save(qrCodePath, QREXTENSION)

    #Close the file
    CSVFILE.close()

    #Delete csv file to prevent file mixup
    os.remove(CSVFILE)

else:
    print("Place CSV File in the same folder as the Generator")
    time.sleep(5)
