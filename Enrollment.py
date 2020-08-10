import requests
import csv
from datetime import datetime
from time import sleep
from os import path

def main():
    while(True):
        result = coursesAPI()
        if len(result) != 0:
            if path.exists("result.csv"):
                with open('result.csv', 'a', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow([datetime.now(), result[0][6], result[1][6], result[2][6], result[3][6], result[4][6], result[5][6], result[6][6], result[7][6], result[8][6]])
            else:
                with open('result.csv', 'w', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow(["Date", "201", "202", "203", "204", "205", "206", "207", "212" , "217"])
                    writer.writerow([datetime.now(), result[0][6], result[1][6], result[2][6], result[3][6], result[4][6], result[5][6], result[6][6], result[7][6], result[8][6]])
        sleep(10)

def coursesAPI():
    headers = {
        'Host': 'apps.novasbe.pt',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://apps.novasbe.pt/Bachelor_Enrollment/Add-Drop',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en;q=0.9,pt-PT;q=0.8,pt;q=0.7,en-US;q=0.6',
        'Cookie': 'JSESSIONID=2DBAFB46C7BD5A84ABDCEF55414511D7',
    }

    response = requests.get("https://apps.novasbe.pt/Bachelor_Enrollment/Add-Drop/JSON",
        headers=headers).text


    removeLawComma = response.replace("Communication, Leadership and Ethics", "Communication Leadership and Ethics")
    tmp = removeLawComma.replace(']','').replace('[','')
    tmp2 = tmp.replace('"','').split(",")
    courses = []

    for i in range(0, int(len(tmp2)/9)):
        course = []
        for j in range(0, 9):
            current = tmp2[i*9+j]
            course.append(current)
        courses.append(course)

    targets = []
    for course in courses:
        # if course[0] == "1458" and (course[2] == "T205APT" or course[2] == "T207A"):
        if course[0] == "1458":
            # if int(course[6]) > 0:
            targets.append(course)

    # if(len(targets) > 1):
    #     targets.pop(1)

    return targets

main()