import requests
import re
url = 'https://data.gov.gr/api/v1/query/mdg_emvolio?date_from=2021-01-16&date_to=2021-01-17'
#insert your key in APIKEY
headers = {'Authorization':'APIKEY'}
response = requests.get(url, headers=headers)
rawdata=response.json()
#Data sorting
data = ' '.join([str(elem) for elem in rawdata])
data = re.sub("'","",data)
data = re.sub(": ",":",data)
data = re.sub("{","",data)
data = re.sub("}","",data)
data = re.sub(r"\barea\b",",# area",data)
data = re.sub("referencedate:2021-01-16T00:00:00,","",data)
data = re.sub(",","\n",data)
data = re.sub("  "," ",data)
finaldata=data.split("#")

#Main
print("\nΚαλωσήλθατε στο πρόγραμμα ανάλυσης δεδομένων εμβολιασμού COVID-19\n")
print("Το πρόγραμμα αυτό θα σας δείξει όλα τα σημερινά δεδομένα για την πρόοδο του εμβολιασμού στην επιλεγμένη περιοχή")
print("Για να κλείσετε την εφαρμογή,πληκτρολογήστε ΕΞΟΔΟΣ")
print("Για να δείτε όλα τα δεδομένα,πληκτρολογήστε ΟΛΑ")
selection=""
while selection!="ΕΞΟΔΟΣ":
    selection=input("\nΕπιλέξτε δήμο/περιοχή ενδιαφέροντος(κεφαλαία ελληνικά): ")
    matching = ""
    valid=False
    for options in finaldata:
        if selection in options:
            matching = [s for s in finaldata if selection in s]
            print('\n'.join(matching))
            valid=True
            break
    if selection=="ΟΛΑ":
        for s in finaldata:
            print(s)
    if selection=="ΠΕΡΙΟΧΕΣ":
        print("Σύντομα κοντά σας")
        #data = re.sub("^area:\S+","",data)
        #print(data)
    if valid==False and selection!="ΕΞΟΔΟΣ" and selection!="ΟΛΑ":
        print("\nΗ περιοχή δεν βρέθηκε")
