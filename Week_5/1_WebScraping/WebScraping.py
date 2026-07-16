import requests
from bs4 import BeautifulSoup

# =====================================================
#   BASIC CONNECTION
# =====================================================

url = "https://www.shine.com/job-search/python-developer-jobs?suid=492ef81f-b981-478f-a326-43ab2ccfd32c&q=python-developer&qActual=Python+developer&minexp=2&hidden_id_exp=2"

headers = {
    "User-Agent"      : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept"          : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language" : "en-US,en;q=0.5",
}

# =====================================================
#   GET REQUEST
# =====================================================

response = requests.get(url, headers=headers, timeout=10)

html_content = response.text
# print(html_content)   # raw HTML of the job search page (only needed for debugging selectors)

# =====================================================
#   PARSE WITH BEAUTIFULSOUP
# =====================================================
soup = BeautifulSoup(html_content, 'html.parser')

# Each job posting on the page sits inside a div with this class
job_cards = soup.find_all("div", class_="jobCardNova_bigCard__W2xn3 jdbigCard")

# print(job_cards)
# Output: a list of BeautifulSoup Tag objects, one per job card
# (each is the full <div>...</div> block of HTML for that job posting)

jobs = []
# =====================================================
#   EXTRACT FIELDS FROM EACH JOB CARD
# =====================================================
for job in job_cards:
    print("-"*20)
    post_date = job.find("span", class_="jobCardNova_postedData__LTERc")
    # print(post_date.text)
    job_title = job.find("h3", class_="jobCardNova_bigCardTopTitleHeading__Rj2sC jdTruncation")
    # print(job_title.text)
    company_name = job.find("span", class_="jobCardNova_bigCardTopTitleName__M_W_m jdTruncationCompany")
    # print(company_name.text)
    experience = job.find("span", class_="jobCardNova_bigCardCenterListExp__KTSEc")
    # print(experience.text)
    location = job.find("div", class_="jobCardNova_bigCardCenterListLoc__usiPB jobCardNova_limits__G87pQ d-flex justify-content-start align-items-center")
    # print(location.text)
    skills = job.find("div", class_="jobCardNova_setskills__kMYTq d-flex align-items-center justify-content-start")
    # print(skills.text.split(" "))

    jobs.append({
        'post_date' : post_date.text,
        'job_title' : job_title.text,
        'company_name' : company_name.text,
        'experience' : experience.text,
        'location' : location.text,
        'skills' : skills.text.split(' '),
    })

print(jobs)

import json

with open("jobs.json", "w") as file:
    json.dump(jobs, file, indent=4)