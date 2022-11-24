import csv
import re

#reading the regions from the csv file and assigning it to the regions list
regions = []
def readRegionsFromCSVFile():
    elem_str = ""
    global regions
    
    #reading from the file
    with open('region.csv', mode='r') as region:
        readRegions = csv.reader(region)
		
		#removing the brackets and the single quotation marks from the elements
        for i in readRegions:
            elem_str = str(i)
            slicedElement = elem_str[2:]
            elementWithoutBackBracket = re.findall(".*(?='])", slicedElement)
            bracketlessElementString = ''.join(elementWithoutBackBracket)
            regions.append(bracketlessElementString)
        
        #checking the contents of the regions list
        for element in regions:
        	print(element)
		
		
		
		
		
	
		
#reading the network from the csv file and assigning it to the network list
network = []
def readNetworkFromCSVFile():
    elem_str = ""
    global network
    
    #reading from the file
    with open('network.csv', mode='r') as networks:
        readNetwork = csv.reader(networks)
		
		#removing the brackets and the single quotation marks from the elements
        for i in readNetwork:
            elem_str = str(i)
            slicedElement = elem_str[2:]
            elementWithoutBackBracket = re.findall(".*(?='])", slicedElement)
            bracketlessElementString = ''.join(elementWithoutBackBracket)
            network.append(bracketlessElementString)
        
        #checking the contents of the network list
        for element in network:
        	print(element)
		
    
    



  
  
  
#reading the ids from the csv file and assigning it to the ID list
ID = []
def readIDFromCSVFile():
    elem_str = ""
    global ID
    
    #reading from the file
    with open('id.csv', mode='r') as ids:
        readID = csv.reader(ids)
		
		#removing the brackets and the single quotation marks from the elements
        for i in readID:
            elem_str = str(i)
            slicedElement = elem_str[2:]
            elementWithoutBackBracket = re.findall(".*(?='])", slicedElement)
            bracketlessElementString = ''.join(elementWithoutBackBracket)
            ID.append(bracketlessElementString)
        
        #checking the contents of the ID list
        for element in ID:
        	print(element)
		          





#reading the admins from the csv file and assigning it to the admins list
admin = []
def readAdminFromCSVFile():
    elem_str = ""
    global admin
    
    #reading from the file
    with open('admin.csv', mode='r') as admins:
        readAdmin = csv.reader(admins)
		
		#removing the brackets and the single quotation marks from the elements
        for i in readAdmin:
            elem_str = str(i)
            slicedElement = elem_str[2:]
            elementWithoutBackBracket = re.findall(".*(?='])", slicedElement)
            bracketlessElementString = ''.join(elementWithoutBackBracket)
            admin.append(bracketlessElementString)
        
        #checking the contents of the admin list
        for element in admin:
        	print(element)
		          



#reading the serNo from the csv file and assigning it to the serNo list
serNo = []
def readSerNoFromCSVFile():
    elem_str = ""
    global serNo
    
    #reading from the file
    with open('serno.csv', mode='r') as serNos:
        readSerNo = csv.reader(serNos)
		
		#removing the brackets and the single quotation marks from the elements
        for i in readSerNo:
            elem_str = str(i)
            slicedElement = elem_str[2:]
            elementWithoutBackBracket = re.findall(".*(?='])", slicedElement)
            bracketlessElementString = ''.join(elementWithoutBackBracket)
            serNo.append(bracketlessElementString)
        
        #checking the contents of the serNo list
        for element in serNo:
        	print(element)
		          




#reading the regID from the csv file and assigning it to the regID list
regID = []
def readRegIDFromCSVFile():
    elem_str = ""
    global regID
    
    #reading from the file
    with open('reg-id.csv', mode='r') as regIDs:
        readRegIDs = csv.reader(regIDs)
		
		#removing the brackets and the single quotation marks from the elements
        for i in readRegIDs:
            elem_str = str(i)
            slicedElement = elem_str[2:]
            elementWithoutBackBracket = re.findall(".*(?='])", slicedElement)
            bracketlessElementString = ''.join(elementWithoutBackBracket)
            regID.append(bracketlessElementString)
        
        #checking the contents of the regID list
        for element in regID:
        	print(element)
		          




#reading the subID from the csv file and assigning it to the subID list
subID = []
def readSubIDFromCSVFile():
    elem_str = ""
    global subID
    
    #reading from the file
    with open('subscr-id.csv', mode='r') as subIDs:
        readSubIDs= csv.reader(subIDs)
		
		#removing the brackets and the single quotation marks from the elements
        for i in readSubIDs:
            elem_str = str(i)
            slicedElement = elem_str[2:]
            elementWithoutBackBracket = re.findall(".*(?='])", slicedElement)
            bracketlessElementString = ''.join(elementWithoutBackBracket)
            subID.append(bracketlessElementString)
        
        #checking the contents of the subID list
        for element in subID:
        	print(element)
		          







#reading the descr from the csv file and assigning it to the descr list
descr = []
def readDescFromCSVFile():
    elem_str = ""
    global descr
    
    #reading from the file
    with open('descr.csv', mode='r') as descrs:
        readDescr= csv.reader(descrs)
		
		#removing the brackets and the single quotation marks from the elements
        for i in readDescr:
            elem_str = str(i)
            slicedElement = elem_str[2:]
            elementWithoutBackBracket = re.findall(".*(?='])", slicedElement)
            bracketlessElementString = ''.join(elementWithoutBackBracket)
            descr.append(bracketlessElementString)
        
        #checking the contents of the descr list
        for element in descr:
        	print(element)
		          




#reading the ONTProf from the csv file and assigning it to the ONTProf list
ONTProf = []
def readONTProfFromCSVFile():
    elem_str = ""
    global ONTProf
    
    #reading from the file
    with open('ontprof.csv', mode='r') as ONTProfs:
        readONTProf= csv.reader(ONTProfs)
		
		#removing the brackets and the single quotation marks from the elements
        for i in readONTProf:
            elem_str = str(i)
            slicedElement = elem_str[2:]
            elementWithoutBackBracket = re.findall(".*(?='])", slicedElement)
            bracketlessElementString = ''.join(elementWithoutBackBracket)
            ONTProf.append(bracketlessElementString)
        
        #checking the contents of the ONTProf list
        for element in ONTProf:
        	print(element)
		          




#reading the LOW_RX_OPT_PWR_NE_THRESH from the csv file and assigning it to the LOW_RX_OPT_PWR_NE_THRESH list
LOW_RX_OPT_PWR_NE_THRESH = []
def readLOW_RX_OPT_PWR_NE_THRESHFromCSVFile():
    elem_str = ""
    global LOW_RX_OPT_PWR_NE_THRESH
    
    #reading from the file
    with open('LOW-RX-OPT-PWR-NE-THRESH.csv', mode='r') as LOW_RX_OPT_PWR_NE_THRESHs:
        readLROPNT= csv.reader(LOW_RX_OPT_PWR_NE_THRESHs)
		
		#removing the brackets and the single quotation marks from the elements
        for i in readLROPNT:
            elem_str = str(i)
            slicedElement = elem_str[2:]
            elementWithoutBackBracket = re.findall(".*(?='])", slicedElement)
            bracketlessElementString = ''.join(elementWithoutBackBracket)
            LOW_RX_OPT_PWR_NE_THRESH.append(bracketlessElementString)
        
        #checking the contents of the LOW_RX_OPT_PWR_NE_THRESH list
        for element in LOW_RX_OPT_PWR_NE_THRESH:
        	print(element)
		          




#reading the  HIGH_RX_OPT_PWR_NE_THRESH  from the csv file and assigning it to the  HIGH_RX_OPT_PWR_NE_THRESH  list
HIGH_RX_OPT_PWR_NE_THRESH = []
def readHIGH_RX_OPT_PWR_NE_THRESHFromCSVFile():
    elem_str = ""
    global  HIGH_RX_OPT_PWR_NE_THRESH 
    
    #reading from the file
    with open('HIGH-RX-OPT-PWR-NE-THRESH.csv', mode='r') as  HIGH_RX_OPT_PWR_NE_THRESHs:
        readHROPNT= csv.reader(HIGH_RX_OPT_PWR_NE_THRESHs)
		
		#removing the brackets and the single quotation marks from the elements
        for i in readHROPNT:
            elem_str = str(i)
            slicedElement = elem_str[2:]
            elementWithoutBackBracket = re.findall(".*(?='])", slicedElement)
            bracketlessElementString = ''.join(elementWithoutBackBracket)
            HIGH_RX_OPT_PWR_NE_THRESH .append(bracketlessElementString)
        
        #checking the contents of the  HIGH_RX_OPT_PWR_NE_THRESH  list
        for element in  HIGH_RX_OPT_PWR_NE_THRESH :
        	print(element)
		          



#reading the  BATTERY_PRESENT  from the csv file and assigning it to the  BATTERY_PRESENT  list
BATTERY_PRESENT = []
def readBATTERY_PRESENTFromCSVFile():
    elem_str = ""
    global  BATTERY_PRESENT 
    
    #reading from the file
    with open('BATTERY-PRESENT.csv', mode='r') as  BATTERY_PRESENTs:
        readBATTERY_PRESENT= csv.reader(BATTERY_PRESENTs)
		
		#removing the brackets and the single quotation marks from the elements
        for i in readBATTERY_PRESENT:
            elem_str = str(i)
            slicedElement = elem_str[2:]
            elementWithoutBackBracket = re.findall(".*(?='])", slicedElement)
            bracketlessElementString = ''.join(elementWithoutBackBracket)
            BATTERY_PRESENT .append(bracketlessElementString)
        
        #checking the contents of the  BATTERY_PRESENT  list
        for element in  BATTERY_PRESENT :
        	print(element)
		          




readRegionsFromCSVFile()
readNetworkFromCSVFile()
readIDFromCSVFile()
readAdminFromCSVFile()
readSerNoFromCSVFile()
readRegIDFromCSVFile()
readSubIDFromCSVFile()
readDescFromCSVFile()
readONTProfFromCSVFile()
#readLOW_RX_OPT_PWR_NE_THRESHFromCSVFile()
#readHIGH_RX_OPT_PWR_NE_THRESHFromCSVFile()
#readBATTERY_PRESENTFromCSVFile()
