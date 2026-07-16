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
job_cards = soup.find_all('div', class_='jobCardNova_bigCard__W2xn3 jdbigCard')

# print(job_cards)
# Output: a list of BeautifulSoup Tag objects, one per job card
# (each is the full <div>...</div> block of HTML for that job posting)

jobs = []

# =====================================================
#   EXTRACT FIELDS FROM EACH JOB CARD
# =====================================================

for job in job_cards:
    print('-' * 20)

    job_title = job.find('h3', 'jobCardNova_bigCardTopTitleHeading__Rj2sC jdTruncation')

    company_name = job.find('span', 'jobCardNova_bigCardTopTitleName__M_W_m jdTruncationCompany')

    experience = job.find('span', 'jobCardNova_bigCardCenterListExp__KTSEc')

    salary = job.find('span', 'jobCardNova_bigCardCenterListExp__KTSEc')

    location = job.find('div', 'jobCardNova_bigCardCenterListLoc__usiPB jobCardNova_limits__G87pQ d-flex justify-content-start align-items-center')

    skills = job.find('ul', 'jobCardNova_skillsLists__7YifX d-flex align-items-center')

    jobs.append({
        'title'        : job_title.text,
        'company_name' : company_name.text,
        'experience'   : experience.text,
        'salary'       : salary.text,
        'location'     : location.text,
        'skills'       : skills.text.split(' '),
    })

print(jobs)
# Output (one dict per job, list grows with every posting found), e.g.:
# [
#   {'title': 'Python Developer', 'company_name': 'Sparks To Ideas Hiring For Sparks To Ideas',
#    'experience': '0 to 1 Yr', 'salary': '0 to 1 Yr',
#    'location': 'Junagadh, Gandhinagar+7Gandhinagar, Jamnagar, Rajkot, Bharuch, Bhavnagar, Surat, Vadodara, Ahmedabad',
#    'skills': ['numpy', 'django', 'sql', 'panda', 'python', 'machine', 'learning', 'deep', 'learning']},
#   {'title': 'Python Developer Internship', 'company_name': 'MAXGEN TECHNOLOGIES PRIVATE LIMITED',
#    'experience': '0 Yrs', 'salary': '0 Yrs',
#    'location': 'Gandhinagar, Gandhidham+3Gandhidham, Anand, Mehsana, Ahmedabad',
#    'skills': ['python', 'django', 'web', 'development', 'internship']},
#   {'title': 'Jr. Full Stack Python Developer', 'company_name': 'IMPACT HR AND KM SOLUTIONS',
#    'experience': '0 to 3 Yrs', 'salary': '0 to 3 Yrs',
#    'location': 'Nashik, Pune',
#    'skills': ['developers', 'python', 'numpy']},
#   ... (one entry per job card on the page)
# ]