import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

headers = {'User-Agent': 'Mozilla/5.0'}
jobs_list = []

germany_cities = [
    "Germany", "Berlin", "München", "Hamburg", "Frankfurt", "Köln", "Stuttgart", "Düsseldorf",
    "Leipzig", "Dresden", "Hannover", "Nürnberg", "Bremen", "Essen", "Dortmund"
]

keywords = [
    "Marketingfachkraft", "Marketing Specialist", "Marketing Manager",
    "Marketingmitarbeiter", "Online Marketing", "Digital Marketing",
    "Marketing Koordinator", "Marketing Coordinator", "Marketingreferent",
    "Marketingberater", "Marketing Consultant", "Marketing Professional",
    "Kommunikationsmanager", "PR Manager", "Content Manager"
]
print('start!')
for city in germany_cities:
    for kw in keywords:
        for start in range(0, 250, 25):
            kw_encoded = kw.replace(" ", "%20").replace("ü", "u").replace("ä", "a").replace("ö", "o").replace("ß", "ss")
            city_encoded = city.replace(" ", "%20").replace("ü", "u").replace("ä", "a").replace("ö", "o").replace("ß", "ss")
            url = f'https://www.linkedin.com/jobs/search/?keywords={kw_encoded}&location={city_encoded}&f_TPR=r2592000&start={start}'
            try:
                response = requests.get(url, headers=headers, timeout=15)
                soup = BeautifulSoup(response.text, 'html.parser')
                job_cards = soup.find_all('div', class_='base-card')

                for job in job_cards:
                    title = job.find('h3', class_='base-search-card__title').text.strip() if job.find('h3', class_='base-search-card__title') else ''
                    company = job.find('h4', class_='base-search-card__subtitle').text.strip() if job.find('h4', class_='base-search-card__subtitle') else ''
                    location = job.find('span', class_='job-search-card__location').text.strip() if job.find('span', class_='job-search-card__location') else ''
                    link = job.find('a', class_='base-card__full-link')['href'] if job.find('a', class_='base-card__full-link') else ''
                    jobs_list.append({
                        'Title': title,
                        'Company': company,
                        'Location': location,
                        'Link': link,
                        'Keyword': kw,
                        'City': city
                    })
                time.sleep(random.uniform(0.7, 1.2))

            except Exception as e:
                print("❌ Error:", e)
                time.sleep(10)

print("📝 Fetching job descriptions...")
batch_size = 500
results_batch = []
total = len(jobs_list)
output_file = 'raw_qa_Marketing_germany.csv'

for i, job in enumerate(jobs_list):
    url = job['Link']
    try:
        response = requests.get(url, headers=headers, timeout=12)
        soup = BeautifulSoup(response.text, 'html.parser')
        desc_block = soup.find('div', {'class': lambda x: x and 'description' in x})
        if desc_block:
            description = desc_block.get_text(separator=' ', strip=True)
        else:
            description = 'Not found'
    except Exception as e:
        print("❌ Error:", e)
        description = 'Error'

    job['Description'] = description
    results_batch.append(job)
    time.sleep(random.uniform(1, 1.7))

    # === Каждые batch_size, или последний ===
    if ((i + 1) % batch_size == 0) or (i + 1 == total):
        df = pd.DataFrame(results_batch)
        if i < batch_size:  # Первый батч, пишем с заголовками
            df.to_csv(output_file, index=False, mode='w')
        else:               # Остальные — без header, дописываем
            df.to_csv(output_file, index=False, header=False, mode='a')
        print(f"💾 Batch saved: {i + 1} / {total}")
        results_batch = []

print(f"✅ {output_file} готов. Теперь твой ноут скажет спасибо.")
