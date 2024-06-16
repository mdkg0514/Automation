from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
user_data_path = "C:/Users/dwdqb/AppData/Local/Google/Chrome"
profile_name = "Dawood"
options = Options()
options.add_argument(f"--user-data-dir={user_data_path}")
options.add_argument(f"--profile-directory={profile_name}")
driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
wait = WebDriverWait(driver, 20)
connect_no = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/div/section/header/h1")))
len_conn = int(connect_no.text.split(" ")[0])
link_list = []
name_list = []
count = 0
# for i in range(2, len_conn):
for i in range(2, 607):
    try:
        # time.sleep()
        occupation = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/div/section/div[2]/div[1]/ul/li[{i}]/div/div/div[1]/a/span[4]")))
        driver.execute_script("window.scrollBy(0, 100);")
        name = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/div/section/div[2]/div[1]/ul/li[{i}]/div/div/div[1]/a/span[2]"))).text
        print(occupation.text)
        if "HR" in occupation.text:
            continue
        if "Mohsin Riaz" in name:
            continue
        l = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/div/section/div[2]/div[1]/ul/li[{i}]/div/div/a")))
        link = l.get_attribute("href")
        print(link)
        print(name)
        link_list.append(link)
        name_list.append(name)
        count = count + 1
        print(count)
    except Exception as e:
            print(f"Error processing connection {i}: {e}")
            continue
for i in range(len(link_list)):
    driver.get(link_list[i])
    try:
        time.sleep(3)
        msg_bar = wait.until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div[1]/div[1]/button")))
        msg_bar.click()
        # time.sleep(5)
        msg = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[5]/div[4]/aside[1]/div[2]/div[1]/div[2]/div/form/div[2]/div[1]/div/div[1]/p[3]")))
        msg.clear()
        time.sleep(2)
        msg_b = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[5]/div[4]/aside[1]/div[2]/div[1]/div[2]/div/form/div[2]/div[1]/div")))
        msg_b.click()
        msg.send_keys('''I hope you're doing well. My name is Dawood, and I'm reaching out because I see a great opportunity for us to collaborate in a way that could benefit us both.

I’m currently in the process of starting a software house focused on delivering top-notch software solutions to a wide range of clients. I’m confident in my project management and business development skills, but I need talented professionals like you to help bring this vision to life.

Here’s what I’m thinking:

Portfolio Collaboration: I’ve been really impressed by the work showcased on your LinkedIn profile. I believe your portfolio would be an excellent fit for the types of projects I’m aiming to secure. With your permission, I’d love to include your portfolio in our company’s profile to highlight our collective expertise.

Project Hunting: I’ll take on the role of project hunter, using my network and business skills to find and secure projects that match our combined talents.

Profit Sharing: For every project we successfully secure and complete, I propose a fair profit-sharing arrangement. This way, you can focus on what you do best—delivering outstanding work—while I handle client acquisition and management.

Currently, we are a team of 10 members freelancing in different fields. By joining us, you’ll be part of a diverse and talented group. I will hunt the projects for you, and in return, we will divide the earnings based on specific percentages.

What’s in it for you?

Increased Opportunities: Together, we can attract and take on more substantial and diverse projects than we might individually.
Focused Expertise: You can concentrate on your craft without worrying about finding and negotiating with clients.
Mutual Growth: As we complete projects, we’ll build a strong, diverse portfolio that attracts even more clients, leading to potential long-term collaboration and growth.
I genuinely believe that by working together, we can create a successful partnership that leverages our strengths and brings about rewarding projects. I’d love to discuss this opportunity further and answer any questions you might have.

Thank you for considering this collaboration. Looking forward to your positive response.

Best regards,

M. Dawood Iqbal
https://www.linkedin.com/in/mdawoodiqbal
mdawoodiqbal0514@gmail.com
03268675657''')
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[4]/aside[1]/div[2]/div[1]/div[2]/div/form/footer/div[2]/div[1]/button"))).click()
        time.sleep(4)
    except Exception as e:
            print(f"Error sending message to {name_list[i]}: {e}")
            continue